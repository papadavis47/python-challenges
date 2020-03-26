# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def alphabetize(string):
    result = ""
    alpha = sorted(list(string.lower()))
    for letter in alpha:
        result += letter
    return result

print(alphabetize("supercalifragilisticexpialidocious"))