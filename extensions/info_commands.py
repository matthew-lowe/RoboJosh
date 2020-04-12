import discord
from discord.ext import commands

class InfoCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(help="Get the avatar of a user", usage=";avatar [user]")
	async def avatar(self, ctx, target=None):
		utils = self.bot.get_cog("Utils")

		user = None
		if target is None:
			user = ctx.author
		else:
			try:
				user = self.bot.get_user(int(target.split("<@!")[1].split(">")[0]))
			except Exception:
				ctx.send("`Invalid user! Please tag a member`")
				return

		url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)

		embed = discord.Embed(title="Avatar URL", url=url, description=user.name + '#' + user.discriminator)
		embed.set_image(url=url)
		await utils.style_embed(embed, ctx)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(InfoCommands(bot))
