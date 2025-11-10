# Initialise a 5x5 matrix of zeros
matrix = [[0 for i in range(5)] for j in range(5)]
num_rows = 5
num_cols = 5

# Loop through each row index
for i in range(num_rows):
    while True:
        user_input = input()
        row_strings = user_input.split()
        if len(row_strings) == num_cols:
            try:
                row_integers = [int(num) for num in row_strings]
                matrix[i] = row_integers
                break 
            except ValueError:
                print("Invalid input. Please ensure all inputs are integers.")
        else:
            print(f"Invalid number of elements. Expected {num_cols} elements, but got {len(row_strings)}.")

count = 0
found_one = False
column_found=0
row_found=0
for i in range(num_rows):
    for j in range(num_cols):
        if matrix[i][j] == 1:
            row_found = i
            column_found = j
            found_one = True
            break
    if found_one == True:
        break
    
# example 1, 4
target_row = 2
target_col = 2

row_shifts = abs(row_found - target_row) 
cols_shifts = abs(column_found - target_col)
result = row_shifts + cols_shifts
print(result)