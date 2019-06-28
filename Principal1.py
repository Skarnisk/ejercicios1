from cuadrado import *
from circulo import *
from cadenaInver import *


base = int(input("introduzca la base  "))
altura = int(input("introduzca la altura  "))

matriz1 = rectangulo(base, altura)# esto es un OBJETO
print("El area del rectangulo es: ", matriz1.Area())


radio= int(input("Introduzca el radio para calcular el area del circulo y el perimetro del circulo   "))
pi=3.14

Objeto1= Circulo(radio,pi)# OBJETO
print(Objeto1.areac())
print(Objeto1.perimetro())


frase= str(input("Introduzca la frase para darle la vuelta :  "))
Frase = invertido(frase)# esto es un OBJETO
print(Frase.reves())