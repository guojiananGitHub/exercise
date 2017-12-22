#   if特點是自上往下
height = 1.75
weight = 80.5
bmi = weight/(height**2)
if bmi < 18.5:
    print('過輕')
elif bmi >= 18.5:
    print('正常')
elif bmi >= 28:
    print('肥胖')
else:
    print('嚴重肥胖')