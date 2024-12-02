def load_data(filename:str,sep=' ')->list:
    """
    load input text file in a list
    """
    puzzle_input = []
    with open(filename, "r") as file:
        for line in file:
            puzzle_input.append([int(part) for part in line.rstrip().split(sep)])
        return puzzle_input