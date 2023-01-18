from microbit import *
n = 1
borde = Image("99999:90109:90009:99999:")
interior = Image("00000:09990:09990:00000")
while n <= 10:
    if n %2 == 0:
        display.show(borde)
    else:
        display.show(interior)
    n=n+1
    sleep(500)
    n += 1
display.scroll("FIN")
        
