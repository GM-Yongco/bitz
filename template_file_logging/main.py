# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: for the file logging I will do on the other projects
# ========================================================================
# HEADERS
# ========================================================================

import csv
import pandas as pd
from datetime import datetime

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	print("-" * 50)
	print(section_name)
	print("-" * 50)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def log_read(file_name:str = "generic_log_file.csv"):
	custom_headers = ["year", "month", "day", "hour", "minute", "second", "category", "details"]
	df = pd.read_csv(file_name, header=None, names=custom_headers)
	print(df)

def log_write(
		file_name:str = "generic_log_file.csv", 
		category:str = "NA", 
		details:str = "NA"):
	
	time_now:datetime = datetime.now()
	log_data = [
		str(time_now.year), 
		f"{time_now.month:02}", 
		f"{time_now.day:02}",
		f"{time_now.hour:02}", 
		f"{time_now.minute:02}", 
		f"{time_now.second:02}",
		str(category.replace(",", "<comma>")),
		str(details.replace(",", "<comma>"))
	]

	with open(file_name, "a", newline="") as log_file:
		writer = csv.writer(log_file)
		writer.writerow(log_data)

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	log_write(category=f"test{datetime.now().microsecond:2}", details=f"test{datetime.now().hour:05}")
	log_read()

	section("END")