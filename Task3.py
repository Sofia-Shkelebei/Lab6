# Program analyzes a file to determine the number of lines, words, and characters contained therein.
def wc(filename):
    lines = 0
    words = 0
    characters = 0

    with open(filename, 'r') as reader:
        for line in reader:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters


file_name = input('Enter file name: ')
lines, words, characters = wc(file_name)
print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)





