# def foo():
#     r = some_function()
#     if r == (-1):
#         return (-1)
#     #  do something
#     return r


# def bar():
#     r = foo()
#     if r == (-1):
#         print('Error')
#     else:
#         pass

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('except:', e)
# else:
#     print('no error')
# # finally語句不需要
# finally:
#     print('finally...')
# print('END')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()