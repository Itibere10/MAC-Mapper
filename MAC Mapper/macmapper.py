import pandas as pd
import numpy as np
import nmap
import os
import requests
import lxml
import re
import subprocess
print('\n')
print('================== Script Python ==================')

#Checando a existência do arquivo vendorMacs.xml
nm = nmap.PortScanner()
if not os.path.exists('vendorMacs.xml'):
    print('\n> Arquivo vendorMacs.xml não encontrado localmente! Realizando o Download...')
    response = requests.get("https://devtools360.com/en/macaddress/vendorMacs.xml?download=true")
    open("vendorMacs.xml", "wb").write(response.content)
df = pd.read_xml('vendorMacs.xml')
print('\n> Dataset vendorMacs.xml carregado!')

#Checando a margem de IPs
modo = input('\n> Selecione o modo: \n[1]> IP de rede pública (Automático)\n[2]> Margem de IPs privados (Manual)\n')
if int(modo) == 1:
    ip = requests.get('https://ifconfig.me/ip').text
    print('\n> IP público da rede:',ip)
    #content = str(os.system("nmap -O "+ip))
    content = subprocess.getoutput("nmap -sP "+ip)
else:
    if int(modo) == 2:
        ip = input('\n> Digite a margem de IPs: ')
        #content = str(os.system("nmap -O "+ip))
        content = subprocess.getoutput("nmap -sP "+ip)

print('\n> Realizando as análises dos endereços MAC obtidos...')

regex = r"(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})"
matches = re.findall(regex, content, re.MULTILINE)

print('\n> Endereços MAC dos dispositivos locais obtidos:')
print(matches)

prefixes = matches
for i in range(len(prefixes)):
    prefixes[i] = prefixes[i][:8]
print('\n> Prefixos MAC obtidos!')
print(prefixes)

print('\n> Mapeando prefixos dos endereços MAC com a base de dados...\n')
finded = df[pd.DataFrame(df.mac_prefix.tolist()).isin(prefixes).any(1).values]
finded = finded.reset_index(drop=True)
finded.columns = ['Prefixo MAC', 'Empresa']
notfound = list(set(prefixes)-set(finded['Prefixo MAC']))
print('>>> OUTPUT:')
print("\n",finded)
print('\nPrefixos MAC não descobertos: ')
for i in range(len(notfound)):
    print(i+1,'   ',notfound[i])
print('\n> Script Python encerrado!')
