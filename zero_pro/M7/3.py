# import time
#
#
# for x in range(0,5):
#     print("Hello World")
#     time.sleep(5)
#
#Adapte o programa acima para celular o tempo de prosessamento do
#script: Utilize time.time() e perf_counter() para apresentar a variação no tempo

import time
from time import perf_counter

# for x in range(0,5):
#     print("Hello World")
#     time.sleep(5)

tempo_zero = perf_counter()

for x in range(0,5):
    print("Hello World")
    time.sleep(5)

tempo_stop = perf_counter()

print("Tempo decorrido para rodar o programa(em segundos): ", tempo_zero+tempo_stop)
