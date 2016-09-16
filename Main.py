import USB,Teclado


teclado1 = Teclado.Teclado('/dev/input/event2')
c = teclado1.scanf()
print(c)