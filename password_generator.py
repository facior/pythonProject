import random
import string

password_length = int(input("How many characters do you want in your password? "))
number_of_passwords = int(input("How many passwords do you need? "))

def password_generator(password_length, number_of_passwords):
    passwords = []
    for i in range(number_of_passwords):
        password = ''.join(random.choices(string.printable, k = password_length))
        passwords.append(password)
    return passwords

passwords = password_generator(password_length, number_of_passwords)

with open("passwords.txt", "w") as file:
    for password in passwords:
        file.write(password + "\n")

print("Passwords have been saved to 'passwords.txt'")