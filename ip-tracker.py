import requests
import sys

BANNER = """
 ██▓███ ▄▄▄█████▓ ██▀███ ▄▄▄ ▄████▄ ██ ▄█▀▓█████ ██▀███
▓██░ ██▒▓ ██▒ ▓▒ ▓██ ▒ ██▒▒████▄ ▒██▀ ▀█ ██▄█▒ ▓█ ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒ ▓██░ ▒░ ▓██ ░▄█ ▒▒██ ▀█▄ ▒▓█ ▄ ▓███▄░ ▒███ ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██▀▀█▄ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█ ▄ ▒██▀▀█▄
▒██▒ ░ ░ ▒██▒ ░ ░██▓ ▒██▒ ▓█ ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
[ Criado por graziellycarolini94-gif ]
"""

def track(ip):
    url = f"http://ip-api.com/json/{ip}"
    r = requests.get(url).json()
    if r['status'] == 'fail':
        print(f"[!] IP invalido: {ip}")
        return
    print(f"""
[✓] LOCALIZACAO ENCONTRADA

IP: {r['query']}
Pais: {r['country']} ({r['countryCode']})
Estado: {r['regionName']}
Cidade: {r['city']}
CEP: {r['zip']}
Provedor: {r['isp']}
Org: {r['org']}
Lat/Long: {r['lat']}, {r['lon']}
Mapa: https://www.google.com/maps?q={r['lat']},{r['lon']}

    """)

print(BANNER)
if len(sys.argv) < 2:
    print("Uso: python ip-tracker.py 8.8.8.8")
else:
    track(sys.argv[1])
