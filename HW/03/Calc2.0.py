first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

try:
    first_value: int = int(first_value)
    second_value: int = int(second_value)
except ValueError:
    print('Not a digit')

if operation == '+':
    print(first_value + second_value)
elif operation == '-':
    print(first_value - second_value)
elif operation == '*':
    print(first_value * second_value)
elif operation == '**':
    print(first_value ** second_value)
elif operation == '/':
    try:
        print(first_value / second_value)
    except ZeroDivisionError:
        print('Error: Zero division')
elif operation == '//':
    try:
        print(first_value // second_value)
    except ZeroDivisionError:
        print('Error: Zero division')

else:
    print(f'Invalid operation {operation}')
