import random

print("Password Generator")

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&'

number=int(input("How many passwords needed: "))
length=int(input("What should be the length of the passoword: "))

print("\n The following are the recommended passwords: ")

for pwd in range(number):
    password=""
    for i in range(length):
        password=password+random.choice(chars)
    print(password)