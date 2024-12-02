import pandas as pd
import numpy as np
from utils import load_data

# Fetch the data
day1_puzzle = load_data("day1.txt",sep="   ")
print(day1_puzzle[:10])


list1 = [x[0] for x in day1_puzzle ]
list2 = [x[1] for x in day1_puzzle ]
# Step 1: Sort the lists
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# Step 2: Ensure lists are the same length
# (If they are not the same length, truncate or pad with zeros)
if len(sorted_list1) != len(sorted_list2):
    max_len = max(len(sorted_list1), len(sorted_list2))
    sorted_list1.extend([0] * (max_len - len(sorted_list1)))
    sorted_list2.extend([0] * (max_len - len(sorted_list2)))

# Step 3: Compute the absolute normed distance
# Convert to numpy arrays for easier computation
array1 = np.array(sorted_list1)
array2 = np.array(sorted_list2)

# Absolute norm (L1 distance)
absolute_distance = np.sum(np.abs(array1 - array2))

# Normed distance (divide by the length of the lists)
normed_distance = absolute_distance 

#print("Sorted List 1:", sorted_list1)
#print("Sorted List 2:", sorted_list2)
print("Normed Absolute Distance:", normed_distance)

##part 2
occurences = np.array([list2.count(x) for x in list1 ])
similarity_score = np.sum(list1*occurences)
print(similarity_score )
