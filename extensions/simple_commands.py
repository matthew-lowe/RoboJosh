import math
import discord
import datetime
from discord.ext import commands

class SimpleCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Display help message
	@commands.command(help="Help command, get commands", usage=";help [command]")
	async def help(self, ctx, req_command=None):
		utils = self.bot.get_cog("Utils")

		# If no specific command is chosen, show all commands
		if req_command is None:
			embed = discord.Embed(title="Help Menu")
			await utils.style_embed(embed, ctx)
			for command in self.bot.commands:
				embed.add_field(name=f"**`{command.usage}`**", value=command.help, inline=False)
			await ctx.send(embed=embed)
		# Else, show the specific command given
		else:
			for command in self.bot.commands:
				if command.name == req_command:
					embed = discord.Embed(title=f"Help for {command.name}")
					await utils.style_embed(embed, ctx)
					embed.add_field(value=f"{command.help}", name=f"**Usage:** `{command.usage}`")
					await ctx.send(embed=embed)
					return
			await ctx.send("```Unable to find command!```")

	# Returns ping in ms
	@commands.command(help="Tests bot activity and gets ping in ms", usage=";ping")
	async def ping(self, ctx):
		await ctx.send(f"Pong <@{ctx.author.id}>  (Took {math.trunc(self.bot.latency*1000)}ms)")

	# As the help message says, for testing purposes
	@commands.command(help="Useless commmand to make bot say something", usage=";say <message>")
	async def say(self, ctx, *args):
		message = ""
		for arg in args:
			message += arg + " "

		await ctx.send(message)


def setup(bot):
	bot.add_cog(SimpleCommands(bot))
