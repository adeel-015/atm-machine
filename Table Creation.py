import mysql.connector as sql
print("Use only ONCE on a system.")
con=sql.connect(host='localhost',user='root',password='toor')
if con.is_connected():
      print("Successfully Connected")
con1=con.cursor()
con1.execute("CREATE DATABASE IF NOT EXISTS ATM_MACHINE")
con1.execute("USE ATM_MACHINE")
con1.execute("CREATE TABLE RECORDS( ACCOUNT_NO  INT(4) primary key,PASSWORD INT(3),NAME VARCHAR(20),CURRENT_AMOUNT INT default(0),WITHDRAWL INT default(0),BALANCE INT default(0))")
print("Successfully Created")
