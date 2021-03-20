import sys
import re

email: str = input('Input email \n')

if '@' not in email:
    raise TypeError('Invalid: "@" is not in email!')
elif '.' not in email:
    raise TypeError('Invalid: "." is not in email!')
at_sign_index = email.index('@')
for sign in {'.', '@'}:
    if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
        raise NameError('Invalid: incorrect first or last symbol!')
    elif email[-1] == sign or email[0] == sign:
        print('Invalid')
        sys.exit(0)

password: str = input('Create your password \n')

if len(password) < 8:
    raise SyntaxError('Password is too short! Password is required to be at least 8 symbols.')
elif not re.search("[A-Z]", password):
    raise SyntaxError('Password is weak! Your password required to have at least 1 capital letter.')
elif not re.search("[a-z]", password):
    raise SyntaxError('Password is weak! Your password is required to have at least 1 lowercase.')
elif not re.search("[0-9]", password):
    raise SyntaxError('Password is weak! Your password is required to have at least 1 digit.')


else:
    print('Your account has been succesfully created!')

