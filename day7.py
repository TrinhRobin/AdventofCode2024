import numpy as np
def parse_text_file_to_dict(file_path):
    """Reads a text file and converts it into a dictionary."""
    result_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            # Strip and split each line at the colon
            key, values = line.strip().split(':')
            
            # Convert the key to an integer and the values into a list of integers
            result_dict[int(key)] = list(map(int, values.split()))
    
    return result_dict

# Example usage
file_path = 'day7.txt'  # Replace with your file path
dictionary = parse_text_file_to_dict(file_path)
#print(dictionary)
def generate_all_combinations(l):
    results = []
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return ([l[0]+l[1],l[0]*l[1]])
    else:
        other=generate_all_combinations(l[1:])
        for combi in other:
            results.append(l[0]+combi )
            results.append(l[0]*combi )
    return results
for key in dictionary.keys():
    combinations_possibles = generate_all_combinations(list(reversed(dictionary[key])))
    #if key in combinations_possibles:
        #print("calibration result !", " :",key)
#print(np.sum(np.array([ key for key in dictionary.keys() if key in generate_all_combinations(list(reversed(dictionary[key])))])))


def concat_operator(a, b):
    """Custom concatenation operator that emulates '||'."""
    return int(str(a) + str(b))

def generate_all_combinations_part2(l):
    results = []
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return ([l[0]+l[1],l[0]*l[1], concat_operator(l[1],l[0])])
    else:
        other=generate_all_combinations_part2(l[1:])
        for combi in other:
            results.append(l[0]+combi )
            results.append(l[0]*combi )
            results.append(concat_operator(combi,l[0]))
    return results

file_path = 'day7.txt'  # Replace with your file path
dictionary = parse_text_file_to_dict(file_path)

for key in dictionary.keys():
   # print("Key",key)
    combinations_possibles = generate_all_combinations_part2( list(reversed(dictionary[key])))
   # print(combinations_possibles)
    if key in combinations_possibles:
        print("calibration result !", " :",key)
print(np.sum(np.array([ key for key in dictionary.keys() if key in generate_all_combinations_part2( list(reversed(dictionary[key])))])))