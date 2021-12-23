from houou.bot import HououClient
from houou.commands import HououCommands
import json

def main():
	# load config.json
	config = json.load(open('config.json'))
	token = config["token"]
	prefix = config["prefix"]

	# configure bot
	bot = HououClient(prefix)
	bot.add_cog(HououCommands(bot))

	bot.run(token)

if __name__ == "__main__":
	main()