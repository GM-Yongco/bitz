# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: matrix multiplication that will help me with my assignment for linear equations
# HEADERS ================================================================

import pandas as pd

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# HELPER FUNCTIONS 
# ========================================================================
	
def my_read_csv(file_name:str) -> pd.core.frame.DataFrame:
	df:pd.core.frame.DataFrame = pd.read_csv(
		filepath_or_buffer = "matrix.csv", 
		sep = ",", 
		header = None
	)
	df.reset_index(drop = True, inplace = True)
	return df
	
def minimal_print_df(
		x:
			pd.core.frame.DataFrame|
			pd.core.series.Series
		)->None:
	print(f"{x.to_string(header=False, index=False)}\n")

# ========================================================================
# FUNCTIONS CORE 
# ========================================================================

def row_swap(		
		x:pd.DataFrame,
		row_a:int = 1,
		row_b:int = 1
		) -> None:
			
	row_a = row_a - 1
	row_b = row_b - 1
	# because math starts with 1 ;^;
	
	x.iloc[[row_a, row_b]] = x.iloc[[row_b, row_a]].values
	print(f"\tR{row_a + 1} <-> R{row_b + 1}")
	minimal_print_df(df)
	# no return val cuz df are like pointers

def row_add(
		x:pd.DataFrame,
		row_a:int = 1,
		row_b:int = 1,
		row_a_multiple:int = 1,
		row_b_multiple:int = 1,
		is_add:bool = True 
	) -> None:
	# the changed row will be on row 1
	
	row_a = row_a - 1
	row_b = row_b - 1
	# because math starts with 1 ;^;
		
	temp_row_b:pd.Series = x.iloc[row_b] * row_b_multiple
	
	x.iloc[row_a] = x.iloc[row_a] * row_a_multiple
	if is_add:
		x.iloc[row_a] = x.iloc[row_a] + temp_row_b
	else:
		x.iloc[row_a] = x.iloc[row_a] - temp_row_b
	
	# ====================================================================
	
	report:str = "\t"
	report += f"{row_a_multiple}R{row_a+1}"
	if is_add:
		report += " + "
	else:
		report += " - "
	report += f"{row_b_multiple}R{row_b+1}"
	report += f" -> R{row_a+1}"
	
	print(report)
	minimal_print_df(df)

def row_multiply(
		x:pd.DataFrame, 
		row_number:int = 1, 
		row_multiple: int = 1,
		is_multiply:bool = True
	) -> None:

	row_number = row_number - 1
	if is_multiply:
		x.iloc[row_number] = x.iloc[row_number] * row_multiple
	else:
		x.iloc[row_number] = x.iloc[row_number] / row_multiple
		
	# ====================================================================
	
	report:str = "\t"
	report += f"R{row_number+1}"
	if is_multiply:
		report += " * "
	else:
		report += " / "
	report += f"{row_multiple}"
	report += f" -> R{row_number+1}"
	
	print(report)
	minimal_print_df(x)
		
# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	df:pd.core.frame.DataFrame = my_read_csv("matrix.csv")
	minimal_print_df(df)
	
	section("START OF COMPUTATIONS")

	
	row_add(df, 2, 1, 1, 2, False)
	row_multiply(df, 2, 3, False)
	
	row_add(df, 1, 2, 1, 2)
	
	section("END")
