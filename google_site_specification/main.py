# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

# ========================================================================
# MAIN 
# ========================================================================

def main():
	
	file_path_1 = rf".\keyword.txt"
	file_path_2 = rf".\exclusion_list.txt"
	file_path_3 = rf".\formatted_search.txt"
	
	final_string = ""

	
	file_ptr_1 = open(file_path_1, "r")
	final_string = final_string + file_ptr_1.read() + " "
	file_ptr_1.close()

	counter = 0
	file_ptr_2 = open(file_path_2, "r")
	for line in file_ptr_2:
		f_line = "-site:" + line.strip('\n') + ".com "
		final_string = final_string + f_line
		counter = counter +1
	file_ptr_2.close()


	file_ptr_3 = open(file_path_3, "w")
	file_ptr_3.write(final_string)

	print(final_string)

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