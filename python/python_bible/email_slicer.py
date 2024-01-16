# get user email address
email = input("What is your email address?: ").strip()

# slice out username - bobdoe@thing.com
user = email[:email.index("@")]

# slice domain name
domain = email[email.index("@") + 1:]

# format message
output = "Your username is {} and your domain name is {}".format(user, domain)

# display output message
print(output)
print(f"f-string: Your username is {user} and your domain name is {domain}.")
