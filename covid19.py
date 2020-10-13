#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys,requests

class cli_colors:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def sysout(output=''):
    sys.stdout.write(output + cli_colors.endc + '\n')

gouvbjpage = requests.get('http://www.gouv.bj/coronavirus/')
soup = BeautifulSoup(gouvbjpage.content,'html.parser')
a = soup.find_all('h2',{'class': ['h1 adapt white left-5']})

sysout(soup.find('title').text)
sysout()
sysout(cli_colors.fail + 'Cas confirmés\t:' + " " + a[0].text)
sysout(cli_colors.warning + 'Sous traitement\t:' + " " + a[1].text)
sysout(cli_colors.okgreen + 'Cas guéris\t:' + " " + a[2].text)
sysout(cli_colors.header + 'Décès\t:' + " " + a[3].text)
sysout()