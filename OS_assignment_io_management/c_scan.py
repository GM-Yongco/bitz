# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: lest recently used algorithm
# HEADERS ================================================================

from helper import *

class LRU_CPU(CPU):
	def simulation(self):
		current_pages:List[int] = []
		index_recency_list:List[int] = []
		for i in range(0, self.page_slots):
			current_pages.append(-1)			# -1 is a sentinel value
			index_recency_list.append(0)

		output:str = f"{'page_queue':12}"
		print(output)
	
		for new_page in self.page_queue:
			max_value = max(index_recency_list)		# its been in the list the longes without being updated
			LRU_index = index_recency_list.index(max_value)

			if new_page not in current_pages:
				current_pages[LRU_index] = new_page
			else:
				LRU_index = current_pages.index(new_page)
				
			for i in range(0, len(index_recency_list)):
				index_recency_list[i] += 1
			index_recency_list[LRU_index] = 0

			output = f"{new_page:5}"
			for current_page in current_pages:
				output += f"|{current_page:5}" 

			print(output)
		
			
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	test_cpu:LRU_CPU = LRU_CPU()
	test_cpu.json_to_details()
	test_cpu.simulation()

	section("END")
