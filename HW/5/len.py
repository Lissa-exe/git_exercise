from collections import Counter

text = input('Input some text \n')

text = Counter(text.split(' '))
print(text.most_common(n=1))

print(max(text, key=len))