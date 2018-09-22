from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
# now = datetime.now()  # 獲取當前datetime
# print(now)
# print(type(now))

# 获取指定日期和时间
# dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期時間創建datetime
# print(dt)

# datetime转换为timestamp
# dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
# print(dt.timestamp())  # 把datetime转换为timestamp

# timestamp转换为datetime
# t = 1429417200.0
# print(datetime.fromtimestamp(t))

# timestamp也可以直接被转换到UTC标准时区的时间：
# t = 1429417200.0
# print(datetime.fromtimestamp(t))  # 本地時間
# print(datetime.utcfromtimestamp(t))  # UTC時間

# str转换为datetime
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
# now = datetime.now()
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
# print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
# tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
# print(dt)

# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)