'''
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

'''

#### LISTA ####
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']
for nombre in mi_lista:
    print(nombre)

####  TUPLA  ####
mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo')
for color in mi_tupla:
    print(color)

    ### LISTAS ###
"""
Las listas pueden guardar cualquier tipo de elementos. 
Pueden ser todos del mismo tipo o combinados

lista_de_enteros = [10, 11, 12]
lista_combinada = ["carlos", 10.2]

Se puede ver la cantidad de elementos utilizando la función 'len'
print(len(lista)) --> Imprime # elementos de 'lista'

Mutación de listas.
Dada la lista lista[2, 3, "carlos"]
    Para cambiar un elemento de la lista: lista[3] = "nuevo valor"
    Para agregar un nuevo valor al final de la lista se utiliza el operador append(): lista.append(23)
    Para insertar un elemento en una posición determinada de la lista y deslpazar un lugar 
    el elemento que esté en esa posición se usa insert:
    lista.insert(2,76) (Se inserta en la posición 2)
    Para eliminar el valor de una lista utilizar el operador remove(): lista.remove(2)
    PAra buscar un valor de la lista usaremos el operador 'in'_ 23 in lista
    Para saber la posición de un valor en una lista usaremos 'index()':
    lista.index(3)


"""

