from pylab import *
from scipy import ndimage
from utils import print_matrix
import numpy as np
from scipy.ndimage import measurements, binary_dilation

def read_grid_from_file(filename):
    """Reads a grid from a text file and converts it into a list of lists."""
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def find_clusters(array):
    clustered = np.empty_like(array)
    unique_vals = np.unique(array)
    cluster_count = 0
    test ={val:0 for val in unique_vals}
 
    for val in unique_vals:
        labelling, label_count = ndimage.label(array == val)
        test[val] = cluster_count
        for k in range(1, label_count + 1):
            clustered[labelling == k] = cluster_count
            cluster_count += 1
    print("map",test)
    return clustered, cluster_count


day12_input = np.array(read_grid_from_file("day12.txt"))
print_matrix(day12_input)

clusters, cluster_count = find_clusters(day12_input)
print("Found {} clusters:".format(cluster_count))
print(clusters)

def compute_cluster_areas(labeled_array):
    """
    Computes the area of each cluster.
    Returns a dictionary where keys are cluster IDs and values are areas.
    """
    labeled_array = np.array(labeled_array, dtype=int)  # Ensure numeric type
    cluster_ids = np.unique(labeled_array)
    #cluster_ids = cluster_ids[cluster_ids > 0]  # Exclude background (assume label 0 is background)
    areas = {cid: np.sum(labeled_array == cid) for cid in cluster_ids}
    return areas


# Compute cluster areas
cluster_areas = compute_cluster_areas(clusters)
print("Cluster Areas:")
for cluster_id, area in cluster_areas.items():
    print(f"Cluster {cluster_id}: Area {area}")

# Compute cluster areas and perimeters
# Example labeled array
labeled_array =clusters.astype(int)
labeled_array2 = labeled_array+1
print(labeled_array)
# Use find_objects to get bounding boxes
clusters_slices = ndimage.find_objects(labeled_array2)
#print(clusters_slices  )
# Print bounding boxes
#for i, slc in enumerate(clusters_slices ):
    #if slc is not None:  # Ensure there's a labeled object
        #print(f"Object {i+1} bounding box: {slc}")
        #print(f"perimeter : {compute_bounding_box_sides(slc)}")

neighbors = {
        '^': (-1, 0),  # Up
        '>': (0, 1),   # Right
        'v': (1, 0),   # Down
        '<': (0, -1)   # Left
    }

# Initialize an empty list to hold the boundary coordinates of each cluster
boundary_points = {i: set() for i in range(0, cluster_count )}
rows = labeled_array.shape[0]
cols = labeled_array.shape[1]
# Iterate over the matrix and find boundary points
for i in range(rows):
    for j in range(cols):
        # Get the current label (cluster) of the matrix element
        cluster_label = labeled_array[i, j]
        #print("Cluster number: ",i,j,cluster_label)
       # print(labeled_array[i])
        # If the point is part of a cluster and is not at the border, check for boundary 
        # Check the 4 neighbors: up, down, left, right
            # If any neighbor is outside the cluster (or out of bounds), it's a boundary
        for n,dir in neighbors.items():
            di,dj = dir[0],dir[1]
            ni,nj = i+di,j+dj
            if ni < 0 or ni>= rows:
                boundary_points[cluster_label].add((i,n))
            if nj<0 or nj >= cols:
                boundary_points[cluster_label].add((j,n))
            if 0<= ni<rows and 0<=nj<cols and  labeled_array[ni, nj] != cluster_label and dj==0:
                boundary_points[cluster_label].add((i,n))
            if  0<= ni<rows and 0<=nj<cols and  labeled_array[ni, nj] != cluster_label and di==0:
                boundary_points[cluster_label].add((j,n))

                #or ni >= labeled_array.shape[0] or nj < 0 or nj >= labeled_array.shape[1] or labeled_array[ni, nj] != cluster_label:
                  #  boundary_points[cluster_label].append((i, j))
                   
    
    # Return the boundary points for each cluster
print(boundary_points)
    
# Find the boundaries of each cluster
#boundary_points = find_cluster_boundaries(labeled_array)

# Output the boundary points for each cluster
for cluster_label, points in boundary_points.items():
    print(f"Cluster {cluster_label} has boundary points: {len(points)}")


def calculate_total_fencing_price(array):
    # Ensure the array is a NumPy array
    array = np.array(array)
    
    # Get unique labels (plant types)
    unique_labels = np.unique(array[array != '0'])  # Exclude '0' if it represents empty space
    
    total_price = 0
    regions_info = []
    
    for label in unique_labels:
        # Create a mask for the current label
        mask = (array == label)
        
        # Label connected components
        labelled, num_features = measurements.label(mask)
        
        for region_id in range(1, num_features + 1):
            # Create a mask for the current region
            region_mask = (labelled == region_id)
            
            # Compute area (number of cells in the region)
            area = np.sum(region_mask)
            
            # Compute perimeter
            perimeter = 0
            rows, cols = region_mask.shape
            for r in range(rows):
                for c in range(cols):
                    if region_mask[r, c]:  # If this cell is part of the region
                        # Count edges that are not shared with another cell of the same region
                        if r == 0 or not region_mask[r - 1, c]:  # Top edge
                            perimeter += 1
                        if r == rows - 1 or not region_mask[r + 1, c]:  # Bottom edge
                            perimeter += 1
                        if c == 0 or not region_mask[r, c - 1]:  # Left edge
                            perimeter += 1
                        if c == cols - 1 or not region_mask[r, c + 1]:  # Right edge
                            perimeter += 1
            
            # Calculate price for this region
            price = area * perimeter
            total_price += price
            
            # Store info
            regions_info.append((label, region_id, area, perimeter, price))
    
    return total_price, regions_info
# Example input
array =  np.array(read_grid_from_file("day12_all.txt"))

# Calculate total fencing price
#total_price, regions_info = calculate_total_fencing_price(array)

# Print results
#print("Total Fencing Price:", total_price)
#for info in regions_info:
 #   print(f"Region {info[0]}-{info[1]}: Area = {info[2]}, Perimeter = {info[3]}, Price = {info[4]}")

