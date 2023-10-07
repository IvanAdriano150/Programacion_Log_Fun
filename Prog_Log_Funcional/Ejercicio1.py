def recortar(lista,lista2):
    lista.pop()
    del lista[0]
    print(lista)
    print(Medio(lista2))
    return

def Medio(lista):
    return lista[1:-1]

print(recortar([33,4,5,6,77],[33,56,56,66,77,88]))