#   while循环，只要条件满足，就不断循环，条件不满足时退出循环
#   计算100以内所有奇数之和
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# sum = 0
# n = 1
# while n < 100:
#     sum = sum + n
#     n = n + 2
# print(sum)
#
# #   break提前退出循环
# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('END')

#   continue語句跳出某些循環
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)