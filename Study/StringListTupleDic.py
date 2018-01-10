# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 11:20
# @Author  : ZhaoMeifeng
# @Email   : Alisasmith@126.com
# @File    : StringListTupleDic.py
# @Software: PyCharm
import copy
# name = input("请输入你姓名：")
# age = int(input("请输入你的年龄："))
# print("你好%s,你今年%d, 你的工资是 %.2f" % (name, age, 30000.4598))
# ====================================字符串操作========================================
# name = input('请输入名字：')
# print(name.isalnum())  # 如果字符串的长度大于 0 ，并且所有字符都是字母或数字，则返回 True
# print(name.isalpha())  # 如果字符串的长度大于 0 ，并且所有字符都是字母，则返回 True
# print(name.isdigit())  # 如果字符串的长度大于 0 ，并且所有字符都是数字，则返回 True
# print(name.upper())  # 所有字母大写
# name1 = name.upper()
# print(name1.lower()) # 所有字母小写
# name2 = name.capitalize().center(40)  # capitalize，将首字母改为大写字母，并返回字符串 ；
#                                       # 空格补充字符串的长度，如果字符串的长度小于center传入的参数
# print(name2)
# print(name2.strip())
# print(name.split('cc'))
# print(name.title())
# print(name.find('l',0))
# print(name.center(10))
# print(name.swapcase())

# ===========================List===========================
a = [10,20,30,40,50,60,70,80,90]  # list声明并赋值
# print(id(a))
# 列表循环遍历
# for b in a:
#     print(b)
# a[2] = 33
# print(type(a))
# a.append(77) # 像列表的末尾添加一个元素
# print(a)
# a.pop(2) # list.pop([index])删除指定索引位置元素，不传的话，默认删除最后一个
# a.insert(2,333) # list.insert(index, ele) 把元素 ele 插入到指定的 index 位置。原来的元素会自动右移动

# 删除
# del a[1]
# del a[:2]
# del a[2:]
# del a[2:5]
# index = 0
# while index < len(a):
#     print(a[index])
#     index += 1


# 修改列表元素
# a[:2] = ["A", "B", "C"] # 修改列表索引为0,1,2的数值为 A,B,C
# index = 0
# while index < len(a):
#     print(a[index])
#     index += 1
#
# a[:] = [] # 清空列表
# print(len(a))

# 添加列表到原有列表中
# b = [11,22,33,44]
# print("b的内存："+str(id(b)))
# c = [55,66]
# a.extend(b)
# print(id(a))
# b+=c
# print("b的内存："+str(id(b)))
# d = [77,88]
# print(a)
# print(b)
# e = c+d
# e_new = e[:]
# print(e_new)
# names = ["小明", "小红", "小黑", ["粉色"], "小黄", "小白"]
# 深复制
# deep_names = copy.deepcopy(names)
# print(deep_names)
# 修改粉色为 Pink
# names[3][0] = "Pink"
# 分别打印输出两个列表
# print(names)
# print(deep_names)
# range 的使用方法
# num = list(range(10)) # python3中range()函数返回的是一个整数序列的对象，而不是列表，所以需要用list()函数返回列表
# print(type(num))
# 求一个列表的三次方
# num = []
# num = [pow(x,3) for x in range(10)]
# print(num)

# nums = []
# for x in range(10):
#     nums.append(pow(x,3))
# print(nums)
# nums = [pow(x, 2) for x in range(20) if x % 2 == 0]
# print(nums)

# 求奇数的平方
# nums = [pow(x, 2) for x in range(20) if x % 2==1]
# print(nums)

# for嵌套
# s1 = [1, 2, 3, 4, 5, 6]
# s2 = ['a', 'b', 'c']
# s3 = [str(x) + y for x in s1 for y in s2]
# print(s3)
# tuple 元组
# t = (12, 23, 34, 45, 56, 67)
# print(t[1])

# 创建字典的方式
# 1，使用{}创建;2.使用dict()函数传入键值序列创建字典;
# 3.当key值为简单字符串时，可以使用变量名=变量值创建

dict1 = {
    'name':'小花',
    'age':13,
    'sex':'girl'
}
dict2 = dict([('name', '小花'), ('age', 13), ('sex', 'girl')])

dict3 = dict(name = '小花', age = 18, sex = 'girl')
print(dict1)
print(dict2)
print(dict3)
# 练习 key是3-9的数字，value 是他的3次方,通过字典[索引] = 新值  来修改原字典的值
dict4 = {x:pow(x,3) for x in range(3, 10)}
print(dict4)
print(id(dict4))   # 打印输出dict4的内存id，来判定修改后的dict4是否是在原字典中修改
dict4[3] = 222222  # 根据key值修改value的值，如果key值存在就直接修改;如果key值不存在，就新增key:value
dict4[1] = 111111  #  key值为1的键不存在，则在字典中新增key为1，value为11111的字典
print(dict4)
print(id(dict4))   # 通过打印修改后的dict4的内存id，与之前创建的id相等说明是在原来的字典中修改
# for x in dict4:
#     print({x:dict4[x]})

tupleKey = ('你好', ' hello')
dict5 = {tupleKey:555}   # 用元组作为字典的key值
print(dict5)

print(10 in dict4.keys())   # 判断key为10的键是否存在于dict4中的key中
print(dict4.get(1))
del dict4[1]   # 删除索引为1 的元素
print(dict4)
keyDict4 = dict4.keys()  # 获取dict4的所有key值
print(keyDict4)

dict6 = {
    1:'haha',
    5:123,
    0:'lop',
    4:456
}
print(sorted(dict6)) # sorted(字典) 排序字典的key值
print(dict6.values()) # 获取dict6中所有的值
