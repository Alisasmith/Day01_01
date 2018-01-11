# @Time    : 2018/1/8 15:33
# @Author  : ZhaoMeifeng
# @Email   : Alisasmith@126.com
# @File    : Test.py
# @Software: PyCharm
import re
name = '赵美丰'
age = 18
sex = '女'
phoneNum = 12345678901
high = '165cm'
weight = '55kg'

# print("姓名："+name+"\n年龄："+str(age)+"\n性别："+sex+"\n电话："+str(phoneNum)+"\n身高："+high+"\n体重："+weight)

# print(" 姓名:%s\n 年龄:%d\n 性别:%s\n 电话:%d\n 身高:%s\n 体重:%s"%(name, age,sex, phoneNum,high,weight))
# 字符串格式化
'''
%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
%e    指数 (基底写为e)
%E    指数 (基底写为E)
%f    浮点数
%F    浮点数，与上相同
%g    指数(e)或浮点数 (根据显示长度)
%G    指数(E)或浮点数 (根据显示长度)
%%    字符"%"
'''

# 字符串练习
# 练习1：声明字符串
s = '浮点数，与上相同'
s1 = "指数(基底写为e)"
# 练习2：获取字符串的长度,并拼接字符串
# print("s的长度为："+str(len(s)) + "，s1的字符串长度为："+ str(len(s1)))
# 练习3：获取练习1中指定的字符
# print("指定索引为3的字符为："+s[3])
# 练习4：拼接字符串

# print("字符串 (采用str()的显示)\n"*5)
# print(((s+",,,"+s1)+"\n")*5)

# ===========Day02_test=========
# 1.从键盘上读取信息：一行内显示。信息之间使用-分隔。

# ss = input('请输入您的身份信息：')
# list_ss = ss.split(",")
# for str_list_ss in list_ss:
#     a = 0
#     while a < 5:
#         if a < 4:
#             print(str_list_ss, end='-')
#             a += 1
#         elif a == 4:
#             print(str_list_ss)
#             break
    # print(str_list_ss)

# a = 0
# while a < 5:
#     if a < 4:
#         print(str_list_ss, end='-')
#         a += 1
#     elif a == 4:
#         print(str_list_ss, end="")
#         break


# 课堂练习
'''
4 / 3
4 // 3
4 % 3
2 / 3
2 // 3
2 % 3
6 / 2
6 //2
6 %2 
5 // 4
5 % 4
4 / 5
4 % 5
3 / 1
3 % 1
'''
# print(4 / 3,
# 4 // 3,
# 4 % 3,
# 2 / 3,
# 2 // 3,
# 2 % 3,
# 6 / 2,
# 6 //2,
# 6 %2,
# 5 // 4,
# 5 % 4,
# 4 / 5,
# 4 % 5,
# 3 / 1,
# 3 % 1)


# sss = input('请输入任意数字：')
# int_sss = list(sss)
# if sss.isdigit():
#     a = 0
#     while a < len(int_sss):
#         print(int_sss[a])
#         a += 1
# else:
#     print('您输入的数字不合法，请重新输入')
# a = 4
# b = 3
# res1 = (a + b ) < (a // b)
# res2 = (a ** b) != (a * b)
# res3 = (a * False) < (b % -1)
# print(res1, res2, res3)
# 练习1：判断给定的成绩是否及格：[0, 60]
# 练习2：给定的成绩是否是良好：[80,89]
# 练习3：给定的成绩是否优秀：[90,100]
# 练习4：键盘输入王二狗的年龄，判断是否可以结婚：25。[0,150]，
# score = input('请输入你的成绩（0-100）：')
# int_score = int(score)
# if 0 <= int_score <= 100:
#     if 60 <= int_score <80:
#         print('您的成绩及格，继续努力哦！')
#     if 80 <=int_score <=89:
#         print('您的成绩良好，加油更进一步！')
#     if 90<= int_score <=100:
#         print('您的成绩优秀哦，请继续保持！')
#     if 0 <= int_score <=59:
#         print('您的成绩弱爆了，还是申请退学吧！！！')
# else:
#     print('您输入的成绩不合法，请重新输入！！！')

# age_test = input('输入您的年龄哦，来看您是否符合结婚要求（0-150）：')
# int_age = int(age_test)
# if 0 <= int_age <= 150:
#     if  int_age >=25:
#         print('小伙，恭喜你，已通过了婚姻法法定年龄！！！')
#     if int_age < 25:
#         print('别太着急了，再等几年哦！！！')
# else:
#     print('您输入的年龄不合法，请问您是外星人吗！！！')
# a = 3
# b = 2
#
# res1 = a * 2 > a % b and a // b != a // a   # False
# res2 = a * b % a < b or (a + 3) // 2 < b    # True
# res3 = b // a != a ** 1 and a % b <= b % a and b < a   # True
# res4 = b // a != a ** 1 or a % b <= b % a or b < a   # True
#
# print(res1, res2, res3, res4)
# 每满100-20




