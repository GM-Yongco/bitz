# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: lest recently used algorithm
# HEADERS ================================================================

from helper import *

class LRU_CPU(CPU):
	def simulation(self):
		current_pages:List[int] = []
		for i in range(0, self.page_slots):
			current_pages.append(-1)			# -1 is a sentinel value

		output:str = f"{'page_queue':12}"
		print(output)
	
		for i, new_page in enumerate(self.page_queue):
			if len(current_pages) < self.page_slots:
				current_pages.append(new_page)
			elif new_page not in current_pages: 

				# then we find the distance to next itteration of the page of everythig in the current pages list
				index_to_replace:int = 0
				page_distance_of_index:int = 0
				for j, page in enumerate(current_pages):
					if page in self.page_queue[i+1:]:
						if self.page_queue[i+1:].index(page) > page_distance_of_index:
							page_distance_of_index = self.page_queue[i+1:].index(page)
							index_to_replace = j
					else:
						index_to_replace = j
						break
				current_pages[index_to_replace] = new_page

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
