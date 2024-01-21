# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================
import os

# ========================================================================
# GLOBAL VARIABLES
# ========================================================================

FOLDER_PATH = "./REFERENCES"
FILE_PATH = "./REFERENCES/sleep_on_the_floor.SRT"

# ========================================================================
# CLASSES
# ========================================================================

class LyricBlock:
	def __init__(self, time_start, time_end, text):
		try:
			self.time_start = int(time_start)
			self.time_end = int(time_end)
			self.text = str(text)

		except Exception as e:
			print(f"An error occurred: {e}")


# ========================================================================
# MISC 
# ========================================================================

def check_if_exist(x:str):
	if not(os.path.exists(x)):
		print(f"'{x}' exists")
		os.mkdir(x)
	else:
		print(f"'{x}' exists")

def string_to_seconds(x:str = "00:04:20,690"):
	# expected default output 260.69
	x = x.replace(':', ' ')
	x = x.replace(',', ' ')
	x = x.split(' ')
	
	return (int(x[0])* 3600) + (int(x[1]) * 60) + (int(x[2])) + (int(x[3]) * 0.001)

def format_SRT_to_class_list(file_path:str):
	file_ptr = open(file_path, "r")

	lyric_block_index = 0
	lyric_block_new = LyricBlock(0, 0, "")
	lyric_block_list = []

	for line in file_ptr:
		if line == "\n":
			lyric_block_index = 0
			lyric_block_list.append(lyric_block_new)
			lyric_block_new = LyricBlock(0, 0, "")
		else:
			lyric_block_index = lyric_block_index + 1

		if lyric_block_index == 2:
			line_split = line.split()
			lyric_block_new.time_start = string_to_seconds(line_split[0])
			lyric_block_new.time_end = string_to_seconds(line_split[2])
		elif lyric_block_index > 2:
			lyric_block_new.text = lyric_block_new.text + line
	lyric_block_list.append(lyric_block_new)

	return lyric_block_list

# ========================================================================
# MAIN 
# ========================================================================

def main():
	check_if_exist(FOLDER_PATH)
	lyric_block_list = format_SRT_to_class_list(FILE_PATH)
	
	i = 0
	for lyric in lyric_block_list:
		print(i)
		print(f"{lyric.time_start} --> {lyric.time_end}")
		print(lyric.text)
		i = i + 1

# ========================================================================
# FINAL RUN
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

if __name__ == '__main__':
	section("START")
	main()
	section("END")