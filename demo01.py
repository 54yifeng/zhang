"""
print("你好") #字符串
print(2333) #整数
print(2.333) #小数
print(True) #布尔值 True False
print(()) #元组
print([]) #数组
print({}) #字典

锄禾日当午
汗滴禾下土

print("哈哈",2333,2.333)
print("哈哈"+"嘻嘻") #字符串的拼接
print("哈哈"*100)
print(((1+2)*100-99)/2)
print(2<3)

#变量
#赋值
# a = float(input("请输入: "))
# b = float(input("请输入: "))
# print("input获取的内容: ",a+b)

#len()命令只支持：字符串、元组、数组、字典
a = input("请输入: ")
b = input("请输入: ")
print("input获取的内容: ",len(a+b))
print(a+b)
"""

# 数据格式的转换
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a = int(2333)
# print(type(a))

# b = str("哈哈哈")
# print(type(b))

# 元组,下标，从0开始编号
# a = (1,2,3,4,"哈哈","嘻嘻","哈哈",True,True,False)
# print(a[7])
# print(a[-3])  #负号从最后一位-1开始
# print(a.index(False))
# print(a.count("哈哈"))

# 切片
# print(a[0:4]) # 左闭右开
# print(a[4:6])
# print(a[6:8])

## 二维元组
# b = (a,8,9)
# print(b[0][3]) #a[3]

# 数组，元组写好后不可以修改，数组可以
# a = [1,2,3,4,"哈哈","嘻嘻","哈哈",True,False]
# print(a[6])
# a.append("nice")  #append的作用是往数组里追加数据，永远是在末尾
# print(a)
# a.insert(7,"insert")   # 插入到下标为0的位置
# print(a)
# b = a.pop(0) # 剪切
# c = a.pop(0)
# print(b+c)
# print(a)
# print(b)
# a.clear()  #清空

# xx = ["你好","好呀"]
#a.extend(xx)  # 可以插入一个数组
# print(a)  # 也可以用print(a+xx)

# a.remove(0)  #删除为0的值  pop可以剪切后赋值给其他，remove不行
# print(a)

# 下标不要超出范围=越界

"""
所有的方法都是用小括号结尾，比如：print(),input(),len()
元组、数组、字典的取值，都是用中括号，比如a[0]
元组、数组、字典的定义，分别是(),[],{}
"""

"""
字典的特点
1.字典中的值没有顺序
2.字典的结构必须是 键值对的结构，key:value  
3.字典的取值，是通过key去取这个value
"""
# a = {"name":"张三",0:"哈哈","age":25}

# #取值
# print(a["name"])
# #新增
# a["high"] = "182cm"
# print(a)
# #修改
# a["name"] = "李四"
# print(a)


# b = a.get("name")   # get:取值
# print(b) 
# print(a)
# b = a.pop("name")   #pop：剪切
# print(b)
# print(a)

# a.update(name=1111)  # update：新增或修改
# print(a)

# print("-----------------")

# print(a.get("name"))
# print(a["name"])


# #数组和字典的删除
# del a["name"]
# print(a)

# a = [1,2,3,4,5]
# del a[3]
# print(a)

# 练习：获取用户输入的个人信息，并存储到字典中
# 个人信息包括了，name,age,sex.
a = {"name":input("姓名: "),"age":input("年龄: "),"sex":input("性别: ")}
print(a)