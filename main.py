import discord
import asyncio
from random import randint

client = discord.Client()

token = ""

YourID = ""

@client.event
async def on_message (message):
	if message.author.id == YourID:
		randomID = randint(0, 99)
		if randomID == 0:
			await client.send_message(message.channel, "*Allegedly...*")

client.run(token)
