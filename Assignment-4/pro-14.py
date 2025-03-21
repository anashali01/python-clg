#Write a function that counts the occurrences of a specific character in a string.
def word_counter(s, char):
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count = count + 1
    return count

# Get input from user
input_string = input("Enter a string: ")
search_char = input("Enter the character to count: ")

# Print the result
result = word_counter(input_string, search_char)
print(f"The character '{search_char}' appears {result} times in '{input_string}'")