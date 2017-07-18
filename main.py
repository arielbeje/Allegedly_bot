import discord
import asyncio
from random import randint

client = discord.Client()

token = ""

userIDs = []
roleIDs = []
roleNames = []

@client.event
async def on_message(message):
    allegedly = False
    
    if message.author.id in userIDs:
        allegedly = True
    
    for roleID in [role.id for role in message.author.roles]:
        if roleID in roleIDs:
            allegedly = True
            break
    
    for roleName in [role.name for role in message.author.roles]:
        if roleName in roleNames:
            allegedly = True
            break
    
    if allegedly:
        randomInt = randint(0, 99)
        if randomInt == 0:
            await client.send_message(message.channel, "*Allegedly...*")

@client.event
async def on_ready():
    print(client.user)
    print(client.user.id)
    print('-'*len(client.user.id))

client.run(token)
