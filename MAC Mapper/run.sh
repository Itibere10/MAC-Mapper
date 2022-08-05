echo "=================================================================="
echo "Script de mapeamento e reconhecimento de endereços MAC"
read -p "Digite a faixa de IPs para a busca (Ex: 10.0.0.1/24): " IPS
#nmap -sP 10.0.0.1/24 | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " | MAC:  "$3;}' | sort
nmap -sP $IPS | awk '/Nmap scan report for/{ $5;}/MAC Address:/{print $3;}' | sort > macs.txt
python search.py
rm macs.txt