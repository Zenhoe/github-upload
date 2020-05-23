import random

char = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'


length = int(input("What do want your password length to be: "))
loop = int(input("How many passwords do you want: "))
for i in range(loop):
        password = ''
        for c in range(length):
            password += random.choice(char)
        print(password)