def Ingresar_Votos(Voto,VotosTotales):
    if(Voto>=1 and Voto<=12):
        VotosTotales.append(Voto)
        Ingresar_Votos(int(input('Ingresar Voto ---- > ')),VotosTotales)
    if(Voto>12 or Voto<-1): Ingresar_Votos(int(input('(Candidato No valido) Ingresa otro voto ----- > ')),VotosTotales)
    if(Voto==-1):
        contar_votos(VotosTotales,0,0,0,0,0,0,0,0,0,0,0,0,len(VotosTotales))



def contar_votos(votos,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez,once,doce,VT):
    if(len(votos)!=0):
        if(votos[0]==1):    contar_votos(votos[1:],uno+1,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez,once,doce,VT)
        if(votos[0]==2):    contar_votos(votos[1:],uno,dos+1,tres,cuatro,cinco,seis,siete,ocho,nueve,diez,once,doce,VT)
        if(votos[0]==3):    contar_votos(votos[1:],uno,dos,tres+1,cuatro,cinco,seis,siete,ocho,nueve,diez,once,doce,VT)
        if(votos[0]==4):    contar_votos(votos[1:],uno,dos,tres,cuatro+1,cinco,seis,siete,ocho,nueve,diez,once,doce,VT)
        if(votos[0]==5):    contar_votos(votos[1:],uno,dos,tres,cuatro,cinco+1,seis,siete,ocho,nueve,diez,once,doce,VT)
        if(votos[0]==6):    contar_votos(votos[1:],uno,dos,tres,cuatro,cinco,seis+1,siete,ocho,nueve,diez,once,doce,VT)
        if(votos[0]==7):    contar_votos(votos[1:],uno,dos,tres,cuatro,cinco,seis,siete+1,ocho,nueve,diez,once,doce,VT)
        if(votos[0]==8):    contar_votos(votos[1:],uno,dos,tres,cuatro,cinco,seis,siete,ocho+1,nueve,diez,once,doce,VT)
        if(votos[0]==9):    contar_votos(votos[1:],uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve+1,diez,once,doce,VT)
        if(votos[0]==10):   contar_votos(votos[1:],uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez+1,once,doce,VT)
        if(votos[0]==11):   contar_votos(votos[1:],uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez,once+1,doce,VT)
        if(votos[0]==12):   contar_votos(votos[1:],uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez,once,doce+1,VT)
    else:
        Dividir(Crear_TUPLAS([(uno,'uno'),(dos,'dos'),(tres,'tres'),(cuatro,'cuatro'),(cinco,'cinco'),(seis,'seis'),(siete,'siete'),(ocho,'ocho'),(nueve,'nueve'),(diez,'diez'),(once,'once'),(doce,'doce')]),VT)




def Crear_TUPLAS(tuplas):
    tuplas.sort()
    return tuplas[-1]

def Dividir(Tuplita,VT):
    print('El candidato Ganador es el ---> Candidato No.',Tuplita[1])
    print('Con un porcentaje del ---> ', ((Tuplita[0]*100)/VT),'%')

Ingresar_Votos(int(input('Ingresar Voto ---- > ')),[])
