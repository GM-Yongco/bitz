# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd



pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 5)


# CREATE -------------------------------------------------------------
def create():
	print("CREATE ---------------------------------------")
	new_id = [input("New ID?:\n")]
	new_name = [input("New name?:\n")]
	new_time = [input("New time?:\n")]
	new_message = [input("New message?:\n")]
	new_channel = [input("New channel?:\n")]

	alarm_db = pd.read_csv('alarm_db.csv')
	new = pd.DataFrame({
		"id":new_id,
		"name":new_name,
		"time":new_time,
		"message":new_message,
		"message":new_channel
	}, 
	index = [len(alarm_db)]
	)

	alarm_db = pd.concat([alarm_db, new])
	print(alarm_db)
	alarm_db.to_csv('alarm_db.csv', index=False)

# READ -------------------------------------------------------------
def read():
	print("READ -----------------------------------------")
	alarm_db = pd.read_csv('alarm_db.csv')
	print(alarm_db)

# UPDATE -------------------------------------------------------------
def update():
	print("UPDATE ---------------------------------------")
	index = int(input("Index Number?:\n"))
	column = input("Column Name?:\n")
	new_value = input("New value?:\n")

	alarm_db = pd.read_csv('alarm_db.csv')
	alarm_db.at[index, column] = new_value
	alarm_db.to_csv('alarm_db.csv', index=False)

# DELETE -------------------------------------------------------------
def delete():
	print("DELETE ---------------------------------------")
	index = int(input("Index Number?:\n"))
	
	alarm_db = pd.read_csv('alarm_db.csv')
	alarm_db = alarm_db.drop( index, axis=0)
	alarm_db.to_csv('alarm_db.csv', index=False)

# MENU ---------------------------------------------------------------
def menu():
	print(f"1.\tCreate\n2.\tRead\n3.\tUpdate\n4.\tDelete\n")
	reply = input("What u want?:\n")

	if(reply == '1'):
		create()
	elif(reply == '2'):
		read()
	elif(reply == '3'):
		update()
	elif(reply == '4'):
		delete()
	else:
		print("weirdo man ka")

	print("\n\n")
	menu()

menu()