import sys
import re

password: str = input('Create your password \n')

if len(password) < 8:
    print('Password is too short! Password is required to be at least 8 symbols.')
    sys.exit(0)
elif not re.search("[A-Z]", password):
    print('Password is weak! Your password required to have at least 1 capital letter.')
    sys.exit(0)
elif not re.search("[a-z]", password):
    print('Password is weak! Your password is required to have at least 1 lowercase.')
    sys.exit(0)
elif not re.search("[0-9]", password):
    print('Password is weak! Your password is required to have at least 1 digit.')
    sys.exit(0)
else:
    print('Your password has been succesfully created!')