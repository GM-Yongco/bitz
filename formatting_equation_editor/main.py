# Description		: Code that will impress u ;)
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# HEADERS ================================================================

# ========================================================================
# MAIN 
# ========================================================================

def main():
	file_name = "input.txt"

	file = open(file_name, "r")
	input_equation = file.read()
	input_equation = input_equation.replace("A", "W")
	input_equation = input_equation.replace("B", "X")
	input_equation = input_equation.replace("C", "Y")
	input_equation = input_equation.replace("D", "Z")

	print(input_equation)
	file.close()

	file = open(file_name, "w")
	file.write(input_equation)

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