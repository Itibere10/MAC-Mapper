echo "================== Script de instalação de componentes =================="
echo "\n[CONFIGURE]: validando base de dados..."
arquivo=vendorMacs.xml
if test -f "$arquivo"; then
    echo "\n[CONFIGURE]: $arquivo localizado! Seguindo com o fluxo normal..."
else
    echo "\n[CONFIGURE]: $arquivo não localizado! Realizando o download do arquivo..."
    curl -o $arquivo https://devtools360.com/en/macaddress/vendorMacs.xml?download=true
fi
echo "\n[CONFIGURE]: Checando versões dos comandos nmap e pip..."
nmap | head -n 1
pip -V
echo "\n[CONFIGURE]: Instalando bibliotecas necessárias do python..."
pip install pandas
pip install numpy
pip install lxml
echo "[CONFIGURE]: Checando acesso direto ao python..."
python -c 'print("Print interno no python")'
echo "[CONFIGURE]: Script de configuração encerrada!"