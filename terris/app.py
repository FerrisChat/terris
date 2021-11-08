from colorama import init, Fore, Back, Style
import os
import ferris

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

print(Fore.RED, "Terris", Fore.RESET)
print(Back.RED, Fore.BLACK, "This is a secure connection to the FerrisChat Servers using the official 'ferriswheel' library.", Fore.RESET, Back.RESET)

email = input(f"{Fore.BLUE}What is you email > {Fore.RESET}")
password = input(f"{Fore.BLUE}What is you password > {Fore.RESET}")


guilds=None

client = ferris.Client()

def guild_select(guilds):
    cls()
    print("test")
    init()
    print("test")
    for i in guilds:
        print("test")
        print(f"{Back.RED}{i.name}{i.guild_id}{Back.RESET}")
    print("test")
    guild = input(Fore.BLUE, "What guild would you like to attatch to? (Please enter the guild ID) > ", Fore.RESET)
    return client.fetch_guild(int(guild))

@client.listen()
async def on_ready():
    print("Terris is ready")
    g = await client.create_guild(name="Test Guild")
    c = await g.create_channel(name="Test Channel")
    guilds = (await client.fetch_user(client.user.id)).guilds
    guild_select(guilds)

client.run(email=email, password=password)

