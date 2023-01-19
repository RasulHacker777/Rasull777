from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import pyfiglet

#Rasul_Hacker
import os
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
os.system("clear")
print(pyfiglet.figlet_format("RasulHacker777", justify="center", width=90))
string = input("String session: ")
os.system("clear")
print(pyfiglet.figlet_format("RasulHacker777", justify="center", width=90))

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.start()

async def main():

    async for message in client.iter_messages(777000):
        print(message.sender.username, message.text)
        print('\n\nCreator: @KayfuyD\n\n')
        break


with client:
    client.loop.run_until_complete(main())
