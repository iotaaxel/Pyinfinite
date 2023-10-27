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
# Using built-in primitives
for idx in range(seq_length):
    res += ascii_values[idx % n]
    print(res)
