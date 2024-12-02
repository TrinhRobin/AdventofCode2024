from utils import load_data
from itertools import combinations
day2_puzzle = load_data("day2.txt")
print(day2_puzzle[:10])

##part 1
def safe_combination_element1(x:int,y:int)->bool:
    return x<y and abs(x-y)>=1 and abs(x-y)<=3
def safe_combination_element2(x:int,y:int)->bool:
    return x>y and abs(x-y)>=1 and abs(x-y)<=3

def safe_combination_list(l:list):
    return all(safe_combination_element1(l[i], l[i+1]) for i in range(len(l) - 1)) or all(safe_combination_element2(l[i], l[i+1]) for i in range(len(l) - 1))

def count_safe_combinations(l:list)->dict:
    return {'Safe':l.count(True),
            'Unsafe': l.count(False)}

part1_solution = [safe_combination_list(l) for l in day2_puzzle]

##part 2

def remove_one_element(l):
    if safe_combination_list(l):
        return True
    for i in range(len(l)):
        liste_remove = l[:i] + l[i+1 :]
        if safe_combination_list(liste_remove):
            return True
    return False

def safe_subset_list(l):
    if safe_combination_list(l):
        return True
    for liste in list(combinations(l, len(l)-1)):
        if safe_combination_list(liste):
            return True
    return False

part2_solution = [safe_subset_list(l) for l in day2_puzzle]

if __name__=="__main__":
    print(count_safe_combinations(part1_solution))
    print(count_safe_combinations(part2_solution))