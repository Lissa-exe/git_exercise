def converter(string, delimiter):
    result = {}
    words_list = string.split(delimiter)
    for i in set(words_list):
        result.setdefault(i, words_list.count(i))

    return result


string = 'qqq q q q w w  e r t y y y u i oo o p'

print(converter(string, ' '))