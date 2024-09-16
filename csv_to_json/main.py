# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================

import os
import json
import pandas as pd

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)


# ========================================================================
# FUNCTIONS 
# ========================================================================

path_csv:str = "UN_countries.csv"
path_txt:str = "output.txt"

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	# CSV STUFF
	df = pd.read_csv(path_csv)
	print(df.__len__())
 
	# DICT AND LIST STUFF
	output:list = []
	template:dict = {
		"question": "What is the capital of",
		"qImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXtcQAqZPsyJ8jKKBklMIFCdS37W6fiSRBgQ&s",
		"answer": "",
		"aImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXtcQAqZPsyJ8jKKBklMIFCdS37W6fiSRBgQ&s",
	}
 
	# CSV LINE TO DICT INTO THE LIST
	for i in range(0, 45):
		template_copy = template.copy()

		template_copy["question"] = template_copy["question"] + " " + 	df.iloc[i]["question"]
		template_copy["answer"] = template_copy["answer"] + df.iloc[i]["answer"]
  
		output.append(template_copy)

	# to json then save
	json_output = json.dumps(output, indent=2)
	print(json_output)
	with open('output.json', 'w') as f:
		f.write(json_output)

	section("END")