# 用print()把可能有问题的变量打印出来
# def foo(s):
#     n = int(s)
#     print('>>>n = %d' % n)
#     return 10/n
#
#
# def main():
#     foo('0')
#
# main()


# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


def main():
    foo('0')