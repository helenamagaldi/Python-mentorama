# maximum = 10
# even_Sum = 0
# odd_Sum = 0

# num = 1
# while (num<=maximum):
#     if (num%2==0):
#         even_Sum=even_Sum+num
#     else:
#         odd_Sum=odd_Sum+num
#     num+=1

# print("Sum of Odd numbers: ", odd_Sum)
# print("Sum of even numbers: ", even_Sum)




# max=int(input("please enter the maximum value: "))
# even_Sum=0
# odd_Sum=0
# num=1
# while (num<=max):
# #     if (num%2==0):
# #         even_Sum=even_Sum+num
# #     else:
# #         odd_Sum=odd_Sum+num
# #     num+=1
# # print("The sum of Even numbers 1 to entered number", even_Sum)
# # print("The sum of Even numbers 1 to entered number", odd_Sum)


# # start, end = 1,10

# # for odd in range(start, end +1):
# #     if odd % 2 != 0:
# #         add = sum(odd)
# #         print(add)
# #         print(odd)
    
# # for even in range(start,end +1):
# #     if even % 2 == 0:
# #         print(even)

# # num = 10
# # s = sum(range(1,num+1,2))

# # print(s)



# # start, end = 1,10

# # for odd in range(start, end +1):
# #     if odd % 2 != 0:
# #         print(odd)
# # s = sum(range(1,end+1,2))
# # print(s)
    
# # for even in range(start,end):
# #     if even % 2 == 0:
# #         print(even)
# # k = sum(range(start,end[::2]))
# # print(k)

# # n = int(input()) 
# # sum = 0 
# # for i in range(0, n): 
# # 	if(i % 2 == 0): 
# # 		sum += i 
# # print(sum)

# # s = sum(range(1,end+1)[::2])
# # print(s)

# # BHASKARA: (-b +- raiz de (-b - 4ac))/2a

# import math

# a = int(input("Digite a: "))
# b = int(input("Digite b: "))
# c = int(input("Digite c: "))

# x = (b**2)-(4*a*c)

# if x>0:
#     x=math.sqrt(x)
#     x1=(-b+x)/2*a
#     x2=(-b-x)/2*a
# else:
#     print("Impossível de realizar a conta")
#     exit()


# print(x1, x2)

###### MISSING
# def equation():
#     a = input("Digite a: ")
#     b = input("Digite b: ")
#     c = input("Digite c: ")

#     delta=(b**2)-(4*a*c)
    
#     x1 = (-b + delta ** (1 / 2)) / (2 * a)
#     x2 = (-b - delta ** (1 / 2)) / (2 * a)

#     print(x1)
#     print(x2)

# equation()

# s = 'Mentorauheoiaama'

# print(s.upper())

# my_string = input("Digite a sua palavra: ")
# vowel = set("aeiouAEIOU")

# for i in my_string:
#     if i in vowel:
#         print(i)

# s = input("Digite a sua string")
# a = s[::-1]
# print(a)




# print("You have an equation ax^2 +bx+c = 0")
# a=float(input("a ="))
# b=float(input("b ="))
# c=float(input("c ="))

# if a==0:
#   print("What the what?? This is not a quadratic equation.")
#   b=0
#   c=0
#   a=1

# x1=(-b+sqrt(b**2-4*a*c))/(2*a)
# x2=(-b-sqrt(b**2-4*a*c))/(2*a)


# print("x1 = "+str(x1))
# print("x2 = "+str(x2))

# def Bhaskara():
#     a = int(input('Digite um valor para A '))
#     b = int(input('Digite um valor para B '))
#     c = int(input('Digute um valor para C '))
#     delta = (b ** 2) - (4 * a * c)
#     x1 = (-b + delta ** (1 / 2)) / (2 * a)
#     x2 = (-b - delta ** (1 / 2)) / (2 * a)
#     print('X1 = {}'.format(x1))
#     print('X2 = {}'.format(x2))
#     print(type(x1))    # Verificação do tipo da variável    

# if __name__ in '__main__':
#     Bhaskara()

# def equation():
#     a = int(input('Digite A '))
#     b = int(input('Digite B '))
#     c = int(input('Digite C '))
#     delta = (b ** 2) - (4 * a * c)
#     x1 = (-b + delta ** (1 / 2)) / (2 * a)
#     x2 = (-b - delta ** (1 / 2)) / (2 * a)
#     print('X1 = {}'.format(x1))
#     print('X2 = {}'.format(x2))
#     print(type(x1))    # Verificação do tipo da variável    

# if __name__ in '__main__':
#     equation()

import math

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))

x = (b**2)-(4*a*c)

if x<0:
    print("Impossível de realizar a conta")
    exit()
else: 
    x=math.sqrt(x)
    x1=(-b+x)/2*a
    x2=(-b-x)/2*a

print(x1, x2)
