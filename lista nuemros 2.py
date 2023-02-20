# Imports go at the top
from microbit import *

lista_numeros = [3, 4, 2, 4, 2]
tptal = 0
for i in lista_numeros:
    total = total + i

display.scroll(total)
