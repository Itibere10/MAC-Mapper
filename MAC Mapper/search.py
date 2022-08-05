import pandas as pd
import numpy as np
print('\n')
print('================== Script Python ==================')
df = pd.read_xml('vendorMacs.xml')
print('\n> Dataset carregado!')
with open("macs.txt", "r") as f:
    macscan = f.readlines()
macscan = [i.replace('\n','') for i in macscan]
print('\n> Endereços MAC dos dispositivos locais obtidos!')
print(macscan)
for i in range(len(macscan)):
    macscan[i] = macscan[i][:8]
print('\n> Prefixos MAC obtidos!')
print(macscan)
print('\n> Mapeando prefixos dos endereços MAC com a base de dados... \n')
match = df[pd.DataFrame(df.mac_prefix.tolist()).isin(macscan).any(1).values]
match = match.reset_index(drop=True)
match.columns = ['Prefixo MAC', 'Empresa']
faltantes = list(set(macscan)-set(match['Prefixo MAC']))
print(match)
print('\nPrefixos MAC não descobertos: ')
for i in faltantes:
    print(i)
print('\n\nScript Python encerrado!')