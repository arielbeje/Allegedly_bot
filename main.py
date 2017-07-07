import discord
import asyncio
from random import randint

client = discord.Client()

token = "" #To get a token,

YourID = "" #Get this id by using \@yourname and copying only the numbers

@client.event
async def on_message (message):
	if message.author. == YourID:
		int = randint(0, 99)
		if int = 0:
			await client.send_message(message.channel, "*Allegedly...*")

client.run(token, bot=False)