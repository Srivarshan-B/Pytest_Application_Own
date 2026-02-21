import mysql.connector
from utilities import dbUtility

# mysql_connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="12345",
#     database="pydb",
# )
#
# mydb = mysql_connection.cursor()
# mydb.execute("SELECT * FROM SELENIUM")
#
# result = mydb.fetchone()
# print(result[1])


dbUtility.db_Connection()
final_result = dbUtility.getresult("Select * from Selenium where tutorial_id = 3")
print(final_result)



