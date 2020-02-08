#Import libs
import os
import time
import sys
import requests
import ctypes
import mysql.connector
import requests
from colorama import Fore,init
import smtplib
import argparse
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import requests, os, nmap, ipwhois, socket
import dns.resolver
from pprint import pprint
from time import sleep

#Connect to the databse
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jai123",
    database="vulkaweb"
)
mycursor = mydb.cursor()
#Colors for text
blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
magenta = Fore.MAGENTA
cyan = Fore.CYAN
white = Fore.WHITE
black = Fore.BLACK
yellow = Fore.YELLOW
try:
    response = urlopen('https://mcpilot.no').getcode()
    if response == 200:
        server = f'[{green}Connected{white}]'
                
except URLError as err:
    server = f'[{red}Disconnected{white}]'

except HTTPError as err:
    server = f'[{red}Disconnected{white}]'

#Extra variables
yourversion = '1'
bs = ('                                    ')

#UI for the program
ui = (f'''
              ██╗   ██╗██╗   ██╗██╗     ██╗  ██╗ █████╗ ██╗    ██╗███████╗██████╗ 
              ██║   ██║██║   ██║██║     ██║ ██╔╝██╔══██╗██║    ██║██╔════╝██╔══██╗
              ██║   ██║██║   ██║██║     █████╔╝ ███████║██║ █╗ ██║█████╗  ██████╔╝
              ╚██╗ ██╔╝██║   ██║██║     ██╔═██╗ ██╔══██║██║███╗██║██╔══╝  ██╔══██╗
               ╚████╔╝ ╚██████╔╝███████╗██║  ██╗██║  ██║╚███╔███╔╝███████╗██████╔╝
                ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚═════╝ 
                                                                                  
                    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗    ██╗   ██╗  ██╗        
                    ████╗ ████║██╔════╝████╗  ██║██║   ██║    ██║   ██║ ███║        
                    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    ██║   ██║ ╚██║        
                    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ╚██╗ ██╔╝  ██║        
                    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝     ╚████╔╝██╗██║        
                    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝       ╚═══╝ ╚═╝╚═╝
                    Server Status >>> {server}''')

def main():
    ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Main Screen | V.' + yourversion)
    os.system('cls')
    print(ui)
    print()
    print(bs + f'╔══════════════════════╗')
    print(bs + f'║ [{cyan}1{white}] Login            ║')
    print(bs + f'║ [{cyan}2{white}] Register         ║')
    print(bs + f'║ [{cyan}3{white}] Updates          ║')
    print(bs + f'║ [{cyan}4{white}] Join Discord     ║')
    print(bs + f'║ [{cyan}5{white}] Credits          ║')
    print(bs + f'║                      ║')
    print(bs + f'║ [{red}E{white}] Exit             ║')
    print(bs + f'╚══════════════════════╝')
    main_input = input(bs + f'VulkaWeb | Choose >>> ')

    if main_input == '1':
        login()

    elif main_input == '2':
        register()

    elif main_input == '3':
        update()

    elif main_input == '4':
        discord()

    elif main_input == '5':
        credit()

    elif main_input == 'E' or main_input == 'e':
        sys.exit()
        
    else:
        print()
        print(bs + f'[{red}!{white}] Invalid Command.')
        time.sleep(1.5)
        main()

#Needs more wokr
def login():
    username = ""
    password = ""
    ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Login Screen | V.' + yourversion)
    os.system('cls')
    print(ui)
    print()
    print(bs + f'╔══════════════════════╗')
    print(bs + f'║ [Your username]      ║')
    print(bs + f'╚══════════════════════╝')
    username = input(bs + f'VulkaWeb | Username >>> ')
    print()
    print(bs + f'╔══════════════════════╗')
    print(bs + f'║ [Your password]      ║')
    print(bs + f'╚══════════════════════╝')
    password = input(bs + f'VulkaWeb | Password >>> ')
    sql = f"SELECT * FROM userdb WHERE user = '{username}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if not username in myresult:
        os.system('cls')
        print(ui)
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ [Wrong username]     ║')
        print(bs + f'╚══════════════════════╝')
        time.sleep(2)
        login()

    if username in myresult and password in myresult:
        os.system('cls')
        print(ui)
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ Loggin Into The Menu ║')
        print(bs + f'╚══════════════════════╝')
        time.sleep(1.5)
        main_menu()
    else:
        os.system('cls')
        print(ui)
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ [Wrong password]     ║')
        print(bs + f'╚══════════════════════╝')
        time.sleep(2)
        login()
#Not working correct
def register():
    ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Register Screen | V.' + yourversion)
    os.system('cls')
    print(ui)
    print()
    print(bs + f'╔══════════════════════╗')
    print(bs + f'║ [Enter a username]   ║')
    print(bs + f'╚══════════════════════╝')
    username = input(bs + f'VulkaWeb | Username >>> ')
    user_check = f"SELECT * FROM userdb WHERE username = '{username}'"
    if user_check in username:
        print(bs + f'[{red}!{white}] Username Exist.')
        time.sleep(2)
        register()
    else:
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ [Enter a password]   ║')
        print(bs + f'╚══════════════════════╝')
        password = input(bs + f'VulkaWeb | Password >>> ')
        os.system('cls')
        print(ui)
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ [Enter an email]     ║')
        print(bs + f'╚══════════════════════╝')
        email = input(bs + f'VulkaWeb | Email >>> ')
        if user_check in email:
            print(bs + f'[{red}!{white}] Email Exist.')
            time.sleep(2)
            register()
        else:
            print()
            print(bs + f'╔══════════════════════╗')
            print(bs + f'║ [Enter the token]    ║')
            print(bs + f'╚══════════════════════╝')
            token = input(bs + f'VulkaWeb | Token >>> ')
            token_check = f"SELECT * FROM userdb WHERE token = '{token}'"
            if not token in token_check:
                print(bs + f'[{red}!{white}] Invalid Token.')
                time.sleep(2)
                register()
            if token in token_check:
                print(token_check)
                update_token_profile = f"UPDATE userdb SET user = '{username}', password = '{password}', email = '{email}' WHERE token = '{token}'"
                mycursor.execute(update_token_profile)
                mydb.commit()
                os.system('cls')
                print(ui)
                print()
                print(bs + f'╔══════════════════════╗')
                print(bs + f'║ [{green}Registration Done{white}]  ║')
                print(bs + f'╚══════════════════════╝')
                time.sleep(2)
                main()
            else:
                print(bs + f'[{red}!{white}] Invalid Token.')
                time.sleep(2)
                register()
def main_menu():
    ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Main Menu Screen | V.' + yourversion)
    os.system('cls')
    print(ui)
    print()
    print(bs + f'╔══════════════════════╗')
    print(bs + f'║ [{cyan}1{white}] Panel Finder     ║')
    print(bs + f'║ [{cyan}2{white}] Temp Email       ║')
    print(bs + f'║ [{cyan}3{white}] LFI Tester       ║')
    print(bs + f'║ [{cyan}4{white}] Site Tester      ║')
    print(bs + f'║ [{cyan}5{white}] Sniffer          ║')
    print(bs + f'║ [{cyan}6{white}] Text To Hash     ║')
    print(bs + f'║ [{cyan}7{white}] Wifi Scan        ║')
    print(bs + f'║ [{cyan}8{white}] XorCrypt         ║')
    print(bs + f'║ [{cyan}9{white}] XssTester        ║')
    print(bs + f'║                      ║')
    print(bs + f'║ [{red}E{white}] Exit             ║')
    print(bs + f'╚══════════════════════╝')
    main_menu_input = input(bs + f'VulkaWeb | Choose >>> ')

    if main_menu_input == '1':
        panel_finder()

    elif main_menu_input == '2':
        bulkbomber()

    elif main_menu_input == '3':
        emailbomber()

    elif main_menu_input == '6':
        sitetester()

print('Whois')
print('Site Checker')
print('Port Scan')
print('Nmap Scaner')
print('Server Information (Headers)')
print('Nameservers of domain')
print('CMS detector')
print('Exit')


def sitetester():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Site Tester Screen | V.' + yourversion)
    print(ui)
    print()
    print(bs + f'╔══════════════════════╗')
    print(bs + f'║ [{cyan}1{white}] Whois            ║')
    print(bs + f'║ [{cyan}2{white}] Site Checker     ║')
    print(bs + f'║ [{cyan}3{white}] Port Scan        ║')
    print(bs + f'║ [{cyan}4{white}] Nmap Scan        ║')
    print(bs + f'║ [{cyan}5{white}] Server Info      ║')
    print(bs + f'║ [{cyan}6{white}] Nameservers      ║')
    print(bs + f'║ [{cyan}7{white}] CMS Detector     ║')
    print(bs + f'║                      ║')
    print(bs + f'║ [{cyan}E{white}] Exit             ║')
    print(bs + f'╚══════════════════════╝')
    num = input(bs + f'VulkaWeb | Choose >>> ')

    if num == '1':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Whois Search | V.' + yourversion)
        print(ui)
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ Enter target IP      ║')
        print(bs + f'╚══════════════════════╝')
        ip = input(bs + f'VulkaWeb | IP >>> ')
        resault = ipwhois.IPWhois(ip).lookup_whois()
        print(resault)
        input(bs + f'VulkaWeb | Press any key to exit >>> ')
        sitetester()

    elif num == '2':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Site checker | V.' + yourversion)
        print(ui)
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ Enter target domain  ║')
        print(bs + f'╚══════════════════════╝')
        addr = input(bs + f'VulkaWeb | Domain >>> ')
        try:
            response = urlopen('https://' + addr).getcode()
            if response == 200:
                print()
                print(bs + f'╔══════════════════════╗')
                print(bs + f'║ [{green}Site is up{white}]         ║')
                print(bs + f'╚══════════════════════╝')
                time.sleep(4)
                sitetester()
                
        except URLError as err:
            print()
            print(bs + f'╔══════════════════════╗')
            print(bs + f'║ [{red}Site is down{white}]║')
            print(bs + f'╚══════════════════════╝')
            print(bs + f'VulkaWeb | Reason >>> ', err.reason)
            time.sleep(4)

        except HTTPError as err:
            print()
            print(bs + f'╔══════════════════════╗')
            print(bs + f"║ [{red}Couldn't check Target{white}]║")
            print(bs + f'╚══════════════════════╝')
            print(bs + f'VulkaWeb | Reason >>> ', err.code)
            time.sleep(4)
        sitetester()

    elif num == '3':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Site checker | V.' + yourversion)
        print(ui)
        print()
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ Enter target ip      ║')
        print(bs + f'╚══════════════════════╝')
        site_ip = input(bs + f'VulkaWeb | IP >>> ')

        try:
            print()
            print(bs + f'╔══════════════════════╗')
            print(bs + f'║ Open ports           ║')
            print(bs + f'╚══════════════════════╝')
            for port in range(20, 500):  # you can change this range
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn = sock.connect_ex((site_ip, port))
                if conn == 0:
                    print(bs + 'VulkanWeb | Port: {}       Open'.format(port))
                    sock.close()

        except KeyboardInterrupt:
            print(bs + f'VulkaWeb | Stopping Scanning.. >>> ')
            sitetester()
        sitetester()

    elif num == '4':
        target_ip = input('\033[36mEnter target ip: \033[0m')
        res = nmap.PortScanner().scan(target_ip, "20-160")  # range ip
        print(res)
        sitetester()

    elif num == '5':
        server = input("\033[36mEnter target address: \033[0m")
        headers = requests.get(server).headers
        print("Some information...")
        sleep(2)

        for key, value in headers.items():  # headers is a dict so we can use items() function to get it as Key, Value
            print(key + "\t\t\t \033[91m ==> \033[0m " + value)
        sitetester()

    elif num == '6':
        dom = input("\033[36mEnter target address (like example.com): \033[0m")
        ans = dns.resolver.query(dom, 'NS')
        for server in ans:
            print(server)
        sitetester()

    elif num == '7':
        site = input("\033[36mEnter target address: \033[0m")

        # Wordpress Scan
        print("")
        print("Scan for Wordpress...")
        sleep(2)
        wpLcheck = requests.get(site + "/wp-login.php")
        if wpLcheck.status_code == 200 and "user_login" in wpLcheck.text and "404" not in wpLcheck.text:
            print("Wordpress detected: admin login => " + site + "/wp-admin.php")
        else:
            pass

        wpAcheck = requests.get(site + "/wp-admin")
        if wpAcheck.status_code == 200 and "user_login" in wpAcheck.text and "404" not in wpAcheck.text:
            print("Wordpress detected: admin page => " + site + "/wp-admin")
        else:
            pass

        # Joomla Scan
        print("")
        print("Scan for Joomla...")
        sleep(2)
        jmAcheck = requests.get(site + "/administrator")
        if jmAcheck.status_code == 200 and "mod-login-username" in jmAcheck.text and "404" not in jmAcheck.text:
            print("Joomla detected: administrator page => " + site + "/administrator")
        else:
            pass

        jmScheck = requests.get(site)
        if jmScheck.status_code == 200 and "joomla" in jmScheck.text and "404" not in jmScheck:
            print("Joomla detected: 'joomla' on index")
        else:
            pass

        # Drupal Scan
        print("")
        print("Scan for Drupal...")
        sleep(2)
        drRcheck = requests.get(site + "/readme.txt")
        if drRcheck.status_code == 200 and 'drupal' in drRcheck.text and '404' not in drRcheck.text:
            print("Drupal detected: Drupal Readme.txt => " + site + '/readme.txt')
        else:
            pass

        drCcheck = requests.get(site + '/core/COPYRIGHT.txt')
        if drCcheck.status_code == 200 and 'Drupal' in drCcheck.text and '404' not in drCcheck.text:
            print("Drupal detected: Drupal COPYRIGHT.txt => " + site + '/core/COPYRIGHT.txt')
        else:
            pass

        # Magento Scan
        print("")
        print("Scan for Magento...")
        sleep(2)
        mgRcheck = requests.get(site + '/RELEASE_NOTES.txt')
        if mgRcheck.status_code == 200 and 'magento' in mgRcheck.text:
            print("Magento detected: Magento Release_Notes.txt: " + site + '/RELEASE_NOTES.txt')
        else:
            pass

        mgCcheck = requests.get(site + '/js/mage/cookies.js')
        if mgCcheck.status_code == 200 and "404" not in mgCcheck.text:
            print("Magento detected: Magento cookies.js: " + site + '/js/mage/cookies.js')
        else:
            pass
        sitetester()


    elif num == '8':
        exit()
    else:
        print("\033[91mWrong choise!!!\033[0m")
        sitetester()        



def emailbomber():
    # Argument setup
    parser = argparse.ArgumentParser(description="Email bomber")
    parser.add_argument("-f", "--sender", type=str, help="Email address for mail to be sent from ONLY SUPPORTS GMAIL")
    parser.add_argument("-p", "--passwd", type=str, help="Password for the sender email account")
    parser.add_argument("-t", "--to", type=str, help="Target email")
    parser.add_argument("-s", "--subject", type=str, help="Subject of email")
    parser.add_argument("-m", "--message", type=str, help="Message body")
    parser.add_argument("-n", "--times", type=int, help="Times to send the email")
    args = parser.parse_args()

    # Send the emails
    if not args.sender or not args.passwd or not args.to:
        print("Fields not specified")
        exit()
    else:
        subject = "Email Bomb"
        msg = "From the python email bomber with <3"
        times = 1000
        if args.subject:
            subject = args.subject
        elif args.message:
            msg = args.message
        elif args.times:
            times = args.times
        sendMail(args.sender, args.passwd, args.to, subject, msg, times)
        


def panel_finder():
    ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Panel Finder Screen | V.' + yourversion)
    os.system('cls')
    print(ui)
    print()
    print(bs + f'╔══════════════════════╗')
    print(bs + f'║ Enter targeted URL   ║')
    print(bs + f'╚══════════════════════╝')
    urls = input(bs + "VulkaWeb | URL >>> ")  # Get target url from user
    url = 'http://' + urls
    start = (bs + "Scanning..\n")
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        sleep(0.1)
    file = open("panels.txt", "r")  # Open files containing possible admin directories
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print(bs + "Panel found >>> {}".format(curl))
            else:
                print(bs + "\033[91mPanel not found >>> {} \033[0m".format(curl))
    except KeyboardInterrupt:
        print(bs + "\033[91mShutdown Request! \033[0m")
    except:
        print(bs + "\033[91mUnknown Error! \033[0m")
    file.close()


def update():
    ctypes.windll.kernel32.SetConsoleTitleW('VulkaWeb Menu | Update Screen | V.' + yourversion)
    os.system('cls')
    print(ui)
    print()
    gitversion = requests.get(url="https://raw.githubusercontent.com/scorpion3013/minecraft-account-recovery-tool/master/stuff/version.txt").content.decode().replace("\n","")
    if gitversion != yourversion:
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ [{red}Outdated Version{white}]   ║')
        print(bs + f'║                      ║')
        print(bs + f'║ Your version: [{yellow}{yourversion}{white}]    ║')
        print(bs + f'║ Latest version: [{green}{gitversion}{white}]  ║')
        print(bs + f'║                      ║')
        print(bs + f'║ [{yellow}U{white}] Update           ║')
        print(bs + f'║ [{red}B{white}] Back             ║')
        print(bs + f'╚══════════════════════╝')
        update_input = input(bs + f'VulkaWeb | Choose >>> ')

        if update_input == 'U' or update_input == 'u':
            print()
            print(bs + f'https://raw.githubusercontent.com/scorpion3013/minecraft-account-recovery-tool/master/stuff/version.txt')
            update_link_input = input(bs + f'VulkaWeb | >>> ')
            main()

        elif update_input == 'B' or update_input == 'b':
            main()

        else:
            print()
            print(bs + f'[{red}!{white}] Invalid Command.')
            time.sleep(1.5)
            update()

    else:
        print(bs + f'╔══════════════════════╗')
        print(bs + f'║ [{green}Updated Version{white}]    ║')
        print(bs + f'║                      ║')
        print(bs + f'║ Your version: [{green}{yourversion}{white}]    ║')
        print(bs + f'║ Latest version: [{green}{gitversion}{white}]  ║')
        print(bs + f'║                      ║')
        print(bs + f'║ [{red}B{white}] Back             ║')
        print(bs + f'╚══════════════════════╝')
        update_input = input(bs + f'VulkaWeb | Choose >>> ')

        if update_input == 'B' or update_input == 'b':
            main()

        else:
            print()
            print(bs + f'[{red}!{white}] Invalid Command.')
            time.sleep(1.5)
            update()
main()


