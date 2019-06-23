import datetime
from requests import get

def fetch_public_ip():
    return get('https://api.ipify.org').text.strip()

def print_diary():
    return

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
    print('\n\nContent:\n{}'.format(content))