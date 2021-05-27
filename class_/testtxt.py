f = open('log.txt', 'r+', encoding='utf-8')

f.write('test3\n')
print(f.readlines())