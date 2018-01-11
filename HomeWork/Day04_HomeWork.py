# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 17:32
# @Author  : ZhaoMeifeng
# @Email   : Alisasmith@126.com
# @File    : Day04_HomeWork.py
# @Software: PyCharm
import random
# 3.操场上有一群人，人数在100到200之间。三人一组多1人，四人一组多2人，五人一组多3人。
# 问操场上共有多少人。(118,178)
# num_person = 100
# while num_person <= 200:
#     if num_person % 3 == 1 and num_person % 4 == 2 and num_person % 5==3:
#         print(num_person)
#     num_person += 1
# 4.两个自然数x，y相除，商3余10，被除数，除数，商，余数的和是163，求被除数，除数
# x = 10
# while x <= 163:
#     y = 3
#     while y <= 160:
#         if x//y == 3 and x%y == 10 and x+y==150:
#             print(x, y)
#         y += 1
#     x += 1
# 5.一个四位数，恰好等于去掉它的首位数字之后所剩的三位数的3倍，这个四位数是多少。
# a = 1000
# while a <= 9999:
#     s = a%1000
#     if s*3==a:
#         print(a)
#     a += 1
# 6. 打印出1-500所有的自然数中不包含4的自然数，共有多少个
# TODO:用其他方式实现
# a = 1
# a_count = 0
# while a<=5:
#     b = 0
#     while b <= 9:
#         c = 0
#         while c <= 9:
#             if a != 4 and b!=4 and c !=4:
#                 s= a*100 + b*10 +c
#                 print(s)
#                 a_count += 1
#             c += 1
#         b += 1
#
#     a += 1
#     print('不包含4的数字的个数为%d：'% a_count)
#  7.某数学竞赛中，参赛人数大约在380-450之间。
#  比赛结果，全体考生的总平均分为76分，男生的平均分为75，女生的平均分为80.1，求男女生各有多少人。
# TODO:未实现
# a = 380
# while a <= 450:
#
#
#     a += 1

# 8.有一个两位数，如果在它的前面添加一个3，可以得到一个三位数，
# 把3添加在它的后面，也可以得到一个三位数。这两个三位数相差468，求原来的两位数。
# a = 1
# while a<9:
#     b = 0
#     while b<=9:
#         s = a*10 + b
#         ss = abs((a*100+b*10+3)-(300+s))
#         if ss ==468:
#             print(ss)
#             print(s)
#         b+=1
#     a += 1
# 9.打印乘法表
# a = 1
# while a <= 9:
#     b=1
#     while b <=a:
#         s = a*b
#         print("%d * %d = %d"%(b,a,s),end='\t')
#         b+=1
#     print()
#     a+=1
'''
10：			    行	空格	星星	换行
    *			1	4	1	1
   ***			2	3	3	1
  *****			3	2	5	1
 *******		4	1	7	1
*********		5	0	9	1
 *******		1	1	7	1
  *****			2	2	5	1
   ***			3	3	3	1
    *			4	4	1	1
'''
# a = 0  # 控制行数
# b = 0  # 控制空格数，以及*的个数
# while a <= 5:
#     while b < 5:
#         b += 1
#         print(' ' * (5-b), '*' * (b*2-1))
#     a += 1
# c = 1
# d = 0
# while c < 5:
#     while d<4:
#         d += 1
#         print(' '*d, '*'*(9-2*d))
#     c+=1
'''

       *
      ***
     *****
    *******
   *********
     *****
    *******
   *********
  ***********
 *************
***************
     *****
     *****
     *****
     *****
'''
# TODO:未实现
'''
11.某电话公司电话收费有3个套餐
	A.月租50元，包100分钟，超出100分钟，1元/分，200元封顶。(含月租)
	B.月租50元，包100分钟，超出100分钟，0.85元/分，不封顶
	C.无月租，0.75元/分，不封顶。
根据用户输入的通话时长，为用户推荐最优惠的套餐。
'''
# minute_input = int(input("请输入您的月通话分钟数，选择最适合您的套餐："))
# # sub_minute = minute_input-100 # 超出部分的通话时长
# if minute_input > 100:
#     sub_minute = minute_input - 100  # 超出部分的通话时长
#     moneyA = 50 + sub_minute*1 #A套餐超出100分钟后的总金额
#     moneyB = 50 + sub_minute*0.85 # B套餐的消费总额
#     moneyC = sub_minute*0.75 # C套餐的消费总额
#     print(moneyA,moneyB,moneyC)
#     if moneyA > moneyB>moneyC>200:
#             print('请选择A套餐，A.B.C三种套餐的消费总额分别为：%d，%d，%d'%(200,moneyB,moneyC))
#     else:
#         if moneyA > moneyB:
#             if moneyB >moneyC:
#                 if moneyA >=200:
#                     moneyA=200
#                     print('请选择C种套餐套餐消费为%d，A.B.C三种套餐的消费总额分别为：%d，%d，%d'%(moneyC,moneyA,moneyB,moneyC))
#         elif moneyB > moneyC:
#                 print('请选择C种套餐套餐消费为%d，A.B.C三种套餐的消费总额分别为：%d，%d，%d' % (moneyC, moneyA, moneyB, moneyC))
# elif minute_input < 100:# TODO:判断条件
#     else_c = minute_input * 0.75
#     if else_c > 50:
#         print('选择A或B套餐:您选择C套餐的消费为：%d'% else_c)
#     else:
#         print('请选择C套餐的消费为%d,您选择A/B套餐的最低消费为50'% else_c)
# else:
#     else_c = minute_input*0.75
#     print('请选择A/B套餐,您选C套餐的消费为%d，而A、B套餐的消费为50'% else_c)

# minute = 100
# minute_b=minute_input-minute # A套餐与B套餐超出部分
# if minute_input > 100: # TODO:判断条件
#     moneyA = 50 + 1*minute_b
#     if moneyA
#     print('....')
# elif minute_input < 100:# TODO:判断条件
#     else_c = minute_input * 0.75
#     if else_c > 50:
#         print('选择A或B套餐:您选择C套餐的消费为：%d'% else_c)
#     else:
#         print('请选择C套餐的消费为%d,您选择A/B套餐的最低消费为50'% else_c)
# else:
#     else_c = minute_input*0.75
#     print('请选择A/B套餐,您选C套餐的消费为%d，而A、B套餐的消费为50'% else_c)
'''
12.游戏：剪刀石头布
系统和玩家
    系统，产生随机数：1,2,3-->剪刀，石头，布
    玩家：由键盘输入：1,2,3-->剪刀，石头，布
'''
sys_num = random.randint(1,3)
print(sys_num)
int_input = int(input('请输入1.剪刀,2.石头,3.布'))
while True:
    if sys_num == int_input :
        print('平局，请继续。。。')
    else:
        if sys_num > int_input:
            if sys_num ==1:
                print('系统赢')
        else:
            print('玩家赢')

    break