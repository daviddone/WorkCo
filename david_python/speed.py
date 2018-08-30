import datetime
import time

f = open("speed.txt",encoding="utf-8")
startTime = 0
endTime = 0
total = 0
for item in f:
    if item.startswith("startTime"):
        startTimeStr = item.split("#")[-1].strip()
        startTime = int(time.mktime(time.strptime(startTimeStr, '%Y-%m-%d %H:%M:%S.%f')))
        print(startTime)
    if item.startswith("endTime"):
        endTimeStr = item.split("#")[-1].strip()
        endTime = int(time.mktime(time.strptime(endTimeStr, '%Y-%m-%d %H:%M:%S.%f')))
        print(endTime)
    if item.startswith("total"):
        totalStr = item.split("#")[-1].strip()
        total = int(totalStr)
spendTime = int(endTime)-int(startTime)
print("耗时：结束时间：%s 开始时间：%s 耗时: %.1f "%(endTimeStr,startTimeStr,spendTime/60))  # 格式化 保留小数点后一位
result = total/spendTime
print("速度:%d /s  %0.1f K"%(result,result/1000))
print("总数:%d"%(total))