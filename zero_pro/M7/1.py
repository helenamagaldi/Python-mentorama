# 1.

# Escreva scripts para mostrar os diversos formatos de tempo conforme se segue:
# a.Impressão da época padrão
# b. Segundos que se passaram desde a época
# c. Imprime dados do tempo no momento atual
# d. Cria um objeto time.localtime() e imprime o valor das horas, minutos e segundos
# e. Imprime se no momento atual estamos em horário de verão ou não


import time

# #a
# print(time.gmtime(0))
#
# #b
# seconds = time.time()
# print("Desde então transcorreram", seconds, "segundos")
#
# #c
# time_now = time.asctime()
# print("Local time: ", time_now)
#
# #d
# print(time.localtime())
#
# #e
daylight_saving = time.localtime()
print(time.localtime[-1])

if time.localtime()[-1] == 0:
    print("Não estamos no horário de verão")
elif time.localtime()[-1] == 1:
    print("Estamos no horário de verão")
else:
    print("Não sabemos se estamos ou não no horário de verão")

