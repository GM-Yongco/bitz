# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: classes to assist in disk scheduling simulation
# HEADERS ================================================================

import io
import json
from typing import List

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)
	
class DISK():
	position_queue:List[int] = []
	position_previous:int
	position_current:int
	track_size:int
	seek_rate:int
	alpha_value:int

	simulated_position_order:List[int] = []
	
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
		json_details:dict = self.json_read(path)

		self.position_queue = json_details["position_queue"]
		self.position_previous = json_details["position_previous"]
		self.position_current = json_details["position_current"]
		self.track_size = json_details["track_size"]
		self.seek_rate = json_details["seek_rate"]
		self.alpha_value = json_details["alpha_value"]

	def display_disk(self) -> None:
		for entry in self.simulated_position_order:
			padding_right:int = self.track_size - entry - len(str(entry))
			print(f"|{'-'*entry}{entry}{'-'*padding_right}|")
	
	def display_head_movement(self) -> None:
		self.simulated_position_order.pop(0)
		
		print("total head movement:")
		total_head_movement:int = 0
		for i in range(len(self.simulated_position_order)-1):
			head_movement:int = abs(self.simulated_position_order[i] - self.simulated_position_order[i+1])
			total_head_movement += head_movement

			out_str:str = f"|{self.simulated_position_order[i]} - {self.simulated_position_order[i+1]}|"
			print(f"{out_str:12} = {head_movement}")
		print(f"{'total head movement':20} : {total_head_movement}")
		print(f"{'seek time':20} : {total_head_movement * self.seek_rate}")

	def display_simulation(self) -> None:
		self.display_disk()
		self.display_head_movement()


	def simulation(self):
		print("wow! such empty")
	
# ========================================================================
# TESTING 
# ========================================================================

if __name__ == '__main__':
	section("START")

	test_disk:DISK = DISK()
	test_disk.json_to_details()



	print(test_disk.position_queue)
	print(f"{'position_previous':20} : {test_disk.position_previous}")
	print(f"{'position_current':20} : {test_disk.position_current}")
	print(f"{'track_size':20} : {test_disk.track_size}")
	print(f"{'seek_rate':20} : {test_disk.seek_rate}")

	section("ANSWER")

	print(test_disk.simulated_position_order)
	test_disk.simulated_position_order.insert(0, test_disk.position_current)
	test_disk.simulated_position_order.insert(0, test_disk.position_previous)
	test_disk.simulated_position_order += test_disk.position_queue
	print(test_disk.simulated_position_order)

	test_disk.display_simulation()

	section("END")

