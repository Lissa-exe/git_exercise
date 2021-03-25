file = open('HW.txt', 'r')
print(file.read())
file.close()

#___

file = open('HW.txt', 'r').read()
new_file = open('newHW.txt', 'w')
new_file.write(file)
new_file.close()

#___

file = open('HW.txt', 'a')
file.write(' Nice to meet you.')
file.close()




