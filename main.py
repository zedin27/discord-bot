import discord
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv() # Loads the local .env file

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event # ADD: Random quotes if a keyword is sad or depressing
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'): # Change behavior
		await message.channel.send('Hello!')

client.run(os.getenv("TOKEN"))