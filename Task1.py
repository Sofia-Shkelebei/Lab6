# a) Print the contents by reading in the entire file
with open('learning_python.txt', 'r') as reader:
    print(reader.read())
print()

# b) Print the contents by looping over the file object
with open('learning_python.txt', 'r') as reader:
    for line in reader:
        print(line, end='')
print("\n")

# c) Print the contents by storing the lines in a list.
with open('learning_python.txt', 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        print(line, end='')
