L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
# 前10個數，每兩個取一個
print('R[:10:2] =', R[:10:2])
# 每5個數取一個
print('R[::5] =', R[::5])