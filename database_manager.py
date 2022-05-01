import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

master_password = os.getenv('MY_ENV_VAR')


def store_passwords(password, user_email, username, app_name, extra):
    conn = psycopg2.connect('dbname=suppliers user=liamwebster password=$master_password')
    cur = conn.cursor()
    postgres_insert_query = """ INSERT INTO passwords (PASSWORD,EMAIL,USERNAME,COMPANY, ETC) VALUES (%s, %s, %s, %s, %s)"""
    record_to_insert = (password, user_email, username, app_name, extra)
    cur.execute(postgres_insert_query, record_to_insert)
    conn.commit()
    cur.close()

def find_password(app_name):
    try:
        connection = psycopg2.connect('dbname=suppliers user=liamwebster password=$master_password')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT PASSWORD FROM passwords WHERE COMPANY = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ' + result[0])
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_username(app_name):
    try:
        connection = psycopg2.connect('dbname=suppliers user=liamwebster password=$master_password')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT USERNAME FROM passwords WHERE COMPANY = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        print('Username is: ' + result[0])
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_useremail(app_name):
    try: 
        connection = psycopg2.connect('dbname=suppliers user=liamwebster password=$master_password')
        cursor = connection.cursor()
        postgres_select_query = """ SELECT EMAIL FROM passwords WHERE COMPANY = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        print('Useremail is: ' + result[0])
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print(error)