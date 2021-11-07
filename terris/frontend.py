from colorama import init, Fore, Back, Style
import os
import ferris

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

init()

print(Fore.RED, "Terris", Fore.RESET)
print(Back.RED, Fore.BLACK, "This is a secure connection to the FerrisChat Servers using the official 'ferriswheel' library.", Fore.RESET, Back.RESET)

email = input(f"{Fore.BLUE}What is you email > {Fore.RESET}")
password = input(f"{Fore.BLUE}What is you password > {Fore.RESET}")


client = ferris.Client()

client.run(email=email, password=password)


