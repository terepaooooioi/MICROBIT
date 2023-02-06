# Imports go at the top
from microbit import *

lst_numeros = [1,2,4,5,6]
lst_palabras = ["rojo", "amarillo", "verde"]
i = 0
while True:
    if button_a.was_pressed():
        i = i + 1
    elif button_b.was_pressed():
        i = i - 1

    display.scroll(lst_palabras[i])
