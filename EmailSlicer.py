email = input("What is you email: ").strip()

userName = email[: email.index("@")]

domain = email[email.index("@") + 1:]

output = "The username is '{}' and the domain is '{}'".format(userName, domain)
print(output)