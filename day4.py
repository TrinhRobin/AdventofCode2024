import re 
import numpy as np


def load_file_into_list(filename):
    try:
        # Open the file and read all lines
        with open(filename, "r") as file:
            lines = file.readlines()
        # Strip newline characters and return the list
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
filename = "day4.txt"  # Replace with your file name
day4_puzzle = load_file_into_list(filename)

print("Loaded List:")
print(day4_puzzle)


input_data = [
     'MMMSXXMASM',
     'MSAMXMSMSA',
     'AMXSXMAAMM',
     'MSAMASMSMX',
     'XMASAMXAMM',
     'XXAMMXXAMA',
     'SMSMSASXSS',
     'SAXAMASAAA',
     'MAMMMXMMMM',
     'MXMXAXMASX'
     ]
pattern ='XMAS'
# Find all matches
matches = [re.findall(pattern, input) for input in input_data]

# Evaluate the valid instructions
result = np.sum(np.array([len(x) for x in matches]))
#print(matches)
#print("Total:", result)


def generate_patterns(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    print(rows,cols)

    # Convert all rows to strings (horizontal)
    horizontal = ["".join(row) for row in matrix]

    # Vertical: Read columns
    vertical = ["".join(matrix[row][col] for row in range(rows)) for col in range(cols)]

    # Diagonal: Top-left to bottom-right
    diagonals_top_left = []
    for d in range(rows + cols - 1):
        diag = []
        for row in range(rows):
            col = d - row
            if 0 <= col < cols:
                diag.append(matrix[row][col])
        if diag:
            diagonals_top_left.append("".join(diag))

    # Diagonal: Top-right to bottom-left
    diagonals_top_right = []
    for d in range(-rows + 1, cols):
        diag = []
        for row in range(rows):
            col = row + d
            if 0 <= col < cols:
                diag.append(matrix[row][col])
        if diag:
            diagonals_top_right.append("".join(diag))

    # Generate reversed patterns
    horizontal_reversed = [string[::-1] for string in horizontal]
    vertical_reversed = [string[::-1] for string in vertical]
    diagonals_top_left_reversed = [string[::-1] for string in diagonals_top_left]
    diagonals_top_right_reversed = [string[::-1] for string in diagonals_top_right]

    # Combine all patterns
    all_patterns = {
        "horizontal": horizontal,
        "vertical": vertical,
        "diagonals_top_left": diagonals_top_left,
        "diagonals_top_right": diagonals_top_right,
        "horizontal_reversed": horizontal_reversed,
        "vertical_reversed": vertical_reversed,
        "diagonals_top_left_reversed": diagonals_top_left_reversed,
        "diagonals_top_right_reversed": diagonals_top_right_reversed,
    }

    return all_patterns

def count_pattern_in_patterns(patterns, search_pattern):
    # Find all matches
    matches = [re.findall(search_pattern, pattern) for pattern in patterns]
    # Evaluate the valid instructions
    count = np.sum(np.array([len(x) for x in matches]))
    return count

def count_pattern_in_patterns_matrix(dict, search_pattern):
    count=0
    for matrix in dict.values():
        count+=  count_pattern_in_patterns(matrix,search_pattern)
    return count

# Example usage:
matrix = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

patterns_input = generate_patterns(input_data)
patterns = generate_patterns(day4_puzzle)
# Print all patterns
def print_patterns(patterns):
    for key, values in patterns.items():
        print(f"{key.capitalize()}:")
        for value in values:
            print(value)
        print()
    

search_pattern = "XMAS"

#occurrences =  count_pattern_in_patterns_matrix(patterns, search_pattern)
#print("Total:", count_pattern_in_patterns(input_data,search_pattern))
#print(f"Occurrences of '{search_pattern}':", occurrences)

##part 2
def find_matching_elements_and_indices(list1, list2):
    """
    Find matching elements and their indices in two lists.
    Both lists must be of the same length.
    """
    # Ensure the lists are the same length
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length.")
    
    # Find matches
    matches = [(index, element1) for index, (element1, element2) in enumerate(zip(list1, list2)) if element1 == element2 or element1[::-1] == element2]
    
    return matches

def find_matching_non_empty_lists(list1, list2):
    """
    Find indices and counts of matching non-empty lists in two lists.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length.")
    
    matching_indices = []
    matching_count = 0
    
    for index, (sublist1, sublist2) in enumerate(zip(list1, list2)):
        if sublist1 and sublist2:  # Both lists are non-empty
            matching_indices.append(index)
            matching_count += len(sublist1)

    return matching_indices, matching_count

print_patterns(patterns_input )
search_pattern='MAS|SAM'
matches = [re.findall(search_pattern, pattern) for pattern in patterns_input['diagonals_top_left_reversed']]
matches2 = [re.findall(search_pattern, pattern) for pattern in patterns_input['diagonals_top_right_reversed']]
matches3 = [re.findall(search_pattern, pattern) for pattern in patterns_input['diagonals_top_left']]
matches4 = [re.findall(search_pattern, pattern) for pattern in patterns_input['diagonals_top_right']]
print(matches)
print(matches2 )
print(find_matching_elements_and_indices(matches,matches2))
print(find_matching_non_empty_lists(matches,matches2))
print(find_matching_non_empty_lists(matches3,matches4))


def count_x_mas(matrix):
    """
    Counts the number of X-MAS patterns in a given matrix.
    Each X-MAS consists of two MAS patterns forming an X shape.
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    target = "MAS"
    target_reversed = target[::-1]

    count = 0

    # Iterate through the matrix and check for the X-MAS pattern
    for i in range(rows - 2):  # At least 3 rows needed
        for j in range( cols - 2):  # Center of the X must fit
            # Check for X-MAS:
            # Top-left to bottom-right diagonal must be "M", "A", "S" (or reversed)
            # Top-right to bottom-left diagonal must be "M", "A", "S" (or reversed)
            top_left_to_bottom_right = "".join([matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2]])
            top_right_to_bottom_left = "".join([matrix[i][j+2], matrix[i+1][j+1], matrix[i+2][j]])

            if (top_left_to_bottom_right in (target, target_reversed)) and (
                top_right_to_bottom_left in (target, target_reversed)
            ):
                #print("motif numero ", count,i,j)
                count += 1

    return count


# Example matrix
matrix = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    "..........",
]

# Convert matrix from string to character list for easier indexing
matrix = [list(row) for row in matrix]
print(matrix)
# Count X-MAS patterns
x_mas_count = count_x_mas(matrix)

print("Number of X-MAS patterns:", x_mas_count)

matrix = [list(row) for row in day4_puzzle]
x_mas_count = count_x_mas(matrix)

print("Number of X-MAS patterns:", x_mas_count)

x_mas_count = count_x_mas(day4_puzzle)

print("Number of X-MAS patterns:", x_mas_count )

