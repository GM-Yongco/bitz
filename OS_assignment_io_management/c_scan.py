# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: first in first out disk scheduling simulation
# HEADERS ================================================================

from helper import *

class CScan(DISK):
	def display_simulation(self) -> None:
		self.display_disk()
		self.display_head_movement()

	def display_head_movement(self) -> None:
		self.simulated_position_order.pop(0)
		
		print("total head movement:")
		total_head_movement:int = 0

		if self.simulated_position_order[0] < self.simulated_position_order[1]: # if the head is going right
			# current to end
			head_movement:int = abs(self.simulated_position_order[0] - (self.track_size - 1))
			total_head_movement += head_movement
			out_str:str = f"|{self.simulated_position_order[0]} - {self.track_size - 1}|"
			print(f"{out_str:12} = {head_movement}")

			# end to current
			head_movement:int = abs(0 - (self.simulated_position_order[-1]))
			total_head_movement += head_movement
			out_str:str = f"|{0} - {self.simulated_position_order[-1]}|"
			print(f"{out_str:12} = {head_movement}")

		else:
			# current to end
			head_movement:int = abs(0 - self.simulated_position_order[0])
			total_head_movement += head_movement
			out_str:str = f"|{0} - {self.simulated_position_order[0]}|"
			print(f"{out_str:12} = {head_movement}")

			# end to current
			head_movement:int = abs(399 - (self.simulated_position_order[-1]))
			total_head_movement += head_movement
			out_str:str = f"|{399} - {self.simulated_position_order[-1]}|"
			print(f"{out_str:12} = {head_movement}")

		total_head_movement += self.alpha_value
		print(f"{'alpha value':12} = {self.alpha_value}")

		print(f"{'total head movement':20} : {total_head_movement}")
		print(f"{'seek time':20} : {total_head_movement * self.seek_rate}")

	def simulation(self):

		lower_than_current = [num for num in self.position_queue if num < self.position_current]
		bigger_than_current = [num for num in self.position_queue if num >= self.position_current]

		if self.position_current > self.position_previous: # if the head is spinning to the "right"
			bigger_than_current.append(self.track_size-1)
			lower_than_current.append(0)
			bigger_than_current.sort()
			lower_than_current.sort()

			self.simulated_position_order += bigger_than_current + lower_than_current
		else:
			bigger_than_current.append(self.track_size-1)
			lower_than_current.append(0)
			bigger_than_current.sort(reverse=True)
			lower_than_current.sort(reverse=True)

			self.simulated_position_order += lower_than_current + bigger_than_current



		self.simulated_position_order.insert(0,self.position_current)
		self.simulated_position_order.insert(0, self.position_previous)

			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	test_disk:CScan = CScan()
	test_disk.json_to_details()
	test_disk.simulation()
	test_disk.display_simulation()

	section("END")
