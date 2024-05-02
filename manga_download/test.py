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

def download_url_img(file_path = r"./SCRAPED/scraped.jpg",
					 src = "https://v4.mkklcdnv6tempv2.com/img/tab_24/04/17/76/py993133/chapter_73_both_in_sickness/1-o.jpg"
					 ) -> None:
	urlretrieve(src, file_path)

# ========================================================================
# MAIN 
# ========================================================================

def main():
	download_url_img(src = "https://2.bp.blogspot.com/drive-storage/AJQWtBP75IWBEnv60A_RJWEQylU2sZXjNKIkU5lPzqWsnxRsRmuK4vc-LPBIyAKnNHMizTtNPdanj6WZHJdKXBZzeviZMWOLtGWgMyce7MmRj98QFBo=w700")


if __name__ == '__main__':
	section("START")
	main()
	section("END")