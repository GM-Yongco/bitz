# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: classes to assist in cpu scheduling simulation
# HEADERS ================================================================

import io
import json
from collections import deque
from typing import List

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)
	
class CPU():
	page_queue:List[int] = []
	page_slots:int = -1
	
	# ========================================================================
	# CORE FUNCTIONALITY 
	# ========================================================================
	
	def json_read(self, path:str = "example_processes.json")->dict:
		json_details:dict = {"error":"error"}
		try:
			file:io.TextIOWrapper = open(path, "r")
			json_details = json.load(file)
			file.close()
		except Exception as e:
			print(e)
		return json_details
	
	def json_to_details(self, path:str = "example_processes.json")->None:
		json_details = self.json_read(path)

		self.page_queue = json_details["page_queue"]
		self.page_slots = json_details["page_slots"]
		
	def simulation(self):
		print("wow! such empty")
	
# ========================================================================
# TESTING 
# ========================================================================

if __name__ == '__main__':
	section("START")

	test_cpu:CPU = CPU()
	test_cpu.json_to_details()

	print(test_cpu.page_queue)
	print(test_cpu.page_slots)

	section("END")

