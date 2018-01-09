# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 11:52
# @Author  : ZhaoMeifeng
# @Email   : Alisasmith@126.com
# @File    : HelloWorld.py
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
t = (12, 23, 34, 45, 56, 67)

print(t[1])

d = dict([('one', 1), ('two', 2), ('three', 3)])

d['one'] = 1111111
print(d['one'])



