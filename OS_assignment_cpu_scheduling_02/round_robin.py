# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: round_robin cpu scheduling algorithm
# HEADERS ================================================================

from helper import *

class ShortestJobFirstCPU(CPU):
	def simulation(self):

		# how may time slots each process gets each round
		BURST_ALLOCATION:int = 2 

		self.all_processes = sorted(
			self.all_processes, 
			key=lambda x: x.ID
		)
	
		time:int = 0
		all_processes_is_done:bool = False
		queue_processes:list = []
		
		while(all_processes_is_done == False):	

			all_processes_is_done = True
			time_frame_is_available:bool = True
			
			# itterate through all the processes to find one to use a time slot
			for process in self.all_processes:
				if process.burst_completed < process.BURST:
					# if at least one process is not done... 
					all_processes_is_done = False
					
					
					if process.ARRIVAL <= time:
						for i in range(BURST_ALLOCATION):	
							process.time_turn_around += 1
							self.total_time_turn_around += 1
							
							if time_frame_is_available:					
								self.time_frames += str(process.ID) + '|'
								process.burst_completed += 1
								time_frame_is_available = False
								
								if process.burst_completed == process.BURST:
									process.time_complete = time
								elif process.burst_completed == 1:
									process.time_start = time
							else:
								process.time_idle += 1
								self.total_time_idle +=1

			# if time slot is still available after itterating through all the processes
			# and theres still a process not done			
			if (not queue_processes) and (all_processes_is_done == False):
				self.time_frames += '=|'
	
			time += 1
			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	see_pee_you:ShortestJobFirstCPU = ShortestJobFirstCPU()
	see_pee_you.get_processes()
	see_pee_you.simulation()
	see_pee_you.output()

	section("END")
