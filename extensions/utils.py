import discord
from discord.ext import commands
import datetime


class Utils(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Adds embed footer, timestamp + color
	async def style_embed(self, embed, ctx):
		member = ctx.message.guild.get_member(ctx.author.id)
		embed.set_footer(text=f"Requested by {member.display_name}#{ctx.author.discriminator}",
						 icon_url=ctx.author.avatar_url_as(format='png'))
		embed.timestamp = datetime.datetime.utcnow()
		roles = member.roles
		color = roles[len(roles)-1].color
		embed.color = color


def setup(bot):
	bot.add_cog(Utils(bot))