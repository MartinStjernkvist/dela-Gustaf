file_names = [
    "GaAs_final_col1_baseline_nm",
    "GaAs_final_col2_baseline_%T",
    "GaAs_final_col3_meas_nm",
    "GaAs_final_col4_meas_%T"
]
all_data = []

for file_name in file_names:
    with open(file_name, "r") as file:
        column_data = file.readlines()
        all_data.append(column_data)

# Transpose the data (assuming all columns have the same number of rows)
combined_data = zip(*all_data)

# Write the combined data to a new text file
output_file = "combined_data.txt"
with open(output_file, "w") as file:
    for row in combined_data:
        combined_row = "\t".join(map(str.strip, row))  # Strip whitespace from each element
        file.write(combined_row + "\n")


