def Introducir_Lista(lista):
     Ordenar(lista.split(','))

def Ordenar(Lista):
     Lista.sort()
     Eliminar_Repetidos(Lista,0)
    
def Eliminar_Repetidos(ListaRepe,x):
     if(x+1!=len(ListaRepe)):
        if(ListaRepe[x]==ListaRepe[x+1]): Eliminar_Repetidos(Elimininra(ListaRepe,x),x)
        else: Eliminar_Repetidos(ListaRepe,x+1)
     else: print(ListaRepe)

def Elimininra(Lista,index):
     del Lista[index]
     return Lista

Introducir_Lista(input('Introducir Lista ---> '))