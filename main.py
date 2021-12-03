"""
Creamos una funcion read que nos permita leer "archivo.in" dicho archivo
tiene en la primer linea el numero n de tarjetas y las siguientes n lineas
los los valores de las tarjetas.
La función read recibe como parametro el nombre del archivo y devuelve una lista
con los valores de las tarjetas.
"""
def read(archivo):
    lista_tarjetas = []
    with open(archivo, "r", encoding="utf-8") as archivo:
        n = int(archivo.readline())
        for i in range(n):
            lista_tarjetas.append(int(archivo.readline()))
    return lista_tarjetas

"""
Esta funcion recorre la lista y en cada iteracion un elemento de la lista sera el 
pivote, y se ordenara por la izquierda y/o por la derecha. mediante funciones que se declaran abajo."""
def recorrido(lista_tarjetas):
    pass

"""
Esta funcion recorre la lista desde el inicio de la lista hasta el pivote asignando -1 los
elementos que son mayores que el pivote para "eliminarlos"
"""
def ordenar_izquierda(lista_tarjetas, pivote):
    pass


"""
Esta funcion recorre la lista desde el final de la lista hasta el pivote asignando y del 
pivote hasta el final asignando -1 a los elementos que son menores que el pivote para
"eliminarlos".
"""
def ordenar_derecha(lista_tarjetas, pivote):


def main():
    pass


if __name__ == '__main__':
    main()