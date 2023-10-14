def Ingresar_Num(Numero,lista):
    if(Numero.isdigit()==True): lista.append(Numero), Ingresar_Num(input('Ingresar numero--->'),lista)
    else:
        if(Numero=='hecho'): lista.sort(), print('Numero menor ---> ',lista[0]), print('Numero Mayor----> ',lista[-1:])
        else: Ingresar_Num(input('Caracter no valido Ingresa un numero---> '),lista)


Ingresar_Num(input('Ingresar un Numero -------->'),[])
