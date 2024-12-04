# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: first in first out disk scheduling simulation
# HEADERS ================================================================

from helper import *

class FIFO(DISK):
	def simulation(self):
		self.simulated_position_order.insert(0, self.position_current)
		self.simulated_position_order.insert(0, self.position_previous)
		self.simulated_position_order += self.position_queue
		
			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	test_disk:FIFO = FIFO()
	test_disk.json_to_details()
	test_disk.simulation()
	test_disk.display_simulation()

	section("END")
