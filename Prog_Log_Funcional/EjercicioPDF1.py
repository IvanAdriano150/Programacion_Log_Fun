def Ingresar_Lista_Enteros(LE):
    Ingresar_entero(input('Ingresar Entero---> '),LE.split(','),0)

def Ingresar_entero(entero,LE,suma):
    if(len(LE)==0):
        print('Se repite --> ',suma,' veces')
    else:
       if(entero==LE[0]):
          Ingresar_entero(entero,LE[1:],Sumador(suma))
       else: 
          
          Ingresar_entero(entero,LE[1:],suma)

def Sumador(sumar):
    return (sumar+1)

Ingresar_Lista_Enteros(input('Ingresar Lista de Enteros ---> '))