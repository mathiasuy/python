   ### LISTAS ###

Las listas pueden guardar cualquier tipo de elementos. 
Pueden ser todos del mismo tipo o combinados
'''
lista_de_enteros = [10, 11, 12]
lista_combinada = ["carlos", 10.2]
'''
Se puede ver la cantidad de elementos utilizando la función 'len'
'''
print(len(lista)) --> Imprime # elementos de 'lista'
'''

Mutación de listas.
Dada la lista _lista[2, 3, "carlos"]_
    Para cambiar un elemento de la lista: 
    '''
    lista[3] = "nuevo valor"
    '''
    Para agregar un nuevo valor al final de la lista se utiliza el operador _append()_: 
    '''
    lista.append(23)
    '''
    Para insertar un elemento en una posición determinada de la lista y deslpazar un lugar 
    el elemento que esté en esa posición se usa insert:
    '''
    lista.insert(2,76) #(Se inserta en la posición 2)
    '''
    Para eliminar el valor de una lista utilizar el operador _remove()_: 
    '''
    lista.remove(2)
    '''
    PAra buscar un valor de la lista usaremos el operador _in_ 23 in lista
    Para saber la posición de un valor en una lista usaremos _index()_:
    '''
    lista.index(3)
    '''
