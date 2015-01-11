import mysql.connector
import config
 

select_temperature = ("SELECT temp1, temp2, created_at from temps ORDER BY created_at DESC LIMIT 1")
try:
  cnx = mysql.connector.connect(**config.mysql)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  cursor = cnx.cursor()
  cursor.execute(select_temperature)
  for (temp1, temp2, created_at) in cursor:
    print("{}, {} {:%H:%M (%d %b %Y)}".format(temp1, temp2, created_at))
  cnx.commit()
  cursor.close()
  cnx.close()

