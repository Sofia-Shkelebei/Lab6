# Guest Book: Write a while loop that prompts users for their name.
with open('guest_book.txt', 'w') as writer:
    name = ""
    while name != "X":
        name = input("Enter you name (to stop enter 'X'): ")
        if name != "X":
            print(f"Hello {name}! Thank you for visiting!")
            writer.write(name + '\n')

