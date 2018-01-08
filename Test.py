# @Time    : 2018/1/8 15:33
# @Author  : ZhaoMeifeng
# @Email   : Alisasmith@126.com
# @File    : Test.py
# @Software: PyCharm

name = '赵美丰'
age = 18
sex = '女'
phoneNum = 12345678901
high = '165cm'
weight = '55kg'

# print("姓名："+name+"\n年龄："+str(age)+"\n性别："+sex+"\n电话："+str(phoneNum)+"\n身高："+high+"\n体重："+weight)

print(" 姓名:%s\n 年龄:%d\n 性别:%s\n 电话:%d\n 身高:%s\n 体重:%s"%(name, age,sex, phoneNum,high,weight))
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
print("s的长度为："+str(len(s)) + "，s1的字符串长度为："+ str(len(s1)))
# 练习3：获取练习1中指定的字符
print("指定索引为3的字符为："+s[3])
# 练习4：拼接字符串

# print("字符串 (采用str()的显示)\n"*5)
print(((s+",,,"+s1)+"\n")*5)