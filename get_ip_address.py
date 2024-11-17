# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================

import socket
import requests

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================



# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	ip_local:str = ":DDD"
	ip_public:str = ":DDD"
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	try:
		s.connect(("8.8.8.8", 80))
		ip_local = s.getsockname()[0]
	finally:
		s.close()
	try:
		ip_public = requests.get("https://api.ipify.org").text
	except Exception as e:
		ip_public = e 


	print(f"Local\tIP address: {ip_local}")
	print(f"Public\tIP address: {ip_public}")
	section("END")


