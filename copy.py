# Task: Create an exact copy of a file by reading its content and writing it to a new file.

# Instructions:
# - get the file name from the user
# - Open the original file and read its content.
# - Create a new file, and write the same content into it - the output file should be the input file name + _copy.txt
# e.g. story.txt -> story.txt_copy.txt

# Tip: Consider which file modes will let you read and write text data.


# Get the file name from the user
file_name = input("Enter the name of the file to copy (including extension): ")

# Try to open the original file and copy its content
try:
    with open(file_name, 'r') as original_file:  # Open the original file in read mode
        content = original_file.read()  # Read the content of the file

    # Create a new file with the format "original_file_name_copy.txt"
    output_file_name = file_name.replace('.txt', '_copy.txt')  # Generate the output file name
    with open(output_file_name, 'w') as copy_file:  # Open the new file in write mode
        copy_file.write(content)  # Write the content into the new file

    print(f"The file has been successfully copied as {output_file_name}.")  # Inform the user of success
except FileNotFoundError:
    print("The specified file was not found. Please check the file name and try again.")  # Error message if file is missing


