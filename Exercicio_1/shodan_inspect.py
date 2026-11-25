import os
from pathlib import Path
from dotenv import load_dotenv
import shodan

# Inicializando variaveis de ambiente
_root = Path(__file__).resolve().parent.parent
load_dotenv(_root / ".env")

TARGET_URL = os.getenv("TARGET_URL")
TARGET_IP = os.getenv("TARGET_IP")
SHODAN_KEY = os.getenv("SHODAN_API_KEY")

def print_list(data, key, name):
    print(f"+ {name}:")
    for s in data.get(key, []):
        print(f"\t- {s}")


def analizar_alvo(target, is_ip = False):
    sho = shodan.Shodan(SHODAN_KEY)

    print("_"*40)
    print(" == Iniciando reconhecimento passivo do alvo ==")
    print(f"+ Alvo: {target}")

    info = sho.host(target) if is_ip else sho.dns.domain_info(target)
    
    print_list(info, "hostnames", "Hostnames")    
    print_list(info, "subdomains", "Subdominios")
    print_list(info, "ports", "Portas abertas")


def main():
    if not SHODAN_KEY:
        print(f"[ERRO] Variavel de ambiente 'SHODAN_API_KEY' não encontrada em '{_root.absolute}/.env'")
        return

    if not TARGET_IP and not TARGET_URL:
        print(f"[ERRO] Configure pelo menos uma das variaveis 'TARGET_IP' ou 'TARGET_URL' no arquivo de ambiente '{_root.absolute}/.env'")
        return
        
    if TARGET_URL:
        analizar_alvo(TARGET_URL)
    
    if TARGET_IP:
        analizar_alvo(TARGET_IP, is_ip=True)

if __name__ == "__main__":
    main()