import time

# 获取当前13位毫秒时间戳
now_13ts = int(time.time() * 1000)
print("当前13位时间戳:", now_13ts, end='\r')