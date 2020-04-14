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

	# Load files in extensions folder
	for file in os.listdir("./extensions"):
		if file.endswith(".py") and file != "extension_utils.py":
			bot.load_extension("extensions." + file.split(".")[0])

	print("Loaded extensions!")


# Manage extensions from a command
# TODO: check with database to ensure random users can't unload extensions lol
@bot.command()
async def extensions(ctx, method, extension):
	try:
		if method == "load":
			bot.load_extension('extensions.' + extension)
			await ctx.send(f"Extension '{extension}' loaded!")
		elif method == "unload":
			bot.unload_extension('extensions.' + extension)
			await ctx.send(f"Extension '{extension}' unloaded!")
		elif method == "reload":
			bot.reload_extension('extensions.' + extension)
			await ctx.send(f"Extension '{extension}' reloaded!")
		else:
			await ctx.send("Unrecognised extension command!")
	except commands.errors.ExtensionNotFound:
		await ctx.send("Error caught (ExtensionNotFound)")
	except commands.errors.ExtensionNotLoaded:
		await ctx.send("Error caught (ExtensionNotLoaded)")

bot.run(open("token.txt", "r").read())
