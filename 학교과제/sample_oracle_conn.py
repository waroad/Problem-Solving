# Oracle Instant Client (for windows) 설치 필요 
# https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
import os
import sys

os.chdir('D:\\oracle\\instantclient_21_7')
os.putenv('NLS_LANG', 'AMERICAN_AMERICA.UTF8')

#import cx_Oracle module 
# For installation, refer to https://pypi.org/project/cx-Oracle/. 
# command: pip install cx-Oracle
import cx_Oracle 

print("---- Start of Oracle-Python Test ---\n") 
USER_ID = "university"
USER_PW = "comp322"
CONN_STR = "localhost:1521/orcl"
TABLE_NAME = "TEST"

lib_dir = "D:\\oracle\\instantclient_21_7"
try:
    print("\n >>> Oracle client initiatization starts ...\n");
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Error connecting: cx_Oracle.init_oracle_client()")
    print(err);
    sys.exit(1);

print("\n <<< Oracle client initiatization ended ...\n");

# Make a connection
try:
    # [id]/[password]@[server_address]/[SID]
    conn = cx_Oracle.connect(USER_ID + "/" + USER_PW + "@" + CONN_STR)
except:    # 예외가 발생했을 때 실행됨
    print('Cannot get a connection.')

print("\n >>> Successfully connected to Oracle Database <<< \n")

# Execute an SQL statement for CREATE TABLE
TABLE_NAME = "TEST"
try:
    # Make a connection cursor
    cursor = conn.cursor()
    sql = "DROP TABLE " + TABLE_NAME
    cursor.execute(sql)
    sql = "CREATE TABLE " + TABLE_NAME + "(Id NUMBER, Name VARCHAR(10), Address VARCHAR(20))"
    cursor.execute(sql)
    print(">>> Created TABLE " + TABLE_NAME + " Successfully") 
    # Make the changes permanent
    conn.commit()
except:
    print('[ERROR]: Create table')  

# Execute an SQL statement for INSERT
try:
    print("\n >>> Generating tuples\n")
    # Make a dataset for INSERT query
    data = [ (10, 'SUH', 'Daegu'), (20, 'PARK', 'Busan'), (30, 'Rivera', 'New York'), (40, 'Ryu', 'Los Angeles') ]
    print(">>> Inserting the tuples...\n")
    cursor.executemany( "INSERT INTO TEST (Id, Name, Address) VALUES (:1, :2, :3)", data)
    conn.commit()
except:
    print('Insert value ERROR.')

print("\n <<< INSERT succeeded.\n")

# Execute an SQL statement for SELECT
try:
    print("\n >>> Query starts...\n")
    sql = "SELECT * FROM " + TABLE_NAME 
    cursor.execute(sql)
    for row in cursor:
        print("ID = " + str(row[0]) + ", Name = " + row[1] + ", Address = " + row[2])
except:
    print('Select ERROR.')

print("\n <<< Query ended...")

# Execute an SQL statement for UPDATE, DELETE
try:
    print("\n >>> Update starts...\n")
    sql = "UPDATE TEST SET Name = 'Oh' WHERE Id = 40"
    cursor.execute(sql)
    print('\n <<< UPDATE Success\n')
    print("\n >>> DELETE starts...\n")
    sql = "DELETE FROM TEST WHERE Id = 30"
    cursor.execute(sql)
    print('\n <<< DELETE Success\n')
    conn.commit()
except:
    print('UPDATE/DELETE ERROR.')

# Execute the same SELECT statement in a different way
try:
    print('\n >>> UPDATE check start\n')
    cursor.execute("select * from " + TABLE_NAME + " where Id = :did", did=40)
    for row in cursor:
        print("ID = " + str(row[0]) + ", Name = " + row[1] + ", Address = " + row[2])
    print('\n <<< UPDATE check end\n')
    #conn.commit()
except:
    print('SELECT ERROR.')

# Release database resources.
try:
    print("\n >>> Cursor/connection closing...\n") 
    cursor.close()
    conn.close()
    print("\n <<< Cursor/connection closed.\n") 

except:
    print('Quit ERROR.')
    
print("---- End of Oracle-Python Test ---\n") 

