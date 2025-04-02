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

if __name__ == '__main__':
	from utils_misc import section

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

def is_charging()->bool:
	charging_status:str = subprocess.check_output(
		"cat /sys/class/power_supply/BAT0/status", 
		shell=True, 
		text=True
	)
	# charing statuses could be Charging, Discharging, Full, Not charging, Unknown
	# for our usecase, "Not charging" is considered charging as it is not discharging

	ret_val:bool = False
	if(charging_status.strip().lower() == "charging"):
		ret_val = True
	elif(charging_status.strip().lower() == "not charging"):
		ret_val = True
	return ret_val

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
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("TEST START")

	print(f"{'ram value':15}: {get_ram_value()}%")
	print(f"{'is charging':15}: {is_charging()}")
	print(f"{'battery value':15}: {get_battery_value()}%")
	send_notif(notif_title="TEST TITLE", notif_content="TEST CONTENT")

	section("TEST END")