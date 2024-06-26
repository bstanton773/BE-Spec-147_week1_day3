# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)

def solution(string): # O(1 + n * (1 + 1 + 1) + n * (1 + 1) + 1)
    letter_count = {} # O(1)
    for letter in string: # O(n)
        if letter in letter_count: # O(1)
            letter_count[letter] += 1 # O(1)
        else:
            letter_count[letter] = 1 # O(1)
    for letter in string: # O(n)
        if letter_count[letter] == 1: # O(1)
            return letter # O(1)
    return None # O(1)
# O(1 + n * (1 + 1 + 1) + n * (1 + 1) + 1)
# O(5n + 2)
# O(n)

def solution(string):
    letter_count = {}
    for letter in string:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    for letter in string:
        if letter_count[letter] == 1:
            return letter
    return None

def solution(string): # O(n**2)
    for char in string: # O(n)
        if string.count(char) == 1: # O(n)
            return char
    return None