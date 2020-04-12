import discord
import json
import os
from discord.ext import commands

config = json.loads(open("config.json", "r").read())

bot = commands.Bot(command_prefix=config["prefix"], )

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user.name} successfully!")
	
	# Unregister pre-set help command. Probably better ways to do it, but this works
	bot.remove_command("help")

	for file in os.listdir("./extensions"):
		if file.endswith(".py") and file != "extension_utils.py":
			bot.load_extension("extensions." + file.split(".")[0])
	print("Loaded extensions!")

bot.run(open("token.txt", "r").read())
