# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def repeat_characters(input_str):
    result_str = ''.join([char * 2 for char in input_str])
    return result_str

user = input("Enter something: ")
result = repeat_characters(user)
print(result)


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

def expand_letter_range(letter_range):
    start, end = letter_range.split('-')
    expanded_range = ''.join(chr(i) for i in range(ord(start), ord(end) + 1))
    return expanded_range

# User input
user_input = input("Enter a letter range (e.g., 'a-z', 'h-o', 'Q-Z'): ")
result = expand_letter_range(user_input)
print("Result:", result)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# start, end = alphabet.split('-')
# user_range = input("Enter a range of letters (e.g., a-z): ")


