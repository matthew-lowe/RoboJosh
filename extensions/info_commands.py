import discord
from discord.ext import commands

class InfoCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Displays the avatar
	@commands.command(help="Get the avatar of a user", usage=";avatar [user]")
	async def avatar(self, ctx, target=None):
		utils = self.bot.get_cog("Utils")

		# Set the target user if given, else message author
		user = None
		if target is None:
			user = ctx.author
		else:
			try:
				user = self.bot.get_user(int(target.split("<@!")[1].split(">")[0]))
			except Exception:
				ctx.send("`Invalid user! Please tag a member`")
				return

		# URL Discord stores avatars in
		url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)

		# Send avatar as a swanky embed
		embed = discord.Embed(title="Avatar URL", url=url, description=user.name + '#' + user.discriminator)
		embed.set_image(url=url)
		await utils.style_embed(embed, ctx)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(InfoCommands(bot))
