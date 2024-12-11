# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: first come first served cpu scheduling algorithm
# HEADERS ================================================================

from helper import *

class FirstComeFirstServedCPU(CPU):
	def simulation(self):
		time:int = 0
		
		out_of_bounds_process_index = len(self.all_processes)
		current_process_index:int = 0
		
		# sort by arrival time then secondarily sort by process ID
		self.all_processes = sorted(
			self.all_processes, 
			key=lambda x: x.ID
		)
		self.all_processes = sorted(
			self.all_processes, 
			key=lambda x: x.ARRIVAL
		)
		
		last_line:str = ""
		for current_process in self.all_processes:
			
			new_slots:str = last_line
			
			if current_process.ARRIVAL > time:
				new_slots += '=' * (current_process.ARRIVAL - time)
				time += current_process.ARRIVAL - time
			
			current_process.time_start = time
			current_process.time_idle = time - current_process.ARRIVAL
			
			new_slots += f"{str(current_process.ID)}" * current_process.BURST
			current_process.burst_completed += current_process.BURST
			time += current_process.BURST
			
			current_process.time_complete = time
			current_process.time_turn_around = current_process.time_complete - current_process.ARRIVAL 
			
			self.total_time_idle += current_process.time_idle
			self.total_time_turn_around += current_process.time_turn_around
			
			last_line = new_slots
			self.time_frames += new_slots + "\n"
			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	see_pee_you:FirstComeFirstServedCPU = FirstComeFirstServedCPU()
	see_pee_you.get_processes()
	see_pee_you.simulation()
	see_pee_you.output()

	section("END")
