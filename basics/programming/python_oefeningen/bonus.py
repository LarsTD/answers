'''A calculator which calculates with +, -, * and /. (plus, minus, times and division)'''

print('Pick an operation')

'''Operation = '' means that when i type an operator, it will use that exact operator'''
operation = ''

'''while not operation: is an command that will go in an endless loop until you enter an valid operator.'''
while not operation:

    print('enter an valid operator')
    answer=input()

    # if answer == '+': means that if you enter an + the script will recognise that you want to add the two numbers you put in. 

    if answer == '+':

        operation = '+'

       # if answer == '*': means that if you enter an * the script will recognise that you want to multiply the two numbers you put in.
    if answer == '*':

        operation = '*'

        # if answer == '-': means that if you enter an - the script will recognise that you want to subtract the second from the first number put in.
    if answer == '-':
        operation = '-'

        # if answer == '/': means that if you enter an / the script will recognise that you want to divide the second from the first number put in.
    if answer == '/':
        operation = '/'

        # print'enter your first number'. this will ask you to enter a first number.
print('enter your first number')

        # number_1 = int input. the number you typed.
number_1 = int(input())

        # print 'enter your second number'. this will ask you to enter a second number
print('enter your second number')

        # number_2 = int input. the second number you typed and int means that you can only enter a number.
number_2 = int(input())

        # if operation == '+': print number_1 + number_2 means that if you entered + for an operator it will add the two numbers you chose together.
if operation == '+':
    print(number_1 + number_2)

        # if operation == '*': print number_1 * number_2 means that if you entered * for an operator it will multiply the two numbers you chose.
elif operation == '*':
    print(number_1 * number_2)

        # if operation ++ '*': print number_1 / number_2 means that if you entered / for an operator it will divide the two numbers you chose.
elif operation == '/':
    print(number_1 / number_2)

        # elif operation == '-': print number_1 - number_2 means that if you entered something else than +, * and /. it will subtract the second from the firstnumber

elif operation == '-':
    print(number_1 - number_2)

