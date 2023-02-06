import random
import string

while True:
    try:
        password_length = int(input("How many characters do you want in your password? "))
        if password_length <= 0:
            print("Please enter a positive integer for the password length.")
        elif password_length >= 2147483647:
            print("Please enter a positive integer less than 2147483647.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

while True:
    try:
        number_of_passwords = int(input("How many passwords do you need? "))
        if number_of_passwords <= 0:
            print("Please enter a positive integer for the number of passwords.")
        elif number_of_passwords >= 2147483647:
            print("Please enter a positive integer less than 2147483647.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")


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