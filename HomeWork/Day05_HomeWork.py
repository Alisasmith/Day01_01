# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 18:29
# @Author  : ZhaoMeifeng
# @Email   : Alisasmith@126.com
# @File    : Day05_HomeWork.py
# @Software: PyCharm
"""
1.str1 = "hello hello hello world"
    统计字符串的长度:
    统计"llo"出现的次数:
    统计"wor"出现的位置:
"""
# str1 = "hello hello hello world"
# print('该字符串的长度为：%d'% len(str1))
# print('llo出现的次数为：%d'%str1.count('llo'))
# print('wor出现的位置%d：'%str1.find('wor'))
# 2.str2 = "hello"，将字符串长度-->11，左右两边使用-填充
# str2 = "hello"

# print('将字符填充完成后的结果为：%s'% str2.center(11, '-'))
# 3.给定一个以下字符串：统计大写字母的个数，小写字母的个数，非字母的个数。多种算法完成。
# str3 = "ajdkkKDKEK1343KFKiriromfkfKKRIOWJF0928398jjee11djdDJJRH"
# count_upper = count_lower = count_alpha = 0
# for x in str3:
#     if x.isupper():
#         count_upper += 1
#     elif x.islower():
#         count_lower += 1
#     else:
#         count_alpha += 1
# print('大写字母的个数为%d，小写字母的个数为：%d，非字母个数为：%d'%(count_upper, count_lower, count_alpha))
#  3：给定一个路径名：
#  String pathName="http://192.168.10.1:8080/Day33_Servlet/aa.jpeg"; 获取文件名称：aa.jpeg
# pathName="http://192.168.10.1:8080/Day33_Servlet/aa.jpeg"
# list_path = pathName.split('/')
# for x in list_path:
#     if 'aa' in x:
#         print(x)
# 4.给定字符串：str="sunjavaandroidjavajavasejavaeejavamec#java.netjavaphpjava",
# 编写程序，统计字符串"java"出现的次数。多种算法。
# str4 ="sunjavaandroidjavajavasejavaeejavamec#java.netjavaphpjava"
# 方法一：
# TODO:方法二实现
# num_str4_1 = str4.count("java")
# print(num_str4_1)

# 5.字符串str="ABCDEFGHIJK"，要求输出最少一个最多八个的所有组合（向后连续字母）
str5 = "ABCDEFGHIJK"
# for x in str5:
#     for b in range(1, 9):
#
#         print(x)
'''
public static void showCombination(){
        String str = "ABCDEFGHIJK";
        for(int i=0; i<str.length(); i++){
            for(int j=i; j<(i+8 > str.length() ? str.length() : i+8); j++){
                System.out.print(str.substring(i, j+1));
                System.out.println();
            }
            System.out.println();
'''
# TODO:未实现
# a = 0
# list_num = []
# while a < len(str5):
#     b = a
#     while b <=8 :
#         if len(str5) - a>8:
#             str_str5 = str5[a:b]
#             print(str_str5)
#         # elif len(str5) - a <8:
#         #     str_str_str5 = str5[a:a-b]
#         #     print(str_str_str5)
#         b +=1
#     a += 1
# print(list_num)