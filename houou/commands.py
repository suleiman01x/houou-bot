from discord.ext import commands
import discord
from .naga import Naga
from selenium.common.exceptions import *
import os

class HououCommands(commands.Cog, name='Basic Houou Commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="naga")
	async def naga(self, ctx, *args):
		message = await ctx.send("処理中...")
		try:
			# scrape javascript data from naga
			naga_url = args[0]
			naga = Naga(naga_url)

		except IndexError:
			await ctx.send('使い方:\n	{0}naga [url]'.format(self.bot.command_prefix))
			return
		except JavascriptException:
			await ctx.send('{0}は適切なURLではありません'.format(args[0]))
			return
		except InvalidArgumentException:
			await ctx.send('{0}は適切なURLではありません'.format(args[0]))
			return
		
		print("Houou bot: website scraped...")

		# send organized javascript data as file
		file_name = "{0}.txt".format(ctx.message.id)
		with open(file_name, "w") as file:
			file.write(naga.organize())
		
		with open(file_name, "rb") as file:
			await ctx.send(file=discord.File(file))
			await message.delete()
		
		os.remove(file_name)