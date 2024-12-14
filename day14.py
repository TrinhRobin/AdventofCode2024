from utils import read_grid_from_file,print_matrix
import numpy as np
from PIL import Image
day14_input = np.array(read_grid_from_file("day14.txt"))
print_matrix(day14_input)

def move_robot(new_grid,x,y,vx,vy,N):
    rows, cols = len(new_grid), len(new_grid[0])
    for i in range(N):
        new_grid[y][x]-=1
        new_grid[(y+vy)%rows][(x+vx)%cols]+=1
        x,y = (x+vx)%cols,(y+vy)%rows
    return new_grid

def move_robot_matrix(data,grid,N):
    new_grid=[[x for x in l]for l in grid]
    rows, cols = len(new_grid), len(new_grid[0])
    for i, entry in enumerate(data, start=1):
        x,y=entry['position']
        vx,vy = entry['velocity']
        move_robot(new_grid,x,y,vx,vy,N)
    return new_grid


def read_positions_and_velocities(file_path):
    """Lit un fichier contenant des positions et des vitesses, et les stocke dans une liste."""
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Supprimer les espaces et extraire les positions et vitesses
            line = line.strip()
            if line:  # Ignorer les lignes vides
                parts = line.split(" ")
                p = tuple(map(int, parts[0][2:].split(',')))  # Position (p=...)
                v = tuple(map(int, parts[1][2:].split(',')))  # Vitesse (v=...)
                data.append({'position': p, 'velocity': v})
    return data

# Chemin du fichier texte
file_path = "day14.txt"

# Lire les données
data = read_positions_and_velocities(file_path)

grid_ex = [[0 for j in range(101)] for i in range(103)]
# Afficher les données
for i, entry in enumerate(data, start=1):
    #print(f"Objet {i}: Position = {entry['position']}, Vitesse = {entry['velocity']}")
    x,y=entry['position']
    vx,vy = entry['velocity']
    grid_ex[y][x]+=1

grid_100 = move_robot_matrix(data,grid_ex,100)

# Initialize counters
quadrants = {"top_left": 0, "top_right": 0, "bottom_left": 0, "bottom_right": 0}
mid_y,mid_x = len(grid_100)//2,len(grid_100[0])//2

quadrants = { 'top left' : sum([sum(l[:mid_x]) for l in grid_100[:mid_y]]),
'top right': sum([sum(l[(mid_x+1):]) for l in grid_100[:mid_y]]),
'bottom left' : sum([sum(l[:mid_x]) for l in grid_100[(mid_y+1):]]),
'bottom right': sum([sum(l[(mid_x+1):]) for l in grid_100[(mid_y+1):]])}

safety =1
for key,n_robot in quadrants.items():
    safety *= n_robot
print(safety)

def matrix_to_png(matrix, output_file, mode="L"):
    """
    Converts a matrix into a PNG image and saves it to the specified file.

    :param matrix: 2D NumPy array or list of lists containing pixel data.
    :param output_file: Path to save the PNG image (e.g., "output.png").
    :param mode: Image mode (default is "L" for grayscale).
                 Use "RGB" for color images.
    """
    # Convert the matrix to a NumPy array (if not already)
    matrix = np.array(matrix)

    # Normalize matrix values for grayscale (0-255)
    if mode == "L":
        matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min()) * 255
        matrix = matrix.astype(np.uint8)

    # Create the image object
    image = Image.fromarray(matrix, mode)

    # Save the image as PNG
    image.save(output_file)
    print(f"Image saved as {output_file}")

matrix_to_png(grid_ex, "day14/input.png")
for i in range(8000):
    matrix_to_png(move_robot_matrix(data,grid_ex,i), f"day14/output{i}.png")

