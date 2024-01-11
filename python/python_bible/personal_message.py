# use a variable to represent a person's name, and print a message to that person.
# Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"
#
name = input("What is your name?: ")
# remove whitespaces if any
name = name.strip()
# capitalize first letter of each name, i.e. Anne-Marie, if not already
name = name.title()

print(f"Hello {name}, would you like to learn some Python today?")
