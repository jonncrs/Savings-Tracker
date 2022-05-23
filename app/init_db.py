from sqlite3 import connect
from webbrowser import get
import mysql.connector
import json
import os

try:
    print('\n ESTABLISHING CONNECTIONS')
    # to connect to xampp/local server
    _db = mysql.connector.connect(host="localhost", user="root", password="")
    print(' CONNECTED TO SERVER\n')
    print(' RUNNING SERVER\n')

    Q = _db.cursor()

    #Q.execute("drop database userdata") # to drop database : only use if necessary

    db_exists = False # db exist boolean
    print(" LOCATING DATABASE")
    Q.execute('SHOW DATABASES')
    # to check if db exists
    for exist_db in Q:
        if str(exist_db) == "('userdata',)":
            # if exist
                print(" DATABASE LOCATED")
                db_exists = True
    # if db not exist
    if db_exists == False: # !UPDATE ALWAYS SET TO FALSE
        try:
            # to create new db
            print("\n ERROR: NO INITIAL DATABASE FOUND\n")
            print(" SYTEM WILL NOW IMPLEMENT CREATION OF DATABASE\n")
            print(" CREATING NEW DATABASE")
            Q.execute('CREATE DATABASE IF NOT EXISTS userdata') # to run query
            Q.execute('USE userdata') # to set db
            # to create table fields using json
            try:
                to_file = os.getcwd() + "\\app\\" # to get current directory and set path to app folder
                print(" LOCATING DATABASE CONFIGURATIONS")
                with open(to_file + "db_fields.json", "r") as open_tables: # to open json file
                    print(" APPLYING DATABASE CONFIGURATIONS\n")
                    get_table = json.load(open_tables)
                    for x_table in get_table:
                        # to execute user_login query from json : this insert username, password, email
                        _user_login = x_table['user_login']
                        try:
                            Q_user_login = f"CREATE TABLE user_login (id INT AUTO_INCREMENT PRIMARY KEY, {_user_login['username']} TEXT, {_user_login['password']} TEXT, {_user_login['email']} TEXT)"
                            Q.execute(Q_user_login) # to run query
                            print(" ADDED USER LOGIN FIELDS")
                        except:
                            # to display query if error
                            print("\n QUERY NOT RECOGNIZED")
                            print(" " + Q_user_login)
                        # to execute user_profile query from json : this insert username, password, email
                        _user_profile = x_table['user_profile']
                        try:
                            Q_user_profile = f"CREATE TABLE user_profile (id INT AUTO_INCREMENT PRIMARY KEY, {_user_profile['fname']} TEXT, {_user_profile['mi']} TEXT, {_user_profile['lname']} TEXT, {_user_profile['age']} NUMERIC, {_user_profile['birthday']} TEXT)"
                            Q.execute(Q_user_profile) # to run query
                            print(" ADDED USER PROFILE FIELDS")
                        except:
                            # to display query if error
                            print("\n QUERY NOT RECOGNIZED")
                            print(" " + Q_user_login)
                        # to execute bank_acc query from json : this insert email, cash_type, cash_bal
                        _bank_acc = x_table['bank_acc']
                        try:
                            Q__bank_acc = f"CREATE TABLE bank_acc (id INT AUTO_INCREMENT PRIMARY KEY, {_bank_acc['email']} TEXT, {_bank_acc['cash_type']} TEXT, {_bank_acc['cash_bal']} NUMERIC)"
                            Q.execute(Q__bank_acc) # to run query
                            print(" ADDED BANK ACCOUNT FIELDS")
                        except:
                            # to display query if error
                            print("\n QUERY NOT RECOGNIZED")
                            print(" " + Q__bank_acc)
                        # to execute logs query from json : this insert email, cash_type, cash_bal
                        _logs = x_table['logs']
                        try:
                            Q_logs = f"CREATE TABLE logs (id INT AUTO_INCREMENT PRIMARY KEY, {_logs['email']} TEXT, {_logs['cash_in']} NUMERIC, {_logs['cash_out']} NUMERIC, {_logs['cash_type']} TEXT, {_logs['cash_type_before_bal']} NUMERIC, {_logs['cash_type_after_bal']} NUMERIC, {_logs['total_funds_before']} NUMERIC,{_logs['total_funds_after']} NUMERIC, {_logs['date']} TEXT, {_logs['time']} TEXT, {_logs['note']} TEXT)"
                            Q.execute(Q_logs) # to run query
                            print(" ADDED LOGS FIELDS")
                        except:
                            # to display query if error
                            print("\n QUERY NOT RECOGNIZED")
                            print(" " + Q_logs)
                print("\n DATABASE CREATED")
            except:
                print("")
                for x in range (0, 5):
                    print(" UNEXPECTED ERROR OCCURED. PLEASE CHECK IF db_fields.json EXIST IN APP FOLDER.")
        except:
            print("\n UNEXPECTED ERROR OCCURED. PLEASE CHECK SYSTEM CONFIGURATIONS.")

    # to run app
    print("\n RUNNING APPLICATION")

except:
    print("")
    for x in range (0, 5):
        print(' ERROR: SERVER CONNECTION FAILED. PLEASE CHECK IF XAMPP IS RUNNING PROPERLY.')