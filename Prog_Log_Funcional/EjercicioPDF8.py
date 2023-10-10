def Ingresar_Lista(Lista):
    Calcular_Media(Lista,0,len(Lista),Lista)
    Calcular_Moda(Lista,0,0,0,0,0,0,0,0,0,0,0)
    

def Calcular_Media(Lista,sum,tot,L):
    if(len(Lista)!=0): Calcular_Media(Lista[1:],sum+Lista[0],tot,L)
    else:
        print('Media Aritmetica ---> ',round((sum/tot),2))
        Calcular_Varianza(round((sum/tot),2),tot,L,[])


def Calcular_Varianza(Valor_Medio,tot,Lista,dif):
    if(len(Lista)!=0): dif.append((Valor_Medio-Lista[0])*(Valor_Medio-Lista[0])), Calcular_Varianza(Valor_Medio,tot,Lista[1:],dif)
    else: 
        Sumar_Lista(dif,0,tot)

def Sumar_Lista(Lista,sum,tot):
    if(len(Lista)!=0): Sumar_Lista(Lista[1:],sum+Lista[0],tot)
    else: 
        print('Varianza --- > ',round((sum/tot-1),2))
        print('Desviacion Estandar -----> ',round((round((sum/tot-1),2)**0.5),2))

def Calcular_Moda(Lista,C,I,II,III,IV,V,VI,VII,VIII,IX,X):
    if(len(Lista)!=0):
        if(Lista[0]==0):Calcular_Moda(Lista[1:],C+1,I,II,III,IV,V,VI,VII,VIII,IX,X)
        if(Lista[0]==1):Calcular_Moda(Lista[1:],C,I+1,II,III,IV,V,VI,VII,VIII,IX,X)
        if(Lista[0]==2):Calcular_Moda(Lista[1:],C,I,II+1,III,IV,V,VI,VII,VIII,IX,X)
        if(Lista[0]==3):Calcular_Moda(Lista[1:],C,I,II,III+1,IV,V,VI,VII,VIII,IX,X)
        if(Lista[0]==4):Calcular_Moda(Lista[1:],C,I,II,III,IV+1,V,VI,VII,VIII,IX,X)
        if(Lista[0]==5):Calcular_Moda(Lista[1:],C,I,II,III,IV,V+1,VI,VII,VIII,IX,X)
        if(Lista[0]==6):Calcular_Moda(Lista[1:],C,I,II,III,IV,V,VI+1,VII,VIII,IX,X)
        if(Lista[0]==7):Calcular_Moda(Lista[1:],C,I,II,III,IV,V,VI,VII+1,VIII,IX,X)
        if(Lista[0]==8):Calcular_Moda(Lista[1:],C,I,II,III,IV,V,VI,VII,VIII+1,IX,X)
        if(Lista[0]==9):Calcular_Moda(Lista[1:],C,I,II,III,IV,V,VI,VII,VIII,IX+1,X)
        if(Lista[0]==10):Calcular_Moda(Lista[1:],C,I,II,III,IV,V,VI,VII,VIII,IX,X+1)
    else:
        Dividir(Crear_Tuplas([(C,'0'),(I,'1'),(II,'2'),(III,'3'),(IV,'4'),(V,'5'),(VI,'6'),(VII,'7'),(VIII,'8'),(IX,'9'),(X,'10')]))

def Crear_Tuplas(tuplas):
    tuplas.sort()
    return tuplas[-1]

def Dividir(Tuplita):
    print('Moda ---- > ',Tuplita[1])

Ingresar_Lista([5,5,5,6,7,8,10,10,8,9,8,7,6,5,10,9,8,10,10,10,10,10,10,10,10,9,7,8,7,5,6,7,8,9,10,5,6,7,6,5,6,7,6,5,4,3,4,5,6,7,8,9,10])