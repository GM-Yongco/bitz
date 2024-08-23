# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: 
# 	a multiple choice test where the answersheet 
# 	and the question sheet are seprate one would use 
# HEADERS ================================================================

import io
from typing import List

import json
from random import randint

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def json_read(path:str = "philnits_FE-A_answers.json") -> List[str]:
	json_details:dict = {"error":"error"}
	try:
		file:io.TextIOWrapper = open(path, "r")
		json_details = json.load(file)
		file.close()
	except Exception as e:
		print(f"{__name__:30}{e}")

	# would return an empty list if unsucessful
	answers:List[str] = {}
	if json_details["error"] == "none":
		print(f"{'function: json_read':40} was successful")
		answers = json_details["answers"]
	return answers

# ========================================================================

def test_start(file_name:str = "philnits_FE-A_answers.json") -> None:
	answer_list:List[str] = json_read(path = file_name)

	question_number:int = 1
	user_input:str = ""
	while question_number <= len(answer_list):
		user_input:str = input(f"QUESTION {question_number:03}:").strip(" ")
		correct_answer:str = answer_list[question_number - 1]

		skipped:bool = False
		match user_input.lower():
			case "/skip":
				print("you skipped a question >:(((")
			case "/skip_to":
				skip_to_number:int = int(input("move to what number?"))
				if skip_to_number >= 1 and skip_to_number <= len(answer_list):
					question_number = skip_to_number  
				else:
					question_number = 1
				skipped = True
			case "/skip_to_rand":
				question_number = randint(1, len(answer_list))
				skipped = True
			case "/exit":
				break

			case _ if user_input.lower() == correct_answer.lower():
				print(f"{'CORRECT!':15} the answer was {correct_answer}")
			case _:
				print(f"{'WRONG!':15} the answer was {correct_answer}")
		

		if skipped == False:
			question_number += 1



# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	test_start(file_name = "philnits_FE-A_answers.json")

	section("END")