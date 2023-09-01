import socket
import threading
import colorama
import os
import time
from colorama import Fore

colorama.init()

m = Fore.MAGENTA
w = Fore.WHITE
black = Fore.LIGHTBLACK_EX
y = Fore.LIGHTYELLOW_EX
r = Fore.LIGHTRED_EX
g = Fore.GREEN
lb = Fore.LIGHTBLUE_EX

os.system("@mode con cols=90 lines=40")
os.system("cls")
os.system(f"title ^>^>^> Wallah ^| Clownerna2023 ^<^<^<")
gui = f"""
        {r}╔═════════════════════════════════════════════════════════════════╗
        {r}║             [!] Clownerna hälsar [!]                       {r}║
        {r}║                                                            {r}║
        {r}║                  [&] farmoronlyfans[&]                     {r}║
        {r}╚═════════════════════════════════════════════════════════════════╝
"""

print(gui)

def tcpping(ip):
    try:
        
        port = 80

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"{m}[{w}OK{m}] {g}Connection to {y}{ip}:{port} {lb}[{y}CLOWNERNA2023{lb}] {m}[{w}OK{m}]")
    except:
        print(f"{m}[{w}CLOWN{m}] {r}Oops något gick fel {y}{ip} {r}Är nere {lb}[{y}Skickar bytes{lb}]")

def main():
    try:
        ip = input(f"{m}[{w}>>>{m}] {black}IP:{y} ")
        print("")

        while True:
            os.system(f"title - CLOWNERNA2023 ^|  ^| Pingar {ip}:80 -")
            tcpping(ip)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"{m}\n\n[{w}CLOWN{m}] {w}Stänger ner.")
        time.sleep(1)

if __name__ == "__main__":
    main()
