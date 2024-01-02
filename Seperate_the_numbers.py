# Input string
s = "99100"

# Function to extract the next splice of a specified length from the remaining array
def get_next_splice(remaining_array, length):
    """
    Get the next splice of a specified length from the remaining array.

    Args:
    remaining_array (str): The remaining part of the input string.
    length (int): The desired length of the splice.

    Returns:
    str: The next splice of the specified length.
    """
    next_splice = remaining_array[0:length]
    return next_splice 

# Initialize control flags and variables
outer_loop_break = False  # Control flag for the outer for loop
is_beautiful = False  # Flag to indicate if a beautiful sequence is found

# Iterate through potential first numbers of the beautiful sequence
for i in range(1, len(s) // 2 + 1):
    first_number = s[:i]  # Initialize the first number
    previous_number = first_number  # Initialize the previous number
    remaining_array = s[i:]  # Initialize the remaining part of the input string
    
    # Iterate through the remaining parts to check for beautiful sequences
    while len(remaining_array) > 0:
        next_number = int(previous_number) + 1
        length_next_number = len(str(next_number))
        next_splice = get_next_splice(remaining_array, length_next_number)
        
        # Check if the next splice matches the expected next number
        if int(next_splice) != int(next_number):
            break
        else: 
            previous_number = next_splice
            remaining_array = remaining_array[length_next_number:]
            
            # Check if the remaining part is empty, indicating a beautiful sequence
            if len(str(remaining_array)) == 0:
                is_beautiful = True
                outer_loop_break = True
                break
    
    # Break the outer loop if a beautiful sequence is found
    if outer_loop_break:
        break

# Print the result
if is_beautiful:
    print("YES " + str(first_number))
else:
    print("NO")

