# Description		: Code that will impress u ;)
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# HEADERS ================================================================

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def section(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def create_files() -> None:
	file = open(r"REFERENCES/output_1.txt", "x")
	file.close()
	
	file = open(r"REFERENCES/output_2.txt", "x")
	file.close()

	file = open(r"REFERENCES/output_3.txt", "x")
	file.close()


def format1() -> None:
	file = open(r"REFERENCES/script.txt", "r")
	text = file.read()
	file.close()

	text = text.replace("Dennis' Mother", "Mother")
	text = text.replace("\n", " ")
	text = text.replace("Dennis:", "\nDennis:")
	text = text.replace("Mother:", "\nMother:")
	text = text.replace("Arthur:", "\nArthur:")

	file = open(r"REFERENCES/output_1.txt", "w")
	file.write(text)
	file.close()

def format2() -> None:
	file = open(r"REFERENCES/output_1.txt", "r")
	text = file.read()
	file.close()

	text = text.replace("Dennis: ", "")
	text = text.replace("Mother: ", "")
	text = text.replace("Arthur: ", "")
	text = text.replace(r'"', "")
	text = text.replace(r"'", "")

	file = open(r"REFERENCES/output_2.txt", "w")
	file.write(text)
	file.close()

def format3() -> None:
	file = open(r"REFERENCES/output_2.txt", "r")
	text: str = file.read()
	file.close()

	new_text: str = ''
	letter_before: str = ''
	letter_new: str = ''
	for letter in text:
		if letter not in [r'"', '\n']:
			if (letter_before in ['-', ' ']) or (letter in ['!', '.', ',', '?', '-']):
				new_text = new_text + letter
			elif letter_before == '\n':
				new_text = new_text + '\n' + letter

		letter_before = letter

	file = open(r"REFERENCES/output_3.txt", "w")
	file.write(new_text)
	file.close()

# ========================================================================
# MAIN 
# ========================================================================

def main() -> None:
	format2()
	format3()

if __name__ == '__main__':
	section("START")
	main()
	section("END")