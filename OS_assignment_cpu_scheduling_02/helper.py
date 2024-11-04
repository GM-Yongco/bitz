# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: classes to assist in cpu scheduling simulation
# HEADERS ================================================================

import io
import json
from pprint import pprint
from typing import List

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

class CpuProcess():
	burst_completed:int = 0
	
	time_start:int = 0
	time_complete:int = 0
	time_turn_around:int = 0
	time_idle:int = 0
	
	def __init__(
			self, 
			ID:int = -1,
			PRIORITY:int = -1,
			ARRIVAL:int = -1,
			BURST:int = -1,
		)->None:
		self.ID:int = ID
		self.PRIORITY:int = PRIORITY
		self.ARRIVAL:int = ARRIVAL
		self.BURST:int = BURST
	
class CPU():
	time_frames:str = ""
	all_processes:List[CpuProcess] = []
	complete:bool = False
	json_details = {}
	
	total_time_idle:int = 0
	total_time_turn_around:int = 0
	
	def __str__(self)->str:
		str_output:str = ""
		
		all_processes_len = len(self.all_processes)
		str_output += f"{'NUMBER OF PROCESSES':30}: {all_processes_len}" + "\n"
		str_output += f"{'AVERAGE TIME IDLE':30}: {self.total_time_idle / all_processes_len}" + "\n"
		str_output += f"{'AVERAGE TIME TURN-AROUND':30}: {self.total_time_turn_around / all_processes_len}" + "\n"
		
		# HEADER FOR ALL THE PROCESSES
		
		STRING_SIZE_1:int = 5
		STRING_SIZE_2:int = 10
		STRING_SIZE_3:int = 15
		STRING_SIZE_4:int = 20
		
		str_output += f"{'id':{STRING_SIZE_1}}" + "|"
		str_output += f"{'priority':{STRING_SIZE_2}}" + "|"
		str_output += f"{'time_arrival':{STRING_SIZE_3}}" + "|"
		str_output += f"{'time_burst':{STRING_SIZE_3}}" + "|"
		
		str_output += f"{'time_start':{STRING_SIZE_3}}" + "|"
		str_output += f"{'time_complete':{STRING_SIZE_3}}" + "|"
		str_output += f"{'time_turn_around':{STRING_SIZE_4}}" + "|"
		str_output += f"{'time_idle':{STRING_SIZE_3}}" + "|"
		
		str_output += f"{'burst_completed':{STRING_SIZE_2}}" + "|" + "\n"
		
		for process in self.all_processes:
			
			str_output += f"{process.ID:{STRING_SIZE_1}}" + "|"
			str_output += f"{process.PRIORITY:{STRING_SIZE_2}}" + "|"
			str_output += f"{process.ARRIVAL:{STRING_SIZE_3}}" + "|"
			str_output += f"{process.BURST:{STRING_SIZE_3}}" + "|"
			
			str_output += f"{process.time_start:{STRING_SIZE_3}}" + "|"
			str_output += f"{process.time_complete:{STRING_SIZE_3}}" + "|"
			str_output += f"{process.time_turn_around:{STRING_SIZE_4}}" + "|"
			str_output += f"{process.time_idle:{STRING_SIZE_3}}" + "|"
			
			str_output += f"{process.burst_completed:{STRING_SIZE_3}}" + "|" + "\n"
			
		return str_output
	
	# ========================================================================
	# CORE FUNCTIONALITY 
	# ========================================================================
	
	def json_read(self, path:str = "example_processes_01.json")->int:
		return_status = -1
		try:
			file:io.TextIOWrapper = open(path, "r")
			self.json_details = json.load(file)
			file.close()
			return_status = 200
		except Exception as e:
			print(e)
		return return_status
	
	def json_to_processes(self)->int:
		return_status = 200
		for process in self.json_details["processes"]:
			try:
				
				self.all_processes.append(CpuProcess(
					ID = process["id"],
					PRIORITY = process["priority"],
					ARRIVAL = process["time_arrival"],
					BURST = process["time_burst"]
				))
			except Exception as e:
				print(e)
				return_status = -1
		return return_status
	
	def get_processes(self):
		self.json_read()
		self.json_to_processes()
		
	def simulation(self):
		print("wow! such empty")
	
	def output(self)->None:
		print("=\t: no process/waiting")
		print("number\t: process with id of that number is using the cpu in that time slot")
		print('\n' + self.time_frames, self.__str__(), sep = "\n")
	
	
