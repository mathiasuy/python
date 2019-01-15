
print("datos de la primera persona")
#para cargar por teclado una cadena de caracteres utilizamos la función input
# las variables pueden tener muchas funcinoes, aqui tienes una que la utilizamos para almacenar el valor introducido por teclado
nombre1 = input("ingrese nombre del producto: ")
precio1 = float(input("ingrese el precio: "))
nombre2 = input("ingrese nombre del producto 2: ")
precio2 = float(input("ingrese el precio 2:"))
BONIFICACION = 20
"""
Comentarios de
más de una línea
"""
precio_total = (precio1 + precio2) #operador aritmético
comparar  = precio1 >= precio2 # operador de comparación
logico = (precio1 < precio2 and precio1 == precio2) #operador lógico
# concatenación de textos
cabecera = "resultados  del producto {0}. y del producto {1}.:"
print(cabecera.format(nombre1, nombre2))
print(comparar)
# concatenar se puede hacer de esta manera, con el signo + y en la variable la propiedad str
print("la suma de los dos productos es: " + str(precio_total))
print(logico)


#anidamiento
nota1  = int(input("Ingrese primer nota: "))
nota2 = int(input("Inrese segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
media = (nota1+ nota2+ nota3)/3

if media == 9 or media == 10:
    print("Sobresaliente")
elif media == 5:
    print("Suficiente")
elif media == 7 or media == 8:
    print("Regular/Bien")
else:
    #anidamiento
    if (media > 10):
        print("El promedio dió mayor a 10")
    else:
        print("Insuficiente")



########## BUCLE WHILE ##########

x = 1
suma = 0
while x <= 10:
    valor = int(input("Ingrese un valor: "))
    suma = suma + valor
    x = x + 1
promedio = suma/10
print("La suma de los 10 valores es: ")
print(suma)
print(promedio)




########## BUCLE FOR ##########

for x in range(20,31): #"Por cada x en el rango de 20 a 31 (se parece más a un foreach)"
    print(x)
    #SALIDA: 20....30 (el último no lo incluye)


#### LISTA ####
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']
for nombre in mi_lista:
    print(nombre)

####  TUPLA  ####
mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo')
for color in mi_tupla:
    print(color)