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
channel=None

client = ferris.Client()

async def guild_select(guilds):
    cls()
    init()
    for i in guilds:
        print(Back.RED, i, i.id, Back.RESET)
    guild = input(f"{Fore.BLUE}What guild would you like to attatch to? (Please enter the guild ID) > {Fore.RESET}")
    return (await client.fetch_guild(int(guild), fetch_channels=True)).channels

async def channel_select(channels):
    cls()
    init()
    for i in channels:
        print(Back.RED, i, i.id, Back.RESET)
    channel2 = input(f"{Fore.BLUE}What channel would you like to attatch to? (Please enter the channel ID) > {Fore.RESET}")
    channel: int = int(channel2)
    return channel


@client.listen()
async def on_ready():
    print("Terris is ready")
    guilds = (await client.fetch_user(client.user.id)).guilds

    e = await guild_select(guilds)
    await channel_select(e)

client.run(email=email, password=password)

