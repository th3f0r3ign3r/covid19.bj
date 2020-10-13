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

gouvbjpage = requests.get('http://www.gouv.bj/coronavirus/')
soup = BeautifulSoup(gouvbjpage.content,'html.parser')
a = soup.find_all('h2',{'class': ['h1 adapt white alt','h1 adapt white']})
x = "<h2 class='h1 adapt white'>"
y = "<h2 class='h1 adapt white alt>"
z = '</h2>'

def extractN(z,y1,y2,y3):
    return z.replace(y1,'').replace(y2,'').replace(y3,'')

def sysout(output=''):
    sys.stdout.write(output + '\n')

cas = []

for i in a:
    bn = str(i)
    cas.append(extractN(bn,x,y,z))

sysout('\n')
sysout(cli_colors.fail + 'Cas confirmés\t:' + cas[0])
sysout(cli_colors.warning + 'Sous traitement\t:' + cas[1])
sysout(cli_colors.fail + 'Cas guéris\t:' + cas[2])
sysout(cli_colors.fail + 'Décès\t:' + cas[3])