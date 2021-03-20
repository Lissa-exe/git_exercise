import sys

first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

try:
    first_value = int(first_value)
    second_value = int(second_value)
except ValueError:
    print('Not a digit')
    sys.exit(1)

try:
    first_value / second_value or first_value // second_value
except ZeroDivisionError:
    print('Error: Zero division')
    sys.exit(1)

if operation == '+':
    print(first_value + second_value)
elif operation == '-':
    print(first_value - second_value)
elif operation == '*':
    print(first_value * second_value)
elif operation == '**':
    print(first_value ** second_value)

else:
    print(f'Invalid operation {operation}')