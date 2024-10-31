# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: compares old chapter IDs with the new chapter ID
# HEADERS ================================================================
import requests

# discord
import discord
import discord.ext.commands
from discord.ext import commands

import io
import json
import time

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def discord_mention(message:str = "generic response")->None:
	# read file channel
	path:str = "REFERENCES/bot_info.json"
	try:
		file:io.TextIOWrapper = open(path, "r")
		json_details:dict = json.load(file)
		file.close()
		print(f"function : get_references success")
	except Exception as e:
		print(f"function : get_references failed")
		print(e)

	# turning bot on just to send a message
	bot:discord.ext.commands.bot.Bot = commands.Bot(command_prefix = "", intents=discord.Intents.all())
	
	@bot.event
	async def on_ready():
		print(f"{bot.user} is now connected")

		channel:discord.TextChannel = bot.get_channel(int(json_details["log_channel_id"]))
		user:discord.User = bot.get_user(int(json_details["user_ids"]["Veee"]))
		await channel.send(f"{user.mention} {message}")
		print("message has been sent")	
		
		await bot.close()
		print("bot has been closed")

	bot.run(json_details["bot_tokens"]["Vessel"])

def manga_dex_latest_chapter(manga_title:str = "The Guy She Was Interested in Wasn't a Guy at All"):
	base_url = "https://api.mangadex.org"

	response:json = requests.get(
		url = f"{base_url}/manga",
		params={"title": manga_title}
	).json()

	return response['data'][0]['attributes']['latestUploadedChapter']

# ========================================================================
# MAIN 	
# ========================================================================

if __name__ == '__main__':
	section("START")

	while(True):
		section("CHECKING OLD CHAPTER")
		chapter_id:str = str(manga_dex_latest_chapter())

		textFile_path_1 = "./REFERENCES/manga_chapter_id.txt"
		with open(textFile_path_1, 'r') as file:
			old_chapter_id:str = str(file.read())

		section("DISCORD UPDATE")
		if chapter_id == old_chapter_id:
			discord_mention("no new chapters")
		else:
			with open(textFile_path_1, 'w') as file:
				file.write(chapter_id)
		
		time.sleep(10)

	section("END")