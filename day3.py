import re

input_data= "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = r"mul\(\d{1,3},\d{1,3}\)"

# Find all matches
matches = re.findall(pattern, input_data)

# Evaluate the valid instructions
result = 0
for match in matches:
    # Extract numbers from each valid mul(X,Y)
    numbers = re.findall(r"\d+", match)
    x, y = map(int, numbers)
    result += x * y

print("Total:", result)


def compute_mul_sum(filename):
    # Regex pattern to match valid mul(X,Y) instructions
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    try:
        # Read the file content
        with open(filename, "r") as file:
            content = file.read()

        # Find all matches of the pattern
        matches = re.findall(pattern, content)

        # Compute the sum of all valid mul results
        result = 0
        for match in matches:
            # Extract the numbers from each valid instruction
            numbers = re.findall(r"\d+", match)
            x, y = map(int, numbers)  # Convert the numbers to integers
            result += x * y  # Add the multiplication result to the total

        return result

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def compute_mul_sum_with_do_dont(content):
    # Regex patterns
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"  # Matches valid mul(X,Y)
    control_pattern = r"do\(\)|don't\(\)"    # Matches do() or don't()
    
     # Find all instructions in the file
    instructions = re.findall(f"{mul_pattern}|{control_pattern}", content)

    # Initialize state
    mul_enabled = True  # Start with mul instructions enabled
    total = 0

    for instruction in instructions:
        if instruction == "do()":
            mul_enabled = True  # Enable future mul instructions
        elif instruction == "don't()":
            mul_enabled = False  # Disable future mul instructions
        elif mul_enabled and instruction.startswith("mul("):
            # Process mul instruction if enabled
            numbers = re.findall(r"\d+", instruction)  # Extract numbers
            x, y = map(int, numbers)
            total += x * y  # Add the multiplication result to the total

    return total

  
    
# Example usage
if __name__ == "__main__":
    filename = "day3.txt"  # Replace with your text file's name
    total = compute_mul_sum(filename)
    if total is not None:
        print("Total sum of valid mul instructions:", total)
    print(compute_mul_sum_with_do_dont(input_data))
    with open(filename, "r") as file:
            content = file.read()
            print(compute_mul_sum_with_do_dont(content))