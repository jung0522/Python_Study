import datetime
# (1)
d = datetime.date.today()
print(d)
# (2)
print(d.strftime("%Y년 %m월 %d일 요일: %A"))
# (3)
currentTime = datetime.datetime.today()
currentTime.strftime("%H시 %M분 %S초")
