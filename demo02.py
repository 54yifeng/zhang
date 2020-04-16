# 判断
# a = 3
# b = 4 
# if a > b:    #必须有冒号
#     print("a比b大")   #前面有四个空格
# else:
#     print("b更大")


age = int(input("请输入年龄："))

# if age > 60:
#     print("退休")
# elif age > 30:
#     print("赚钱养家")
# elif age >20:
#     print("规划好未来")
# else:
#     print("好好学习")

# if age >20 and age <= 30:
#     print("22222222")
# elif age > 30 and age <= 40:
#     print("33333333")
# elif age > 40 and age <= 50:
#     print("44444444")
# else:
#     print("55555555")
 

# a = "漂亮"
# if a in "你好漂亮":    #或者用["你好","美女"]
#     print("嘻嘻")
# else:
#     print("NO")

#可以用来判断类型
# a = input("请输入: ")
# if a =="":
#     print("不能为空!")
#     exit()
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄! ")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("小")

a = "adjkhnfl"
if type(a) is int:
    print("是数字")
elif  type(a) is str:
    print("是字符")
else:
    print("其他")