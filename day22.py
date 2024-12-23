from collections import defaultdict
from functools import cache
from itertools import pairwise

def mixing(value,secretNumber):
    return value^secretNumber
def pruning(value):
    return value%16777216

def generate_secret_number(x):
    s1 = pruning(mixing(64*x,x))
    s2 =pruning(mixing(int(s1/32),s1))

    return pruning(mixing(s2 * 2048,s2))
@cache
def iterate_secret_number(x, N):
    for _ in range(N):
        x = generate_secret_number(x)
    return x
    

def f(s):
    s ^= s << 6 & 0xFFFFFF
    s ^= s >> 5 & 0xFFFFFF
    return s ^ s << 11 & 0xFFFFFF

def compute_consecutive_change(value,N):
    l = [value] + [value := f(value) for _ in range(N)] #[iterate_secret_number(value,i) for i in range(N)]
    price = [int(str(x)[-1]) for x in l]
    consecutive_changes = [price[i+1]-price[i] for i in range(len(price)-1)]
    return l,price,consecutive_changes

ex = 123
N=10

#print(compute_consecutive_change(ex,N))

sample = [1,10,100,2024]
[iterate_secret_number(x,N) for x in sample]

filename = "day22.txt"
with open(filename ,'r') as file:
     secret_numbers_list = [int(line.strip()) for line in file if line.strip()]
#print(sum([iterate_secret_number(x,N) for x in secret_numbers_list]))

sample = [1,2,3,2024]
#results = [compute_consecutive_change(x,N) for x in sample]




def find_best_sequence(buyers,sequence_length=4, max_steps=2000):
    # Dictionary to store total bananas for each sequence
    sequence_totals = defaultdict(int)
    results = [compute_consecutive_change(x,max_steps) for x in buyers]
    ll_secrets_numbers = [x[0] for x in results]
    ll_prices = [x[1] for x in results]
    ll_changes= [x[2] for x in results]

    
    for i in range(len(buyers)):
        # Generate prices for the current buyer
        prices = ll_prices[i]

        # Calculate price changes
        changes = ll_changes[i]

        visited = set()
        # Track the first occurrence of each sequence
        for i in range(len(changes) - sequence_length + 1):
            sequence = tuple(changes[i:i + sequence_length])
            if sequence not in visited:
                sequence_totals[sequence] += prices[i + sequence_length]  # Add price at sell point
                visited.add(sequence)
    # Find the sequence with the highest total bananas
    #print(max(sequence_totals.values()))
    best_sequence =max(sequence_totals, key=sequence_totals.get)
    max_bananas = sequence_totals[best_sequence]

    return best_sequence, max_bananas



best_sequence, max_bananas = find_best_sequence(secret_numbers_list) #find_best_sequence(sample)
print("Best sequence:", best_sequence)
print("Max bananas:", max_bananas)

