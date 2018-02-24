from io import StringIO

# f = StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# print(f.write('world!'))
# print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())