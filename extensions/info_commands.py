import datetime
import discord
from discord.ext import commands


class InfoCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Displays the avatar
	@commands.command(help="Show the avatar of a user", usage=";avatar [user]")
	async def avatar(self, ctx, target=None):
		utils = self.bot.get_cog("Utils")

		# Set the target user if given, else message author
		user = utils.get_target(ctx, target)

		if user is None:
			await ctx.send("`Invalid user! Please tag a member of the server`")
			return

		# URL Discord stores avatars in
		url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)

		# Send avatar as a swanky embed
		embed = discord.Embed(title="Avatar URL", url=url, description=user.name + '#' + user.discriminator)
		embed.set_image(url=url)
		utils.style_embed(embed, ctx)
		await ctx.send(embed=embed)

	# Gives some info about a user
	@commands.command(help="Get information about a user", usage=";info [user]")
	async def info(self, ctx, target=None):
		utils = self.bot.get_cog("Utils")

		# Set the target user if given, else message author
		user = utils.get_target(ctx, target)

		if user is None:
			await ctx.send("`Invalid user! Please tag a member of the server`")
			return
		
		member = ctx.guild.get_member(user.id)

		author_avatar = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.author)
		user_avatar = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)

		# Ommits the first value (@everyone)
		member_roles = member.roles[1:]

		role_string = ""
		for role in member_roles:
			role_string += f"<@&{role.id}> "

		embed = discord.Embed(title=f"{user.name}#{user.discriminator}")
		embed.add_field(name="User ID:", value=user.id, inline=True)
		embed.add_field(name="Display name:", value=member.display_name, inline=True)
		embed.add_field(name="Account Created:", value=user.created_at.strftime('%A %d %b %Y, %I:%M %p'), inline=False)
		embed.add_field(name="Guild Join Date:", value=member.joined_at.strftime('%A %d %b %Y, %I:%M %p'), inline=False)
		embed.add_field(name="Server Roles:", value=role_string, inline=False)
		embed.set_thumbnail(url=user_avatar)
		utils.style_embed(embed, ctx)

		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(InfoCommands(bot))
