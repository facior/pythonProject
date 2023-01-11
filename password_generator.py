import random
import string

password_lenght = int(input("How long you want your password to be ? "))
many_password = int(input("How many password you need ? "))
def password_generator(password_lenght):
    return ''.join(
        random.choices(
            string.ascii_letters + string.ascii_uppercase + string.digits + string.punctuation, k= password_lenght
        )
    )

print(password_generator(password_lenght))