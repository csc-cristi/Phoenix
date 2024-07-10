
import urllib.request
import json
import time
from colorama import init, Fore
import os

init()

class Data:
    def __init__(self, city, region, country, loc, postal, timezone):
        self.city = city
        self.region = region
        self.country = country
        self.loc = loc
        self.postal = postal
        self.timezone = timezone

def main():

    
    print(Fore.RED)
    print("   ▄███████▄    ▄█    █▄     ▄██████▄     ▄████████ ███▄▄▄▄    ▄█  ▀████    ▐████▀")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███    ███▌   ████▀  ")
    print("  ███    ███   ███    ███   ███    ███   ███    █▀  ███   ███ ███▌    ███  ▐███    ")
    print("  ███    ███  ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄     ███   ███ ███▌    ▀███▄███▀       Made by Baba》Yaga")
    print("▀█████████▀  ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███▀▀▀     ███   ███ ███▌    ████▀██▄     ")
    print("  ███          ███    ███   ███    ███   ███    █▄  ███   ███ ███    ▐███  ▀███    ")
    print("  ███          ███    ███   ███    ███   ███    ███ ███   ███ ███   ▄███     ███▄  ")
    print(" ▄████▀        ███    █▀     ▀██████▀    ██████████  ▀█   █▀  █▀   ████       ███▄   V0.0.5")
    print(" ")
    print(" ")
    print(f"{Fore.YELLOW}[{Fore.WHITE}1{Fore.YELLOW}] {Fore.RED}IP Tracking        {Fore.YELLOW}[{Fore.WHITE}2{Fore.YELLOW}] {Fore.RED} Comming Soon... ")
    print(" ")
    x = input("")
    print(" ")

    if x == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(Fore.GREEN)
        print("██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ")
        print("██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
        print("██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝  Made by Baba》Yaga")
        print("██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
        print("██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║")
        print("╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  V0.1.0")
        print(" ")
        print(f"{Fore.YELLOW}[{Fore.WHITE}0{Fore.YELLOW}] {Fore.RED}Back")
        print(" ")
        print(Fore.GREEN)
        ip = input("Enter IP: ")
        url = f"https://ipinfo.io/{ip}/json"
        
        

        try:
            with urllib.request.urlopen(url) as response:
                responseData = response.read().decode('utf-8')
                ipInfo = json.loads(responseData)

                os.system('cls' if os.name == 'nt' else 'clear')
                
                print("██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ")
                print("██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
                print("██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝")
                print("██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
                print("██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║")
                print("╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  V0.1.0")
                print(" ")
                time.sleep(2)
                print("[+] Request Successfully Made")
                print(" ")
                time.sleep(1)
                print("Loading [          ] 0%")
                time.sleep(1)
                print("Loading [#####     ] 50%")
                time.sleep(1)
                print("Loading [#######   ] 75%")
                time.sleep(1)
                print("Loading [##########] 100%")
                time.sleep(1)
                print(" ")
                time.sleep(2)
                print("[!] Data Found")

                ipData = Data(
                    city=ipInfo['city'],
                    region=ipInfo['region'],
                    country=ipInfo['country'],
                    loc=ipInfo['loc'],
                    postal=ipInfo['postal'],
                    timezone=ipInfo['timezone']
                )
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print("██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ")
                print("██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
                print("██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝")
                print("██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
                print("██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║")
                print("╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  V0.1.0")
                
                print(" ")
                print("   [!] Target info [!]   ")
                print(" ")
                print(f"Country: {ipData.country}")
                print(f"City: {ipData.city}")
                print(f"Coordinates: {ipData.loc}")
                print(f"Region: {ipData.region}")
                print(f"Timezone: {ipData.timezone}")
                print("")
                print("[?] Thank you for using :)")

                time.sleep(10)

        except Exception as ex:
            print(f"Error: {ex}")

    elif x == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Comming soon")


    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid option. Please choose between 1 and 2.")

if __name__ == "__main__":
    main()



