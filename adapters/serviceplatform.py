#!/usr/bin/python

import psycopg2
import requests

from flask import Flask, request, jsonify, render_template
import os, sys, logging, json, argparse 
from configparser import ConfigParser




class ServicePlatform:

    def __init__(self, name, host, type, username, password, project_name,service_token):
        self.name = name
        self.host = host
        self.type = type
        self.username = username
        self.password = password
        self.project_name = project_name
        self.service_token = service_token



    def getServicePlatformUser(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT username FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
            all = cursor.fetchall()
            return jsonify(all), 200     
        except (Exception, psycopg2.Error) as error :
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 


    def getServicePlatformPassword(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT password FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
            all = cursor.fetchall()
            return jsonify(all), 200     
        except (Exception, psycopg2.Error) as error :
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 


    def getServicePlatformToken(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT service_token FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
            all = cursor.fetchall()
            return jsonify(all), 200     
        except (Exception, psycopg2.Error) as error :
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 



    def getServicePlatflormType(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT type FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
            all = cursor.fetchall()
            return jsonify(all), 200     
        except (Exception, psycopg2.Error) as error :
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 



    def getServicePlatflorm(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT * FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
            all = cursor.fetchall()
            return jsonify(all), 200     
        except (Exception, psycopg2.Error) as error :
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")   

    def registerServicePlatform(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")            
            print (self.name)
            new_sp = "INSERT INTO service_platforms (name, host, type, username, password, project_name, service_token) VALUES (\'" +self.name+ "\',\'" +self.host+ "\',\'" +self.type+ "\',\'" +self.username+ "\',\'" +self.password+ "\',\'" +self.project_name+ "\',\'" +self.service_token+ "\')"
            print (new_sp)                    
            cursor.execute(new_sp)
            connection.commit()
            create_text = "New service platform registered"
            return jsonify(create_text), 200

        except (Exception, psycopg2.Error) as error :
            #print ("Error while connecting to PostgreSQL", error)
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")     



    def getServicePlatflormsByType(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT * FROM service_platforms WHERE type=\'" +self.type+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
            all = cursor.fetchall()
            return jsonify(all), 200     
        except (Exception, psycopg2.Error) as error :
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")  




    def getServicePlatforms(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()   
            print ( connection.get_dsn_parameters(),"\n")
            cursor.execute("SELECT * FROM service_platforms;")
            all = cursor.fetchall()
            return jsonify(all), 200
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")          