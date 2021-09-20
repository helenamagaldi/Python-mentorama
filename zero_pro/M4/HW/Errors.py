#!/usr/bin/env python
# coding: utf-8

# Questão 1

# In[23]:


listin = ["200.135.80.9", "192.168.1.1", "8.35.67.74", "257.32.4.5", "85.345.1.2", "1.2.3.4", "9.8.234.5", "192.168.0.256"]
my_file = open("list.txt", "w")
file_valid_list = []

for element in listin:
    my_file.write(element + "\n")

content = open("my_file.txt", "a")
valid_element = ["200.135.80.9", "192.168.1.1", "8.35.67.74", "1.2.3.4"]
new_valid_list = []
new_nonvalid_list = []


for index, sList in enumerate(listin):
    if sList in valid_element:
        new_valid_list.append(listin[index])
    else:
        new_nonvalid_list.append(listin[index])
        
        
for val in valid_element:
    if val in new_list:
            print("'Endereços válidos: ", new_valid_list)
            print("'Endereços inválidos: ", new_nonvalid_list)
        


# Questão 2

# a) Erro de sintaxe: problemas com a estrutura e com as regras sobre essa estrutura (i.e. esquecer ";" ou outros itens, como "()"). 
# b) Erro de execução (runtime errors): são também conhecidos como erros de exceção - ocorrem em situações excepcionais (i.e.: divisão por 0).
# c) Erros de Semântica: são erros de lógica. O programa roda, mas gera problemas com o resultado esperado. 

# Questão 3

# In[ ]:


# 1a

i = 0

while i<10:
    i += "hello"
    print(i)
    
########

i = 0

for i<10:
    i += 1
    print(i)
    
######

i = 0

for i<10:
    i = 1
    print(i)    


# In[24]:


# 2a

maximum = int(input("Pick a number between 10 and 20"))
even_Sum = 0
odd_Sum = 0

num = 1
while (num<=maximum):
    try:
        if (num%2==0):
            even_Sum=even_Sum+num
        else:
            odd_Sum=odd_Sum+num
        num =1
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        
print("Sum of Odd numbers: ", odd_Sum)
print("Sum of even numbers: ", even_Sum)

####

maximum = 10
even_Sum = 0
odd_Sum = 0

num = 1
while (num<=maximum)
    if (num%2==0):
        even_Sum=even_Sum+num
    else:
        odd_Sum=odd_Sum+num
    num+=1

print("Sum of Odd numbers: ", odd_Sum)
print("Sum of even numbers: ", even_Sum)


# In[ ]:





# 
