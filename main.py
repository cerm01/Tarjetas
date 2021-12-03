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


def main():
    pass


if __name__ == '__main__':
    main()