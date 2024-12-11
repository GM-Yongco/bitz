# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: round_robin cpu scheduling algorithm
# HEADERS ================================================================

from helper import *

class RoundRobin(CPU):
	def simulation(self):

		# how may time slots each process gets each round
		BURST_ALLOCATION:int = 3

		self.all_processes = sorted(
			self.all_processes, 
			key=lambda x: x.ID
		)
	
		time:int = 0
		
		queue_processes:list = []
		current_process_index:int = 0
		removed_from_queue:bool = False
		shared_time_left:int = BURST_ALLOCATION
		
		all_processes_is_done:bool = False
		time_frame_is_available:bool = True
		
		while(all_processes_is_done == False):	

			all_processes_is_done = True
			time_frame_is_available = True
			
			# itterate through all the processes to see if the processes arent done yet
			# and to find one to maybe add to the process_queue
			for process in self.all_processes:
				if process.burst_completed < process.BURST:
					# if at least one process is not done... 
					all_processes_is_done = False
					
					# if process already arrived and is not in the queue process
					if not(process in queue_processes) and process.ARRIVAL <= time:
						queue_processes.append(process)
			
			# update the processes in queue_processes
			for process in queue_processes:
				process.time_turn_around += 1
				self.total_time_turn_around += 1
				if (process == queue_processes[current_process_index]):
					shared_time_left -= 1
					self.time_frames += str(process.ID) + '|'
					process.burst_completed += 1
					time_frame_is_available = False
					
					if process.burst_completed >= process.BURST:
						process.time_complete = time + 1
						shared_time_left = 0
					elif process.burst_completed == 1:
						process.time_start = time
				else:
					process.time_idle += 1
					self.total_time_idle +=1
			
			

			# if time slot is still available after itterating through all the processes
			# and theres still a process not done			
			if time_frame_is_available and (all_processes_is_done == False):
				self.time_frames += '=|'
	
			#update for next itteration
			
			#removed for queue process when finished
			
			if shared_time_left <= 0:
				if queue_processes[current_process_index].burst_completed >= queue_processes[current_process_index].BURST:
					queue_processes.remove(queue_processes[current_process_index])
				else:
					current_process_index += 1
					
				if len(queue_processes):
					current_process_index %= len(queue_processes)
				else:
					current_process_index = 0
					
				shared_time_left = BURST_ALLOCATION
			time += 1
			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	see_pee_you:RoundRobin = RoundRobin()
	see_pee_you.get_processes()
	see_pee_you.simulation()
	see_pee_you.output()

	section("END")
