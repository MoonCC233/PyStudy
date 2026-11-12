# 求200以内能被17整除的最大整数
for i in range(200,0,-1):
    if i%17 == 0:
        print(i)
        break

# 1-100求和
sum = 0
for i in range(1,101):
    sum += i
print(sum)

# 1-100中找奇数偶数
for i in range(1,101):
    if i % 2 == 0:
        print(i,"是偶数")
    else:
        print(i,"是奇数")

# if的成绩等级判断
score = float(input("请输入你的成绩："))
if 90 < score <= 100:
    print("优秀")
elif 80 < score <= 90:
    print("良好")
elif 60 <= score <= 80:
    print("及格")
else:
    print("不及格")