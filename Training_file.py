value: str = input('Do you have a pet? \n')

if value == 'Yes':
    print('So cute! Me too :)')

elif value == 'No':
    print(':(')

elif value.isdigit():
    print('Wow, how much!')

else:
    print('Incorrect answer. Please, try again.')
