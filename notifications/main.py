# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: code to notify when ram and batter needs attention
	# were also gonna need 
	# sudo apt install libnotify-bin
	# for the notification
	# note: also only works on debian
# HEADERS ================================================================

import time
from utils_misc import section, log_write
from utils_notifs import get_battery_value, is_charging, get_ram_value, send_notif

# ========================================================================
# FUNCTIONS 2
# ========================================================================

def task_cycle():
	cycle_interval_seconds:int = 30
	ram_max:int = 80
	battery_max:int = 85
	battery_min:int = 25

	cycle_count:int = 0
	while(True):

		ram_now:int = get_ram_value()
		if ram_now > ram_max:
			message = f"RAM is above {ram_max}%"
			send_notif(notif_title=message, notif_content="")

		# ================================================================

		battery_now:int = get_battery_value()
		if (battery_now > battery_max) and (is_charging()):
			message = f"Battery is above {battery_max}%"
			send_notif(notif_title = message, notif_content="")
		elif(battery_now < battery_min) and (not is_charging()):
			message = f"Battery is below {battery_min}%"
			send_notif(notif_title=message, notif_content="")

		log_write(
			file_name=r"ram_and_battery_log_log.csv", 
			category=f"cycle: {cycle_count:6}", 
			ram = f"{ram_now:3}",
			battery = f"{battery_now:3}")
		
		# ================================================================

		cycle_count += 1
		time.sleep(cycle_interval_seconds)

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	task_cycle()
	section("END")