#!/bin/bash

echo 'Baixando python...'

sudo apt update
sudo apt install python3

clear
echo 'Python instalado'
echo 'Executando Calculadora'
echo ''

python3 /home/igor/modulo1/python/calculadora.py