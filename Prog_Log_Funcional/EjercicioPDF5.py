def insertar_arreglo(Arreglo):
    Leer(Arreglo,0,0,0,0,0,0,0,0,0,0,0)


def Leer(Arreglo,C,I,II,III,IV,V,VI,VII,VIII,IX,X):
    if(len(Arreglo)!=0):
        if(Arreglo[0]=='0'):Leer(Arreglo[1:],C+1,I,II,III,IV,V,VI,VII,VIII,IX,X)
        if(Arreglo[0]=='1'):Leer(Arreglo[1:],C,I+1,II,III,IV,V,VI,VII,VIII,IX,X)
        if(Arreglo[0]=='2'):Leer(Arreglo[1:],C,I,II+1,III,IV,V,VI,VII,VIII,IX,X)
        if(Arreglo[0]=='3'):Leer(Arreglo[1:],C,I,II,III+1,IV,V,VI,VII,VIII,IX,X)
        if(Arreglo[0]=='4'):Leer(Arreglo[1:],C,I,II,III,IV+1,V,VI,VII,VIII,IX,X)
        if(Arreglo[0]=='5'):Leer(Arreglo[1:],C,I,II,III,IV,V+1,VI,VII,VIII,IX,X)
        if(Arreglo[0]=='6'):Leer(Arreglo[1:],C,I,II,III,IV,V,VI+1,VII,VIII,IX,X)
        if(Arreglo[0]=='7'):Leer(Arreglo[1:],C,I,II,III,IV,V,VI,VII+1,VIII,IX,X)
        if(Arreglo[0]=='8'):Leer(Arreglo[1:],C,I,II,III,IV,V,VI,VII,VIII+1,IX,X)
        if(Arreglo[0]=='9'):Leer(Arreglo[1:],C,I,II,III,IV,V,VI,VII,VIII,IX+1,X)
        if(Arreglo[0]=='10'):Leer(Arreglo[1:],C,I,II,III,IV,V,VI,VII,VIII,IX,X+1)
    else:
        print('Calificacion                      Alumnos')
        print('       10                          ',X)
        print('        9                          ',IX)
        print('        8                          ',VIII)
        print('        7                          ',VII)
        print('        6                          ',VI)
        print('        5                          ',V)
        print('        4                          ',IV)
        print('        3                          ',III)
        print('        2                          ',II)
        print('        1                          ',I)
        print('        0                          ',C)




insertar_arreglo(['10','10','2','3','10','8','9','10','10','10','10','10','10','10','10','0','1','2'])