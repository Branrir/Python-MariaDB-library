import mysql.connector as mariadb

##MariaDB configuration
mariadb_conn = mariadb.connect(user='java', password='123',database='library')
cursor = mariadb_conn.cursor

try:
cursor.execute("SELECT * FROM games")
except mariadb.Error as error:
    print("Error: {}".format(Error))
for id, name, jahr, gerne, console in cursor:
    print("ID: {}, Name: {}, Jahr: {}, Gerne: {}, Console: {}").format(id, name, jahr, gerne, console)
