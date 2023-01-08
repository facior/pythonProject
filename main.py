first_number1 = int(input("Write first number "))
second_number1 = int(input("Write second number "))
action1 = input("Choose action (*,/,+,-)")
def select_action(first_number1, second_number1, action1):
    if action1 == '*':
        print('Your score is ' + str(first_number1*second_number1))
    elif action1 == '/':
        print('Your score is ' + str(first_number1/second_number1))
    elif action1 == '+':
        print('Your score is ' + str(first_number1+second_number1))
    elif action1 == '-':
        print('Your score is ' + str(first_number1-second_number1))

select_action(first_number1, second_number1, action1)

