from discord.ext import commands
import discord

class HououClient(commands.Bot):
	async def on_ready(self):
		print('Houou Bot: Ready! {0}'.format(self.user))

#houou = commands.Bot(command_prefix)