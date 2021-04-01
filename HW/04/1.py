file = open('HW.txt', 'r')
print(file.read())
file.close()

#___

with open('HW.txt') as file, open('newHW.txt', 'w') as new_file:
    new_file.write(file.read())

#___

file = open('HW.txt', 'r+')
data = file.read()
file.write('_'.join(data.split(' ')))
file.close()




