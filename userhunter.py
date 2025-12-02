import requests
import sys
import signal
from os import system

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def signal_handler(sig, frame):
    print(f"\n{Colors.YELLOW}{Colors.BOLD}[*] Interrumpido por el usuario. Adiós!{Colors.RESET}")
    sys.exit(0)

def clear_screen():
    _ = system('clear')

def check_user(username, site_url):
    full_url = f"{site_url}{username}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(full_url, headers=headers, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            return True, full_url
        else:
            return False, full_url
    except requests.exceptions.RequestException:
        return False, full_url

def main():
    signal.signal(signal.SIGINT, signal_handler)

    clear_screen()
    
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
 _    _                     _   _             _            
| |  | |                   | | | |           | |           
| |  | |_   _  ___ _ __    | | | |_ __   ___ | | ___  _ __ 
| |  | | | | |/ _ \ '_ \   | | | | '_ \ / _ \| |/ _ \| '__|
| |__| | |_| |  __/ | | |  | |_| | | | | (_) | | (_) | |   
 \____/ \__,_|\___|_| |_|   \___/|_| |_|\___/|_|\___/|_|   
{Colors.RESET}{Colors.YELLOW}
                    User Hunter
                    Creado por: Tonii
{Colors.RESET}
"""
    print(banner)

    username = input(f"{Colors.BLUE}[?] Introduce el nombre de usuario a buscar: {Colors.RESET}")

    if not username:
        print(f"\n{Colors.RED}[!] No se ha introducido ningún nombre de usuario. Saliendo.{Colors.RESET}")
        sys.exit(1)

    print(f"\n{Colors.MAGENTA}[*] Buscando al usuario '{username}' en las webs configuradas...{Colors.RESET}\n")

    try:
        with open("sites.txt", "r") as f:
            sites = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Error: El archivo 'sites.txt' no se encuentra.{Colors.RESET}")
        sys.exit(1)

    found_count = 0

    for site in sites:
        found, url = check_user(username, site)
        if found:
            print(f"{Colors.GREEN}[+] ENCONTRADO: {url}{Colors.RESET}")
            found_count += 1
        else:
            print(f"{Colors.RED}[-] NO ENCONTRADO: {url}{Colors.RESET}")
    
    print(f"\n{Colors.CYAN}{Colors.BOLD}[*] Búsqueda finalizada. Se han encontrado {found_count} perfiles para el usuario '{username}'.{Colors.RESET}")

if __name__ == "__main__":

    main()
