# Description		: Auto make a csv truth table and k-map for me
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# HEADERS ================================================================
import pandas as pd
from matplotlib import pyplot as plt
import math as ma

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def create_csv_template(file_path: str = "./REFERENCES/test.csv",
		table_inputs: int = 3,
		table_outputs: int = 8) -> None:
	# inputs must be > 1 and < 6
	# outputs must be > 0

	# creates the input columns
	table = pd.DataFrame({"input_1": [0]*(pow(2,table_inputs))})
	for i in range(2,table_inputs+1):
		table[f"input_{i}"] = 0
	
	# puts in the ones for the inputs
	for column in range(0,table_inputs):
		for row in range(0,pow(2,table_inputs)):
			if(row%(pow(2,column+1)) > (pow(2,column)-1)):
				table.iloc[row,column] = 1

	# flips the input colums order
	table = table[table.columns[::-1]]

	# puts in the output columns default 0
	for i in range(1, table_outputs+1):
		table[f"output_{i}"] = 0
	table.to_csv(file_path, index=False)

# ========================================================================

def create_csv_k_map_(file_path: str = "./REFERENCES/test.csv") -> None:
	big_table = pd.read_csv(file_path)
	num_columns = big_table.shape[1]
	num_columns_output = int(big_table.columns[-1].lstrip("output_"))
	num_columns_input = num_columns - num_columns_output

	# getting dimensions of the kmap
	smol_table_height = pow(2, ma.floor(num_columns_input/2))
	smol_table_length = pow(2, ma.ceil(num_columns_input/2))

	# create a template kmap with all 0s
	smol_table_template = pd.DataFrame({f"_0_": [0]*(smol_table_height)})
	for i in range(1, smol_table_length):
		smol_table_template[f"_{i}_"] = 0

	# creating the csvs for each kmap
	file_path_output = "./REFERENCES/output_"
	for column in range(num_columns - num_columns_output, num_columns):
		smol_table = smol_table_template.copy()
		for row in range(0, pow(2, num_columns_input)):
			if big_table.iloc[row, column] != 0:
				smol_table.iloc[ma.floor(row/smol_table_length), row%smol_table_length] = big_table.iloc[row, column]
		
		# swaping columns part
		if smol_table_length > 2:
			smol_table["_2_"], smol_table["_3_"] = smol_table["_3_"], smol_table["_2_"]
		if smol_table_height > 2:
			smol_table.iloc[2], smol_table.iloc[3] = smol_table.iloc[3].copy(), smol_table.iloc[2].copy()
		if smol_table_length > 4:
			smol_table["_4_"], smol_table["_7_"] = smol_table["_7_"], smol_table["_4_"]
			smol_table["_5_"], smol_table["_6_"] = smol_table["_6_"], smol_table["_5_"]
		
		smol_table.to_csv(f"{file_path_output + str(column - num_columns_input + 1)}.csv", index=False)

# ========================================================================

def display_kmap(file_path: str = "./REFERENCES/test.csv") -> None:
	big_table = pd.read_csv(file_path)
	table_outputs = int(big_table.columns[-1].lstrip("output_"))

	output = open("./OUTPUT/output.html", 'w')
	template_1 = open("./REFERENCES/template_1.html", 'r')
	output.write(template_1.read())
	template_1.close

	for i in range(1, table_outputs + 1):
		smol_table = pd.read_csv(f"./REFERENCES/output_{i}.csv")
		num_col = smol_table.shape[1]
		num_row = smol_table.shape[0]
		
		output.write(f"\n<h1>output_{i}</h1>")

		output.write("\n<table><tbody>")
		for r in range(0, num_row):
			output.write("\n<tr>")
			for c in range(0, num_col):
				output.write("<td>")
				output.write(str(smol_table.iloc[r, c]))
				output.write("</td>")
			output.write("\n</tr>")
		output.write("\n</tbody>\n</table>")

	template_2 = open("./REFERENCES/template_2.html", 'r')
	output.write(template_2.read())	
	template_2.close
	output.close

# ========================================================================
# MAIN 
# ========================================================================

def main() -> None:
	# create_csv_template(table_inputs=4, table_outputs=7)
	create_csv_k_map_()
	display_kmap()

if __name__ == '__main__':
	section("START")
	main()
	section("END")