def nombreFuncion():
    global numero1
    global numero2 #variables de acceso global
    numero1 = int(input("Ingrese el primer valor: "))
    numero2 = int(input("Ingrese el segnundo valor: "))

def sumar():
   print("La suma es: " + str(numero1 + numero2))

nombreFuncion()
sumar()

def funcionConPArametros(nombre, apellido):
   datosCompletos = nombre.apellido
   print(datosCompletos)

# Parámetros por omisión
def funcion(nombre, apellido="Blanco"):
   print(nombre, apellido)

funcion(apellido="Gomez", nombre="Carlos")

# Parámetros arbitrarios
def funcionArbitrarios(parametroFijo, *arbitrarios):
   print(parametroFijo)
   # Los parámetros arbitrarios se recorren como tupla
   for parametro in arbitrarios:
      print(parametro)

funcionArbitrarios("fijo", "arbitrario1", "arbitrario2", "arbitrario1")

"""
Los arbitrarios deben suceder a los fijos
Es posible obtener parámetros como pares de clave=valor, elnombre del 
parámetro debe preceder a los signos **
"""
def funcionParesArbitrarios(parametroFijo, **arbitrarios):
   print(parametroFijo)
   # Los parámetros arbitrarios se recorren como tupla:
   for clave in arbitrarios:
      print("el valor", clave, "es", arbitrarios[clave])

funcionParesArbitrarios("Fijo", clave1="arbitrario1", clave2="arbitrario2", clave3="arbitrario3")


# Función suma
def sumarlos(v1, v2, *lista):
    suma = v1 + v2
    for x in range(len(lista)):
        suma = suma+lista[x]
    return suma

def mayor(lista):
    may = lista[0]
    for x in range(1,len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may

def menor(lista):
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men

listaValores = [10 , 56, 26, 32]
print("Lista completa: ")
print(listaValores)
print("Suma de los elementos: ", sumarlos(10,56,26,32))
print("El mayor es: " , mayor(listaValores))
print("El menor es: " , menor(listaValores))