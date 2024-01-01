
import sys


# for line in sys.stdin:
#     char_array = list(line.strip())
    
char_array = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k']
odd_chars = []
even_chars = []
for char_index, char in enumerate(char_array):
    if char_index % 2 == 0:
        even_chars.append(char)
    else:
        odd_chars.append(char)

grouped__odd_chars = []
for i in range(0, len(odd_chars), 3):
    group = ''.join(odd_chars[i:i+3])
    grouped__odd_chars.append(group)

grouped__even_chars = []
for i in range(0, len(even_chars), 3):
    group = ''.join(even_chars[i:i+3])
    grouped__even_chars.append(group)

string_odd_chars = " ".join(grouped__odd_chars)
string_even_chars = " ".join(grouped__even_chars)

print(string_even_chars)
print(string_odd_chars)
