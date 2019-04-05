#!/usr/bin/python
import sys, os
import mysql.connector

class MariaDBintegration:
#MariaDB integration
#MariaDB configuration


db = mysql.connector.connect(user='java', password='123',database='library')
cursor = db.cursor()

    def Return_games():
    #select from table
        try:
            cursor.execute("SELECT * FROM games")
        except mariadb.Error as error:
            print("Error: {}".format(Error))
        for id, name, jahr, gerne, console in cursor:
            print("ID: {}, Name: {}, Jahr: {}, Gerne: {}, Console: {}".format(id, name, jahr, gerne, console))

        #Close connection"""
        db.close()
