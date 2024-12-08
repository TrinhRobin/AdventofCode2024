import numpy as np
from utils import print_matrix

def read_grid_from_file(filename):
    """Reads a grid from a text file and converts it into a list of lists."""
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def find_antennas(grid):
    """Parse the grid and locate all antennas by frequency."""
    antennas = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    return antennas


# Fetch the data
day8_puzzle = read_grid_from_file("day8.txt")
print_matrix(day8_puzzle)
antennas =find_antennas(day8_puzzle)
print()

def calculate_antinodes(grid, antennas):
    """Find all unique antinodes based on antenna alignment and distances."""
    rows, cols = len(grid), len(grid[0])
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                # Get antenna positions
                (x1, y1), (x2, y2) = [positions[i], positions[j]]
                dx,dy =  abs(x2-x1),abs(y2-y1)
                ## x1 <= x2
                if y1<=y2:
                    
                    antinod1,antinod2 = (x1-dx,y1-dy) , (x2+dx,y2+dy)
                if y1>y2:
                    antinod1,antinod2 = (x1-dx,y1+dy) , (x2+dx,y2-dy)
                for anti in (antinod1,antinod2):
                    if 0 <= anti[0] < rows and 0 <= anti[1] < cols and anti[0] not in (x1,x2) and anti[1] not in (y1,y2):
                        antinodes.add(anti)
    return antinodes

antinodes = calculate_antinodes(day8_puzzle, antennas)
print(antinodes)
print("Nombre antinodes :", len(antinodes))


def calculate_antinodes_part2(grid, antennas):
    """Find all unique antinodes based on antenna alignment and distances."""
    rows, cols = len(grid), len(grid[0])
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                # Get antenna positions
                (x1, y1), (x2, y2) = [positions[i], positions[j]]
                dx,dy =  abs(x2-x1),abs(y2-y1)
                N_inter=min(int(rows/dx),int(cols/dy))
                #print("iterations:",N_inter)
                antinod_candidates =[]
                ## x1 <= x2
                if y1<=y2:
                    for k in range(N_inter):
                        antinod_candidates.append((x1-k*dx,y1-k*dy))
                        antinod_candidates.append((x2+k*dx,y2+k*dy))
                if y1>y2:
                    for k in range(N_inter):
                        antinod_candidates.append((x1-k*dx,y1+k*dy)) 
                        antinod_candidates.append((x2+k*dx,y2-k*dy))
                for anti in antinod_candidates:
                    if 0 <= anti[0] < rows and 0 <= anti[1] < cols:
                        #print("antinode :",anti)
                        #print("antinodes",antinodes)
                        antinodes.add(anti)
    return antinodes

antinodes = calculate_antinodes_part2(day8_puzzle, antennas)
print(antinodes)
print("Nombre antinodes :", len(antinodes))