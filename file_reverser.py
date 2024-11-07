# Task: Reverse the text on each line of a file and save it to a new file.

# Instructions:
# - get the file name from the user
# - Open the original file and read each line.
# - Reverse the text of each line word by word -> 'hello my name is george' -> 'george is name my hello'
# - Write the reversed lines into a new file - the output file name should be the input filename + _reverse.txt
# for example: 'story.txt' -> 'story.txt_reverse.txt'

# Get the file name from the user
file_name = input("Enter the name of the file to reverse (including extension): ")

# Try to open the original file and reverse its content
try:
    with open(file_name, 'r') as original_file:
        lines = original_file.readlines()  # Read all lines from the file

    # Generate the output file name by appending '_reverse.txt' to the original file name
    output_file_name = file_name.replace('.txt', '_reverse.txt')
    
    with open(output_file_name, 'w') as reversed_file:
        for line in lines:
            # Remove any trailing newline, split the line into words, reverse the word order, and join them back
            reversed_line = ' '.join(line.strip().split()[::-1])
            reversed_file.write(reversed_line + '\n')  # Write the reversed line to the new file

    print(f"The file has been successfully reversed and saved as {output_file_name}.")
except FileNotFoundError:
    print("The specified file was not found. Please check the file name and try again.")

