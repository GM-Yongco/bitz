# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================

import io
import json
from pprint import pprint
from typing import List

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS HELPER
# ========================================================================

def json_read(path:str = "example_processes_02.json") -> dict:
	json_details:dict = {"error":"error"}
	try:
		file:io.TextIOWrapper = open(path, "r")
		json_details = json.load(file)
		file.close()
	except Exception as e:
		print(e)

	return json_details

# ========================================================================
# FUNCTIONS CORE
# ========================================================================

def gant_chart_cpu(processes_data:dict = {}):
	all_processes = processes_data["processes"]
	all_processes = sorted(all_processes, key=lambda x: x["time_arrival"])

	time_slot:int = 0
	current_process:int = 0
	current_process_time_burst:int = 0
	process_ammount = len(all_processes)

	total_time_idle:int = 0
	total_time_turn_around:int = 0

	print(f"{"CPU:":25}", end = "")
	while(True):
		if(current_process >= process_ammount):
			break
		if(all_processes[current_process]["time_arrival"] <= time_slot):
			current_process_time_burst = all_processes[current_process]["time_burst"]

			print("[", end = "")
			print("-" * current_process_time_burst, end = "")
			print("]", end = "")
			
			all_processes[current_process]["time_start"] = time_slot
			all_processes[current_process]["time_idle"] = time_slot - all_processes[current_process]["time_arrival"]
			time_slot += current_process_time_burst
			all_processes[current_process]["time_complete"] = time_slot
			all_processes[current_process]["time_turn_around"] = all_processes[current_process]["time_complete"] - all_processes[current_process]["time_start"]
			
			total_time_idle += all_processes[current_process]["time_idle"]
			total_time_turn_around += all_processes[current_process]["time_turn_around"]

			current_process += 1
		else:
			print("-", end = "")
			time_slot += 1
	print("")

	processes_data["time_end"] = time_slot
	processes_data["total_time_idle"] = total_time_idle
	processes_data["average_time_idle"] = total_time_idle/process_ammount
	processes_data["total_time_turn_around"] = total_time_turn_around
	processes_data["average_time_turn_around"] = time_slot/process_ammount

def gant_chart_arrival_time(processes_data:dict = {}):

	all_processes = processes_data["processes"]
	process_ammount:int = len(all_processes)

	print(f"{"START TIME PROCESS ID:":25}", end="")

	proccess_display:str = "-" * (processes_data["time_end"] + (2*process_ammount))
	char_list:list = list(proccess_display)
	for index, process in enumerate(all_processes):
		char_list[process["time_start"] + (index*2)] = str(process["id"])
	proccess_display = "".join(char_list)

	print(proccess_display)

def processes_properties(processes_data:dict = {}):
	all_processes = processes_data["processes"]

	print(f"{"id":5}|{"priority":10}|{"time_arrival":15}|{"time_burst":15}|{"time_complete":15}|{"time_start":15}|{"time_idle":15}|{"time_turn_around":20}")
	for process in all_processes:
		print(f"{process["id"]:5}|{process["priority"]:10}|{process["time_arrival"]:15}|{process["time_burst"]:15}|{process["time_complete"]:15}|{process["time_start"]:15}|{process["time_idle"]:15}|{process["time_turn_around"]:20}")
	
	print("\n")
	print(F"{"AVERAGE TIME IDLE":30}: {processes_data["average_time_idle"]}")
	print(F"{"AVERAGE TIME TURN-AROUND":30}: {processes_data["average_time_turn_around"]}")


# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	processes_data:list = json_read()

	gant_chart_cpu(processes_data)
	gant_chart_arrival_time(processes_data)
	processes_properties(processes_data)
	
	section("RAW DATA")
	pprint(processes_data)

	section("END")