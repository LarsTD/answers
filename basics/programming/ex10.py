print('Pick an operation')


operation = ''

while not operation:

    print('enter an valid operator')
    answer=input()

    if answer == '+':

        operation = '+'

    elif answer == '-':
        operation = '-'

print('enter your first number')

number_1 = int(input())

print('enter your second number')

number_2 = int(input())

if operation == '+':
    print(number_1 + number_2)

else:
    print(number_1 - number_2)

