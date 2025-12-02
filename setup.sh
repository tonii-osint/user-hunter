#!/bin/bash
echo -e "\e[34m[*] Iniciando el instalador de User Hunter...\e[0m"

if command -v apt-get &> /dev/null; then
    echo -e "\e[33m[*] Sistema basado en Debian/Ubuntu detectado.\e[0m"
    echo -e "\e[34m[*] Actualizando lista de paquetes...\e[0m"
    sudo apt-get update > /dev/null
    echo -e "\e[34m[*] Instalando Python 3 y pip si no están presentes...\e[0m"
    sudo apt-get install -y python3 python3-pip > /dev/null
elif command -v pacman &> /dev/null; then
    echo -e "\e[33m[*] Sistema basado en Arch/Manjaro detectado.\e[0m"
    echo -e "\e[34m[*] Instalando Python y pip si no están presentes...\e[0m"
    sudo pacman -S --needed --noconfirm python python-pip > /dev/null
else
    echo -e "\e[31m[!] Sistema de paquetes no soportado. Por favor, instala Python 3 y pip manualmente.\e[0m"
    exit 1
fi

echo -e "\e[34m[*] Instalando la librería 'requests' para Python...\e[0m"
pip3 install requests > /dev/null

if python3 -c "import requests" &> /dev/null; then
    echo -e "\e[32m[+] Instalación completada con éxito.\e[0m"
    echo -e "\e[32m[+] Ahora puedes ejecutar la herramienta con: python3 userhunter.py\e[0m"
else
    echo -e "\e[31m[!] Hubo un error al instalar las dependencias.\e[0m"
    exit 1
fi
