def load_data(filename:str,sep=' ')->list:
    """
    load input text file in a list
    """
    puzzle_input = []
    with open(filename, "r") as file:
        for line in file:
            puzzle_input.append([int(part) for part in line.rstrip().split(sep)])
        return puzzle_input
    
def print_matrix(matrix):
    """
    Print a matrix (list of lists) line by line.
    
    Args:
        matrix (list of lists): The matrix to print.
    """
    for row in matrix:
        print(' '.join(map(str, row)))