#!/usr/bin/python
import sys, os
import mysql.connector as mariadb
from mysql.connector import Error
from mysql.connector import errorcode

class MariaDBintegration:
#MariaDB integration

    #select from table
    def Return_games():
        #MariaDB configuration
        db = mariadb.connect(user='java', password='123',database='library')
        cursor = db.cursor()

        try:
            cursor.execute("SELECT * FROM games")
        except mariadb.Error as error:
            print("Error: {}".format(error))
        for id, name, jahr, gerne, console in cursor:
            print("ID: {}, Name: {}, Jahr: {}, Gerne: {}, Console: {}".format(id, name, jahr, gerne, console))

        #Close connection"""
        db.close()

    #insert entry in table games
    def Insert_games(name, jahr, gerne, console):
        #MariaDB configuration
        db = mariadb.connect(user='java', password='123',database='library')
        cursor = db.cursor()
        sql = 'INSERT INTO games (name, jahr, gerne, console) VALUES ("{}", "{}", "{}", "{}")'.format(name, jahr, gerne, console)
        print(sql)
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))




    #remove entry from table games
    def Delete_games(id, name):
        #MariaDB configuration
        db = mariadb.connect(user='java', password='123',database='library')
        cursor = db.cursor()
        print(id)
        print(name)
        sql = 'DELETE FROM games WHERE id={} AND name="{}"'.format(id, name)
        print(sql)
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))
        print("Succesfull delete")
