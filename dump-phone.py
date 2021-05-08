#import 
import requests
import time
import sys
import os
from colorama import Fore
from banner_phone import *
#system
system_name = sys.platform
if system_name =='linux':
    os.system('clear')
else:
    os.system('cls')
#colors
yellow = Fore.YELLOW
white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED
fofo = Fore.MAGENTA
print(banner())
while True:

    try:
        #input
        n_tc = input(f"{Fore.WHITE}({Fore.LIGHTRED_EX}dump-phone{Fore.WHITE})>> ")
       
        number = n_tc.split()[0]
        code = n_tc.split()[1]
        #requests.get
        r = requests.get(f'http://146.148.112.105/caller/index.php/UserManagement/search_number?number={number}&country_code={code}')
        try:
            data = r.json()
            for i in data['result']:
                print(f"{white}[{green}*{white}] name :", i['name'])
                time.sleep(0.2)
                print(f"{white}[{green}*{white}] id : ", i['id'])
                time.sleep(0.2)
                print(f"{white}[{green}*{white}] number : ", i['number'])
                time.sleep(0.2)
                print(f"{white}[{green}*{white} country code :", i['country_code'])
        except:
            print(f"{white}[{red}*{white}] You have an error")
    except:
        print(f"< {yellow}number {white}> < {yellow}country code {white}>")
