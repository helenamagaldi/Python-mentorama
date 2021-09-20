### 1) Escreva um programa em Python para contar de 1 até 10. 

# 1a - usando a instrução while 
i = 0

while i<10:
    i += 1
    print(i)

# 1b - usando a instrução for e a função range 
for i in range(1,11):
    print(i)

### 2) Escreva um programa para contar quantos números pares e ímpares existentes entre 1 e 10 bem como a soma deles. 

# 2a - usando a instrução while
maximum = 10
even_Sum = 0
odd_Sum = 0

num = 1
while (num<=maximum):
    if (num%2==0):
        even_Sum=even_Sum+num
    else:
        odd_Sum=odd_Sum+num
    num+=1

print("Sum of Odd numbers: ", odd_Sum)
print("Sum of even numbers: ", even_Sum)



# 2b - usando a instrução for e as funções range e sum 
start, end = 1,10

for odd in range(start, end +1):
    if odd % 2 != 0:
        print(odd)
s = sum(range(1,end+1)[::2])
print(s)
    
for even in range(start,end):
    if even % 2 == 0:
        print(even)
k = sum(range(0,11)[::2])
print(k)

### 3) Escreva um programa para resolver equações do segundo grau representadas por ax2+bx+c usando a Fórmula de Bhaskara. 

# 3a - a) sem usar o módulo math 
def equation():
    a = int(input('Digite A '))
    b = int(input('Digite B '))
    c = int(input('Digite C '))
    delta = (b ** 2) - (4 * a * c)
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print('X1 = {}'.format(x1))
    print('X2 = {}'.format(x2))
    print(type(x1))    # Verificação do tipo da variável    

if __name__ in '__main__':
    equation()

## TESTE 1 QUESTÃO 3A a=1,b=-5,c=6 
# Digite A 1
# Digite B -5
# Digite C 6
# X1 = 3.0
# X2 = 2.0
## TESTE 2 QUESTÃO 3A a=1,b=0,c=-9 
# Digite A 1
# Digite B 0
# Digite C -9
# X1 = 3.0
# X2 = -3.0
## TESTE 3 QUESTÃO 3A a=5,b=-45,c=0 
# Digite A 5
# Digite B -45
# Digite C 0
# X1 = 9.0
# X2 = 0.0
## TESTE 4 QUESTÃO 3A a=1,b=-1,c=-12 
# Digite A 1
# Digite B 1
# Digite C -12
# X1 = 3.0
# X2 = -4.0
## TESTE 5 QUESTÃO 3A a=1,b=-6,c=10 
# Digite A 1
# Digite B -6
# Digite C 10
# X1 = (3+1j)
# X2 = (3-1j)

# 3B

# 3b) usando o módulo math 

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

## TESTE 1 QUESTÃO 3B a=1,b=-5,c=6 
# Digite a: 1
# Digite b: -5
# Digite c: 6
# 3.0 2.0
## TESTE 2 QUESTÃO 3B a=1,b=0,c=-9
# Digite a: 1
# Digite b: 0
# Digite c: -9
# 3.0 -3.0
## TESTE 3 QUESTÃO 3B a=5,b=-45,c=0 
# Digite a: 5
# Digite b: -45
# Digite c: 0
# 9.0 0.0
## TESTE 4 QUESTÃO 3B a=1,b=-1,c=-12 
# Digite a: 1
# Digite b: -1
# Digite c: -12
# 4.0 -3.0
## TESTE 5 QUESTÃO 3B a=1,b=-6,c=10 
# Impossível de realizar a conta (complex number)


### 4) Reescreva o programa acima criando uma função bhaskara que recebe como parâmetros os coeficientes a, b e c e retorna as raízes da equação.  

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


### 5) Considerando a string s = 'Mentorama' escreva um programa que: 

#5a - converta a string para maiúsculo, em seguida 

s = 'Mentorama'
print(s.upper())

# 5b) imprima-a de trás para frente 

s = input("Digite a sua string")
a = s[::-1]
print(a)

# 5c) imprima somente as vogais

my_string = input("Digite a sua palavra: ")
vowel = set("aeiouAEIOU")

for i in my_string:
    if i in vowel:
        print(i)