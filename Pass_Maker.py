import random
char = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+0|"
password = ""
print("Character : " , char)
length = int(input("Pass length : "))
while len(password) != length:
    password = password + random.choice(char)
    if len(password) == length:
        print("Password is = {}".format (password))
