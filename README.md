# LISTAS

Las listas pueden guardar cualquier tipo de elementos. 
Pueden ser todos del mismo tipo o combinados
```
lista_de_enteros = [10, 11, 12]
lista_combinada = ["carlos", 10.2]
```

Se puede ver la cantidad de elementos utilizando la función 'len'
```
print(len(lista)) --> Imprime # elementos de 'lista'
```

## Mutación de listas.

Dada la lista _lista[2, 3, "carlos"]_
    
    Para cambiar un elemento de la lista: 
    ```
    lista[3] = "nuevo valor"
    ```
    
    Para agregar un nuevo valor al final de la lista se utiliza el operador _append()_: 
    ```
    lista.append(23)
    ```
    
    Para insertar un elemento en una posición determinada de la lista y deslpazar un lugar 
    el elemento que esté en esa posición se usa insert:
    ```
    lista.insert(2,76) #(Se inserta en la posición 2)
    ```
    
    Para eliminar el valor de una lista utilizar el operador _remove()_: 
    ```
    lista.remove(2)
    ```

    PAra buscar un valor de la lista usaremos el operador _in_ 23 in lista
    Para saber la posición de un valor en una lista usaremos _index()_:
    ```
    lista.index(3)
    ```

#FUNCIONES

```
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

```