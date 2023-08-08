import itertools

try:
    seq_length = int(input('Set the length to truncate the infinite sequence: '))
except ValueError:
    print('The provided value is not an integer')
        
input = 0
n = 5
res = 0
# Initial ascii: C - 67, l - 108, o - 111, s - 115, e - 101
# Adding ascii values of each letter gives C - 67, Cl - 175, Clo-286, Clos-401, Close-502
ascii_values = [67,108,111,115,101]

for idx in itertools.count(input):
    
    # switch case based on modulo of index (if using Python >=3.10)
    match idx % n:
        case 0: 
            res += ascii_values[0]
        case 1: 
            res += ascii_values[1]
        case 2: 
            res += ascii_values[2]
        case 3: 
            res += ascii_values[3]
        case 4: 
            res += ascii_values[4]
        case _:
            print('Unreachable case!') 

    if idx == seq_length:
        break
    
    print(res)
# ...