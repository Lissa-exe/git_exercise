file_name = input('Enter file name \n')

if '.' not in file_name:
    raise ValueError('There is no such type of file')
if file_name[-1] == '.':
    raise ValueError('Invalid type of file')
if file_name[0] == '.':
    raise ValueError('Invalid type of file')
print(file_name.split('.')[-1])

