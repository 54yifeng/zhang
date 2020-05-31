#循环

# a = 1
# while a < 10:
#     print("哈哈哈哈")
#     a = a + 1

"""
现有10个学生的成绩，需要录入到系统中。
这10个人分别是。。。。。。
并且名字和成绩需要对应上，
而且大于60和小于60的需要分开放
"""
name = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","亚索"]
highscore = {}
lowscore = {}
i = 0
while i < len(name):
    score = int(input("请输入"+name[i]+"的成绩：" ))   #  "++"加号的作用是把数组拼接起来
        highscore[name[i]] = score
    else:
        lowscore[name[i]] = score
    i = i + 1
print(highscore)
print(lowscore)