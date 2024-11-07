# Get the original file name
file_name = "example.txt"  # replace with the actual file name or ask for user input

try:
    # Initialize counters
    line_count = 0
    word_count = 0
    char_count = 0
    
    # Open the file and process each line
    with open(file_name, 'r') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)
    
    # Print the totals
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
