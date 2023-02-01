# Imports go at the top
from microbit import *

listaletras = ["a", "e", "i", "o", "u"]

i = 0
while(i < len(listaletras)):
    display.show(listaletras[i])
    i = i + 1
    sleep(1000)
