# Task: Open a file and calculate the total number of lines, words, and characters.

# Instructions:
# - get the file name from the user
# - Read the file contents.
# - Count how many lines, words, and characters are in the file.
# - Print out the totals for each.

# Get the file name from the user


file_name = input("Enter the name of the file to analyze (including extension): ")

try:
    # Open the file and read its contents
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Count the total lines, words, and characters
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    # Print the results
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")

except FileNotFoundError:
    print("The specified file was not found. Please check the file name and try again.")
