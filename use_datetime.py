from datetime import datetime

# 获取当前时间
now = datetime.now()
print(now)
# 构建制定日期与时间
dt = datetime(1993, 10, 16, 8, 18)
print(dt)
# datetime转换为timestamp
st = dt.timestamp()
print(st)
# 把timestamp转换为datetime
t = 1429417200.0
dt1 = datetime.fromtimestamp(t)  # 本地时间
print(dt1)
dt2 = datetime.utcfromtimestamp(t)  # UTC时间
print(dt2)