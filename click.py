# contar las veces que se pulsa elboton a
# en 13 segundos
from microbit import *
sleep(13000)
display.scroll(button_a.get_presses())
