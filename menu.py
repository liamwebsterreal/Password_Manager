import subprocess 
from database_manager import store_passwords, find_password, find_username, find_useremail
import bcrypt
import database_manager


def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find a username/password for a site or app')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

def create():
    print('Please proivide the name of the site or app you want to generate a password for')
    app_name = input()
    print('Please provide a simple password for this site: ')
    plaintext = input()
    salt = bcrypt.gensalt()
    passw = bcrypt.hashpw(plaintext.encode('utf-8'), salt)
    password = str(passw)
    write_to_clipboard(password)
    print(passw)
    print('-'*30)
    print('')
    print('Your password has now been created and copied to your clipboard')
    print('')
    print('-' *30)
    print('Please provide a user email for this app or site: ')
    user_email = input()
    print('Please provide a username for this app or site (if applicable): ')
    username = input()
    if username == None:
        username = ''
    print('Please provide any extra pertinant information')
    extra = input()
    if extra == None:
        extra == ''
    store_passwords(password, user_email, username, app_name, extra)

def find():
    print('Please provide site/app name')
    app_name = input()
    find_username(app_name)
    find_useremail(app_name)
    find_password(app_name)















