import datetime
from requests import get
import sqlite3

def fetch_public_ip():
    return get('https://api.ipify.org').text.strip()

def print_diary():
    return

def write_to_datastore(timestamp, content):
    db = sqlite3.connect('datastore.db')
    db.cursor().execute('INSERT INTO CONTENT VALUES(\'{}\',\'{}\')'.format(timestamp, content))
    db.commit()
    print('\nDB Write Success. See you tomorrow :)\n')

if __name__ == "__main__":
    timestamp = str(datetime.datetime.now().date())
    systemip = fetch_public_ip()
    print('[+] Today is {}\n[+] Your Public IP: {}\n[+] Enter today\'s content (Enter 0 to stop and 1 to view your diary)\n'.format(timestamp, systemip))
    content = ''
    while True:
        line = input('>>> ')
        if line=='0':
            exit()
        elif line=='1':
            print_diary()
            exit()
        else:
            content+=str(line).strip()+'\n'
    write_to_datastore(timestamp, content)