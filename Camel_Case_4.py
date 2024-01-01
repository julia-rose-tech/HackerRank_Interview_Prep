
import sys

# Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar). Your task is to write a program that creates or splits Camel Case variable, method, and class names.

# Sample Input

    # S;M;plasticCup()

    # C;V;mobile phone

    # C;C;coffee machine

    # S;C;LargeSoftwareBook

    # C;M;white sheet of paperS;M;plasticCup()

    # S;V;pictureFrame

# Sample Output

    # plastic cup

    # mobilePhone

    # CoffeeMachine

    # large software book

    # whiteSheetOfPaper()

    # picture frame

def split_operation(variableType, inputName):
    if variableType == 'M':
        split_name = ''.join([' ' + char if char.isupper() else char for char in inputName if char not in {'(', ')'}]).lower()
    elif variableType == 'C' or variableType == 'V':
        split_name = ''.join([' ' + char if char.isupper() else char for char in inputName]).lower().lstrip()
    else:
        split_name = ''
    return split_name

def combine_operation(variableType, inputName):
    words = inputName.split()
    if variableType == 'V':
        capitalise_words = [words[0]] + [word.title() for word in words[1:]]
        combined_name = ''.join(capitalise_words)
    elif variableType == 'M':
        capitalise_words = [words[0]] + [word.title() for word in words[1:]]
        combined_name = ''.join(capitalise_words)
        add_brackets = '()'
        combined_name += add_brackets
    elif variableType == 'C':
        capitalise_words = [word.title() for word in words]
        combined_name = ''.join(capitalise_words)
    else:
        combined_name = ''
    return combined_name


for line in sys.stdin:
    inputs = line.strip().split(';')
    
    operation = inputs[0]
    variableType = inputs[1]
    inputName = inputs[2]
    if operation == 'S':
        result = split_operation(variableType, inputName)
    elif operation == 'C':
        result = combine_operation(variableType, inputName)
    print(result)