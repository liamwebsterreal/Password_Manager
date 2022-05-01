import psycopg2
import os
from menu import menu, create, find
from dotenv import load_dotenv

load_dotenv()

master_password = os.getenv('MY_ENV_VAR')

passw = input('Please provide the master password to start using ppManager3000: ')

if passw == master_password:
    print('You\'re in')

else:
    print('no luck')
    exit()

choice = menu()
while choice != 'q':
    if choice == '1':
        create()
    if choice == '2':
        find()
    choice = menu()
exit()
