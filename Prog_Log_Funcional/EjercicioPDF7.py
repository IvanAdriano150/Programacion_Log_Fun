def Ingresar_Calif(Calificaciones):
    Calcular_Promedio(Calificaciones,0,len(Calificaciones))
    Aprobados_Reprobados(Calificaciones,0,0,len(Calificaciones))
    mayor_ocho(Calificaciones,0)


def mayor_ocho(Calificaciones,num):
    if(len(Calificaciones)!=0):
        if(Calificaciones[0]>=8):mayor_ocho(Calificaciones[1:],num+1)
        else: mayor_ocho(Calificaciones[1:],num)
    else: print('Alumnos mayoresa a ocho ---> ',num)

def Calcular_Promedio(Calificaciones,sum,tot):
    if(len(Calificaciones)!=0):
        Calcular_Promedio(Calificaciones[1:],sum+Calificaciones[0],tot)
    else:
        print('El promedio es --- > ',round((sum/tot),2))

def Aprobados_Reprobados(Calificaciones,Ap,Rep,tot):
    if(len(Calificaciones)!=0):
        if(Calificaciones[0]>6): Aprobados_Reprobados(Calificaciones[1:],Ap+1,Rep,tot)
        else: Aprobados_Reprobados(Calificaciones[1:],Ap,Rep+1,tot)
    else:
        print('Alumnos Aprobados ---> ',Ap,'  Con un Porcentaje del ---> ',(round((Ap/tot),2))*100,'%')
        print('Alumnos Reprobados ---> ',Rep, '  Con un Porcentaje del ---> ',(round((Rep/tot),2))*100,'%')

Ingresar_Calif([10,9,10,8,7,6,5,6,7,8,9,10,7,4,5,6,7,8,9,10,6,6,6,6,6,6])
