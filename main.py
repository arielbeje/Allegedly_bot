import discord
import asyncio
import time
from random import randint

client = discord.Client()

token = ""

YourID = ""

@client.event
async def on_message (message):
	if message.author. == YourID:
		int = randint(0, 99)
		if int = 0:
			await client.send_message(message.channel, "*Allegedly...*")

client.run(token, bot=False)