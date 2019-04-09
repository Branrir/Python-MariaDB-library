#!/usr/bin/python
import sys, os
import mysql.connector as mariadb
from mysql.connector import Error
from mysql.connector import errorcode
from settings import *

class MariaDBintegration:
#MariaDB integration (Input, Delete, Return)

    #select from table
    def Return_games():
        #MariaDB configuration

        db = mariadb.connect(host= host, user= user, password= password,database= database)
        cursor = db.cursor()
        sql="SELECT * FROM games"

        tempgames = ""
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))
            errortext = "Error: {}".format(error)
            return errortext
        finally:
            for id, name, jahr, gerne, console in cursor:
                tempgames +="\n" + "ID: {},    Name: {},   Jahr: {},   Gerne: {},   Console: {} ".format(id, name, jahr, gerne, console)
            return tempgames
        #Close connection"""
        db.close()

    #insert entry in table games
    def Insert_games(name, jahr, gerne, console):
        #MariaDB configuration
        db = mariadb.connect(host= host, user= user, password= password,database= database)
        cursor = db.cursor()
        sql = "INSERT INTO games (name, jahr, gerne, console) VALUES ('{}', '{}', '{}', '{}')".format(name, jahr, gerne, console)
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))
            errortext = "Error: {}".format(error)
        finally:
            print("Succesfull insert")

        db.commit()
        db.close()

    #remove entry from table games
    def Delete_games(id, name):
        #MariaDB configuration
        db = mariadb.connect(host= host, user= user, password= password,database= database)
        cursor = db.cursor()
        print(id)
        print(name)
        sql = "DELETE FROM games WHERE id='{}' AND name='{}'".format(id, name)
        print(sql)
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))
            errortext = "Error: {}".format(error)
        finally:
        print("Succesfull delete")

        db.commit()
        db.close()


    #insert entry in table books
    def Insert_books(name, author, jahr, volume, lang):
        #MariaDB configuration
        db = mariadb.connect(host= host, user= user, password= password,database= database)
        cursor = db.cursor()
        sql = "INSERT INTO books (name, author, jahr, volume, lang) VALUES ('{}', '{}', '{}', '{}', '{}')".format(name, author, jahr, volume, lang)
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))
            errortext = "Error: {}".format(error)
        finally:
            print("Succesfull insert")



        db.commit()
        db.close()

    #remove entry from table books
    def Delete_books(id, name):
        #MariaDB configuration
        db = mariadb.connect(host= host, user= user, password= password,database= database)
        cursor = db.cursor()
        print(id)
        print(name)
        sql = "DELETE FROM books WHERE id='{}' AND name='{}'".format(id, name)
        print(sql)
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))
            errortext = "Error: {}".format(error)
        finally:
            print("Succesfull delete")

        db.commit()
        db.close()

    #select from books
    def Return_books():
        #MariaDB configuration
        db = mariadb.connect(host= host, user= user, password= password,database= database)
        cursor = db.cursor()
        sql="SELECT * FROM books"
        temp = ""
        try:
            cursor.execute(sql)
        except mariadb.Error as error:
            print("Error: {}".format(error))
            errortext = "Error: {}".format(error)
            return errortext
        finally:
            for id, name, author, jahr, volume, lang in cursor:
                temp += "\n" + "ID: {}, Name: {}, Author: {}, Jahr: {}, Volume: {}, Language: {}".format(id, name,author , jahr, volume, lang)
            return temp
        #Close connection"""
        db.close()
