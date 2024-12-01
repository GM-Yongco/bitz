# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: first in first out page replacement algorithm
# HEADERS ================================================================

from helper import *

class FIFO_CPU(CPU):
	def simulation(self):
		current_pages:List[int] = []
		for i in range(0, self.page_slots):
			current_pages.append(-1)			# -1 is a sentinel value

		output:str = f"{'page_queue':12}"

		print(output)
		page_index_to_replace:int = 0
		for new_page in self.page_queue:
			if new_page not in current_pages:
				current_pages[page_index_to_replace] = new_page
				page_index_to_replace = (page_index_to_replace+1) % self.page_slots
			

			output:str = ""
			output += f"{new_page:5}"
			for current_page in current_pages:
				output += f"|{current_page:5}" 

			print(output)
		
			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	test_cpu:FIFO_CPU = FIFO_CPU()
	test_cpu.json_to_details()
	test_cpu.simulation()

	section("END")
