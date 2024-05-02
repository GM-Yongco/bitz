# Description		: Code that will impress u ;)
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# HEADERS ================================================================

from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def get_html(url = "https://chihuahuaspin.com/") -> str:
	request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
	page = urlopen(request_site)

	html = (page.read().decode(("utf-8")))
	html = (str)(html.encode('utf-8'))

	return html

def write(test_output, file_path = r"./SCRAPED/test.txt") -> None:
	the_file = open(file_path, "w")
	the_file.write(str(test_output))
	the_file.close

# ========================================================================
# MAIN 
# ========================================================================

def main():
	chapter:int = 0
	url:str = f"https://manhuascan.io/manga/36090-the-guy-she-was-interested-in-wasnt-a-guy-at-all/chapter-{str(chapter)}"

	html = get_html(url)
	html = bs(html, "html.parser")

	image_tags = html.find_all("img")
	img = image_tags[1]
	print(f"image number {len(image_tags)}")

	for images in image_tags:
		print(f"{images}\n\n")



if __name__ == '__main__':
	section("START")
	main()
	section("END")