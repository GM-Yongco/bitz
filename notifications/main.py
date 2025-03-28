# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: code to notify when whatever happens
	# were also gonna need 
	# sudo apt install libnotify-bin
	# for the notification
	# note: also only works on debian
# HEADERS ================================================================

import subprocess
import time

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)
	return None

# ========================================================================
# FUNCTIONS 
# ========================================================================

def get_ram_value()->int:
	ram_total:str = subprocess.check_output(
		'vmstat -s | grep "total memory"', 
		shell=True, 
		text=True
	)
	ram_used:str = subprocess.check_output(
		'vmstat -s | grep "used memory"', 
		shell=True, 
		text=True
	)
	int_ram_total:int = int(ram_total.strip().rstrip("K total memory"))
	int_ram_used:int = int(ram_used.strip().rstrip("K used memory"))
	return int((int_ram_used/int_ram_total)*100)

def get_battery_value()->int:
	battery_percent:str = subprocess.check_output(
		"upower -i $(upower -e | grep 'BAT') | grep -E 'percentage'", 
		shell=True, 
		text=True
	)
	return int(battery_percent.strip().lstrip("percentage:").lstrip().rstrip("%"))

def send_notif(
		notif_title:str = "template_title",
		notif_content:str = "template_content"
		)->None:
	subprocess.run(["notify-send", notif_title, notif_content])
	return None

# ========================================================================
# FUNCTIONS 2
# ========================================================================

def repeat_tasks():
	sleep_seconds:int = 30
	cycle_count_battery_check:int = 10

	cycle_count:int = 0
	while(True):

		if cycle_count % cycle_count_battery_check == 0:
			if (get_battery_value() > 85) and ():
				send_notif(notif_title="Battery is above 85%", notif_content="")
			elif(get_battery_value() < 25):
				send_notif(notif_title="Battery is lower than 25%", notif_content="")

		if get_ram_value() > 80:
			send_notif(notif_title="RAM is above 85", notif_content="")
		
		print(f"cycle: {cycle_count}")
		cycle_count += 1
		time.sleep(sleep_seconds)

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	repeat_tasks()

	section("END")