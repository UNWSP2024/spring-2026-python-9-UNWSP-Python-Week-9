# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_names(filename):
    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                if line.strip():  # Ignore empty lines
                    count += 1
            print(f"Total number of names in the file: {count}")
    except IOError:
        print("Error: The file could not be read.")

# Run the program
count_names("names.txt")


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
