# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================
import pandas as pd

# ========================================================================
# GLOBAL VARS
# ========================================================================
csv_path = "B-Days - Sheet2.csv"
column_names = ["name", "birth_day", "ID_number", "email"]
month_to_int = {
	"jan": 1,
	"feb": 2,
	"mar": 3,
	"apr": 4,
	"may": 5,
	"jun": 6,
	"jul": 7,
	"aug": 8,
	"sep": 9,
	"oct": 10,
	"nov": 11,
	"dec": 12,
	"january": 1,
	"february": 2,
	"march": 3,
	"april": 4,
	"may": 5,
	"june": 6,
	"july": 7,
	"august": 8,
	"september": 9,
	"october": 10,
	"november": 11,
	"december": 12
}

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def abbreviation_to_number(abbrev:str = "jan"):
	return month_to_int.get(abbrev.lower())

def format_date(raw_date:str = "jan 1"):
	
	raw_date = raw_date.replace(",", " ")
	raw_date = raw_date.split()

	formatted_date = {
		"month": int(abbreviation_to_number(raw_date[0])), 
		"day": int(raw_date[1])
	}

	return formatted_date

# ========================================================================
# MAIN 
# ========================================================================
def main():
	data = pd.read_csv(csv_path, header = None, names = column_names)
	data = data.reset_index(drop = True)
	data = data.drop("ID_number", axis = 1)
	data = data.drop("email", axis = 1)

	print(data.loc[0:20 , ("name", "birth_day")])

	section("FORMATTING")
	
	for i in range(0,len(data)):
		# there was one guy with "October 14, 2003" and it brok the converter
		try:
			formatted_date = format_date(data.loc[i, ("birth_day")])
			# data.loc[i, "birth_day"] = f"{formatted_date['month']}/{formatted_date['day']}"
			data.loc[i, "birth_day"] = f" =DATE(YEAR(TODAY()),{formatted_date['month']},{formatted_date['day']})"
		
		except Exception as error:
			print("An exception occurred:", error)
			print(f"index of problem {i}")

	print(data.loc[0:20 , ("name", "birth_day")])

	data.to_csv("formatted.csv", index = False, header = False)

# ========================================================================
# MISC FUNCTIONS FINAL
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

if __name__ == '__main__':
	section("START")
	main()
	section("END")