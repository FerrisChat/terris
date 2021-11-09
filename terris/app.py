from colorama import init, Fore, Back, Style
import os
import ferris

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

print(Fore.RED, "Terris", Fore.RESET)
print(Back.RED, Fore.BLACK, "This is a secure connection to the FerrisChat Servers using the official 'ferriswheel' library.", Fore.RESET, Back.RESET)

email = input(f"{Fore.BLUE}Enter email > {Fore.RESET}")
password = input(f"{Fore.BLUE}Enter password > {Fore.RESET}")


guilds=None

client = ferris.Client()

async def guild_select(guilds):
    cls()
    print("test")
    init()
    print("test")
    for i in guilds:
        print(Back.RED, i, i.id, Back.RESET)
    print("test")
    guild = input(f"{Fore.BLUE}What guild would you like to attatch to? (Please enter the guild ID) > {Fore.RESET}")
    return (await client.fetch_guild(int(guild)))

@client.listen()
async def on_ready():
    print("Terris is ready")
    guilds = (await client.fetch_user(client.user.id)).guilds
    await guild_select(guilds)

try:
    client.run(email=email, password=password)
except ferris.errors.NotFound:
    print(f"{Fore.RED}Incorrect email.{Fore.RESET}")
except ferris.errors.Unauthorized:
    print(f"{Fore.RED}Incorrect password.{Fore.RESET}")
