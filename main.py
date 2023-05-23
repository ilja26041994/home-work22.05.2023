# # 6.8.
# x = int(input('some edge number\n'))
# g=0
# cnt = 0
# while g < x:
#     cnt = cnt + 1
#     g = cnt ** 2
#     print('последовательность больше на одно число', g)
# #6.22
# z=0
# c=1
# x = int(input('input your number'))
# while x > 0:
#     g = x % 10
#     if g > 5:
#         z = z + g
#     if g > 7:
#         c = c*g
#     x = x // 10
# print(z)
# print(c)
# # 6.23 (а,в)
# cnt=0
# cnt1=0
# summ=0
# natureNumber = int(input('input some nature number\n'))
# a = int(input('some number 0<=a<=8\n'))
# if a >= 0 and a <= 8:
#     while natureNumber > 0:
#         num = natureNumber % 10
#         if num == a:
#             cnt = cnt + 1
#         if a < num:
#             summ = summ + num
#         natureNumber = natureNumber // 10
# print(summ)
# print('количество повторившихся а =', cnt)

# # 6.27 б
# min=10
# max=1
# g = 0
# z = 0
# x = int(input('some number\n'))
# while x > 0:
#     g = x % 10
#     if g < min:
#         min=g
#     z = x % 10
#     if z > max:
#         max = z
#
#     x = x // 10
#     result = max - min
# print('result =',result)
