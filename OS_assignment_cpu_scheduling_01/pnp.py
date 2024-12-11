# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: priority non-preemptive cpu scheduling algorithm
# HEADERS ================================================================

from helper import *

class PriorityNonPreemptiveCPU(CPU):
	def simulation(self):
		time:int = 0
		
		self.all_processes = sorted(
			self.all_processes, 
			key=lambda x: x.ID
		)
		self.all_processes = sorted(
			self.all_processes, 
			key=lambda x: x.ARRIVAL
		)
		self.all_processes = sorted(
			self.all_processes, 
			key=lambda x: x.PRIORITY
		)
		# we should expect the lowest priority to be first
		# jsut need to itterate through the arrival times to see if they eligible
		# and if theres still processes with the same priority and arrival, ID will be the decider

		# stores the last line to copy it to the next for the gant chart
		last_line:str = ""
		all_processes_complete:bool = False
		time:int = 0
		while (all_processes_complete == False):
			
			# if all processes are done, it will stay true
			all_processes_complete:bool = True
			something_was_executed:bool = False

			# adds the last line to the current line
			new_slots:str = last_line
			
			# looks for an eligible process
			for current_process in self.all_processes:
				# processes the eligible process 
				# if the porcess hasnt been completed yet
				if (current_process.BURST == current_process.burst_completed):
					continue

				all_processes_complete = False

				# if the process is within the arrival time window
				if(current_process.ARRIVAL > time):
					continue
				
				something_was_executed = True

				# execution of the valid process
				
				current_process.burst_completed += current_process.BURST
				current_process.time_start = time
				current_process.time_idle = time - current_process.ARRIVAL

				time += current_process.BURST

				current_process.time_complete = time
				current_process.time_turn_around = current_process.time_complete - current_process.ARRIVAL 
			
				self.total_time_idle += current_process.time_idle
				self.total_time_turn_around += current_process.time_turn_around

				new_slots += f"{str(current_process.ID)}" * current_process.BURST
				last_line = new_slots
				self.time_frames += new_slots + "\n"

				break
			
			# if nothing was executed, then idle time only if all processes arent complete
			if all_processes_complete == False:
				if something_was_executed == False:
					time += 1

					new_slots += "="
					last_line = new_slots
					self.time_frames += new_slots + "\n"
			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	see_pee_you:PriorityNonPreemptiveCPU = PriorityNonPreemptiveCPU()
	see_pee_you.get_processes()
	see_pee_you.simulation()
	see_pee_you.output()

	section("END")
