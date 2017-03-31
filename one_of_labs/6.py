
def READ_LINE(f):
    s = list(f.readline().rstrip().split('\t-\t'))
    return s

Words = {}
dict = open('en-ru.txt', 'r')
s = READ_LINE(dict)

for line in dict:
    Words[s[0]] = s[1]
    s = READ_LINE(dict)

output = open('ru-en.txt', 'w')
ru_en = {Words[word]: word for word in Words}


print(ru_en)