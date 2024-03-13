# Description		: Code that will impress u ;)
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# HEADERS ================================================================

import pandas as pd
import random as ra
from time import sleep

# ========================================================================
# FUNCTIONS 
# ========================================================================
def question(row: int, data_frame: pd.core.frame.DataFrame):

	choices_num = 2

	# ========================================================================
	# gets random other choices for the multiple choice
	# set to avoid collisions
	choices_set = {row}
	df_len = len(data_frame.index)
	while(len(choices_set) < choices_num):
		choices_set.add(ra.randint(0, df_len-1))

	# ========================================================================
	# remove row to put it somewhere in the list at random
	# change to list for index support
	choices_set.discard(row)
	choices_list = list(choices_set)
	choice_index = ra.randint(0, choices_num-1)		#honestly kindah dumb how range() is inclusive, exclusive and randint() is inclusive, inclusive
	choices_list.insert(choice_index, row)

	# ========================================================================
	# the actual questioning part
	print(f"What is the capital of {data_frame.iloc[row, 0]}")
	for i in range(0, choices_num):
		print(f"{i}) {data_frame.iloc[choices_list[i], 1]}")
	
	# ========================================================================
	# answer checking
	ret = 0
	try:
		answer = int(input("answer the number of the correct answer: "))
		if(answer == choice_index):
			print("\nYAY, YOU GOT IT RIGHT")
			ret = 1
		else:
			print(f"\nu got it wrong \nthe correct answer was {choice_index}, {data_frame.iloc[choices_list[choice_index], 1]}")
	except Exception as error:
		print("An exception occurred:", error)
	
	return ret


# ========================================================================
# MAIN 
# ========================================================================

def main():
	pd.set_option('display.max_columns', None)
	pd.set_option('display.max_rows', None)
	pd.set_option('display.width', 1000)

	file_name = "UN_countries"
	countries = pd.read_csv(rf".\REFERENCES\{file_name}.csv")

	# ========================================================================
	# FOR TESTING PURPOSES
	# print(countries.describe())
	# section("AFTER DESCRIBE")
	# print(countries)
	# print(countries.iloc[0, 1])
	# print(f"number of items {len(countries.index)}")
	# print(f"{type(1)}, {type(countries)}")
	# ========================================================================

	# ========================================================================
	# OPTIONAL CODE TO MIX IT UP
	
	# flips capitals and countries
	# then sorts by capitals
	# countries = countries.iloc[:, [1, 0] + list(range(2, len(countries.columns)))]
	# countries = countries.sort_values(by="CAPITALS", ascending=True)

	# starts from z
	# countries = countries.sort_values(by="COUNTRIES", ascending=False)

	# filters for srtating letters of countries
	countries = countries[countries['COUNTRIES'].str.startswith('U')]
	# ========================================================================
	
	list_indexes = list(range(0,len(countries.index)))

	# ========================================================================
	# shuffles the list
	# ra.shuffle(list_indexes)
	# ========================================================================
	score = 0

	for i in list_indexes:
		section(f"QUESTION {i}")
		score += question(i, countries)
		sleep(1)
	
	print(f"YOU GOT {score}\nOUT OF {len(list_indexes)}")

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

if __name__ == '__main__':
	section("START")
	main()
	section("END")