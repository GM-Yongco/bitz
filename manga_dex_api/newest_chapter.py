# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: compares old chapter IDs with the new chapter ID
# HEADERS ================================================================
import requests
import json

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def get_general_info(manga_title:str = "The Guy She Was Interested in Wasn't a Guy at All"):
	base_url = "https://api.mangadex.org"

	response:json = requests.get(
		url = f"{base_url}/manga",
		params={"title": manga_title}
	).json()

	with open("get_general_info.txt", "w", encoding="utf-8") as f:
		json.dump(response, f, indent=4, ensure_ascii=False)

	return response


def latest_chapter(manga_title:str = "The Guy She Was Interested in Wasn't a Guy at All"):
	response:json = get_general_info(manga_title)

	return f"https://mangadex.org/chapter/{response['data'][0]['attributes']['latestUploadedChapter']}"


def get_chapters(manga_title:str = "The Guy She Was Interested in Wasn't a Guy at All"):
	base_url = "https://api.mangadex.org"

	manga_id = get_general_info(manga_title=manga_title)['data'][0]['id']

	response:json = requests.get(
		url = f"{base_url}/manga/{manga_id}/feed"
	).json()

	if response['result'] == "ok":
		response =  response["data"]
		response = [item for item in response if item['attributes']['translatedLanguage'] == 'en']

	with open("get_chapters_response.txt", "w", encoding="utf-8") as f:
		json.dump(response, f, indent=4, ensure_ascii=False)

	return None


# ========================================================================
# MAIN 	
# ========================================================================

if __name__ == '__main__':
	section("START")

	get_chapters("The Green Yuri")

	section("END")