from utils import load_data

filename= "day6_ex.txt"
with open(filename, "r") as file:
    day6_puzzle = [ [y for y in x.rstrip()] for x in file.readlines()]

print(day6_puzzle)

def find_element_index(lst_of_lsts, element):
    """
    Find the index of an element in a list of lists.
    
    Args:
        lst_of_lsts (list): A list of lists to search in.
        element (any): The element to find.
    
    Returns:
        tuple: A tuple (outer_index, inner_index) representing the indices where the element is found,
               or None if the element is not found.
    """
    for outer_index, sublist in enumerate(lst_of_lsts):
        if element in sublist:
            inner_index = sublist.index(element)
            return (outer_index, inner_index)
    return None

def print_matrix(matrix):
    """
    Print a matrix (list of lists) line by line.
    
    Args:
        matrix (list of lists): The matrix to print.
    """
    for row in matrix:
        print(' '.join(map(str, row)))

directions = ['^', '>', 'v', '<']  # Up, Right, Down, Left
dir_map = {
        '^': (-1, 0),  # Up
        '>': (0, 1),   # Right
        'v': (1, 0),   # Down
        '<': (0, -1)   # Left
    }

x,y = find_element_index(day6_puzzle,'^')
direction = day6_puzzle[x][y]
print(direction )

while 0< x and x< len(day6_puzzle) and 0<y and y< len(day6_puzzle[0]) and day6_puzzle[x][y] != '#' :
    dx, dy = dir_map[direction]
    next_pos = (x + dx, y+ dy)
    day6_puzzle[x][y]='X'
    if day6_puzzle[next_pos[0]][next_pos[1]] != '#':
        #day6_puzzle[x][y],day6_puzzle[x-1][y] = 'X','^'
       # x = x-1
        x,y = next_pos 
    if day6_puzzle[next_pos[0]][next_pos[1]] == '#' :
        direction = directions[(directions.index(direction) + 1) % 4]
      #  day6_puzzle[x][y],day6_puzzle[x][y+1] = 'X','^'
       # y=y+1
        x,y = next_pos 
    if not (0 <= next_pos[0] < len(day6_puzzle) and 0 <= next_pos[1] < len(day6_puzzle[0])):
        
        print("Finish !")
        day6_puzzle[x][y]='X'
        x=-1
        pass
print_matrix(day6_puzzle)

def navigate_robot(matrix, start, direction):
    """
    Simulate a robot navigating through a matrix, marking its path with 'X'.
    Obstacles are represented by '#'.
    The robot turns 90 degrees clockwise upon hitting an obstacle.
    
    Args:
        matrix (list of lists): The grid of strings.
        start (tuple): Starting position (row, col) of the robot.
        direction (str): Initial direction, one of '^', '>', 'v', '<'.
    
    Returns:
        list of lists: The updated matrix with the robot's path.
    """
    directions = ['^', '>', 'v', '<']  # Up, Right, Down, Left
    dir_map = {
        '^': (-1, 0),  # Up
        '>': (0, 1),   # Right
        'v': (1, 0),   # Down
        '<': (0, -1)   # Left
    }
    pos = start

    while True:
        r, c = pos
        matrix[r][c] = 'X'  # Mark the current position with 'X'
        dr, dc = dir_map[direction]
        next_pos = (r + dr, c + dc)
        
        # Check if next position is within bounds
        if not (0 <= next_pos[0] < len(matrix) and 0 <= next_pos[1] < len(matrix[0])):
            break  # Stop if moving out of bounds
        
        nr, nc = next_pos
        if matrix[nr][nc] == '#':  # Hit an obstacle
            # Turn 90 degrees clockwise
            direction = directions[(directions.index(direction) + 1) % 4]
        elif matrix[nr][nc] == 'X':  # Hit already traveled path
            break
        else:
            pos = next_pos  # Move to the next position

    return matrix

start = find_element_index(day6_puzzle,'^')
direction = '^'

result = navigate_robot(day6_puzzle, start, direction)
for row in result:
    print(' '.join(row))
      
    #if day6_puzzle[x-1][y] == '#': 

