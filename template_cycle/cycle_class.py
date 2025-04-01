# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: a template for a program that does something every set space of time
	# itll check every new minute, hour, day, week, month, and year
# ========= ========= ========= ========= ========= ========
# HEADERS
# ========= ========= ========= ========= ========= ========

import datetime
import time

# ========= ========= ========= ========= ========= ========
# FUNCTIONS MISC
# ========= ========= ========= ========= ========= ========

def section(section_name:str = "SECTION")  ->  None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========= ========= ========= ========= ========= ========
# CLASS 
# ========= ========= ========= ========= ========= ========

class TaskCycle:

	def __init__(self)->None:
		self.previous_year:int = -1
		self.previous_month:int = -1
		self.previous_week:int = -1
		self.previous_day:int = -1
		self.previous_hour:int = -1
		self.previous_minute:int = -1

	def cycle_message_date_format(
			date_type:str = "year", 
			previous_date_value:int = -1,
			current_date_value:int = 1)->str:
		return f"\n\t{date_type:10} update {previous_date_value:05} -> {current_date_value:05}"

	# date_type can be {"year", "month", "week", "day", "hour", "minute"}
	def date_update(
			self,
			date_type:str = "minute"
		)->None:
		pass

	# ========= ========= ========= ========= ========= ========

	def update_per_year(self, now:datetime.datetime):
		if now.year != self.previous_year:
			cycle_message += self.cycle_message_date_format("year", self.previous_year, now.year)
			self.previous_year = now.year
			try:
				pass
				# year functions
			except Exception as e:
				print(f"An error occurred: {e}")


	def update_per_month():
		pass
	def update_per_week():
		pass
	def update_per_day():
		pass
	def update_per_hour():
		pass
	def update_per_minute():
		pass

	# ==========================================================

	async def start(self)->None:
		cycle_count:int = 0
		while(True):
			now:datetime.datetime = datetime.datetime.now()
			cycle_message = f"cycle: {cycle_count}"

			# ========= ========= ========= ========= =========

			

			# ========= ========= =========

			if now.month != self.previous_month:
				cycle_message += self.cycle_message_date_format("month", self.previous_month, now.month)
				self.previous_month = now.month

			# ========= ========= =========
			
			if now.isocalendar()[1] != self.previous_week:
				cycle_message += self.cycle_message_date_format("week", self.previous_week, now.isocalendar()[1])
				self.previous_week = now.isocalendar()[1]

			# ========= ========= =========
			
			if now.day != self.previous_day:
				cycle_message += self.cycle_message_date_format("day", self.previous_day, now.day)
				self.previous_day = now.day

			# ========= ========= =========
			
			if now.hour != self.previous_hour:
				cycle_message += self.cycle_message_date_format("hour", self.previous_hour, now.hour)
				self.previous_hour = now.hour

			# ========= ========= =========
			
			if now.minute != self.previous_minute:
				cycle_message += self.cycle_message_date_format("minute", self.previous_minute, now.minute)
				self.previous_minute = now.minute

			# ========= ========= ========= ========= =========

			print(cycle_message)
			cycle_count += 1
			time.sleep(30)

# ========= ========= ========= ========= ========= ========
# MAIN 
# ========= ========= ========= ========= ========= ========

if __name__ == '__main__':
	section("START")

	repeated_tasks:TaskCycle = TaskCycle()
	repeated_tasks.start() 

	section("END")