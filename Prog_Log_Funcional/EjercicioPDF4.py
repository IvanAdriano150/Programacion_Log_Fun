def Ingresar_Votos(Voto,VotosTotales):
    if(Voto>=1 and Voto<=12):
        VotosTotales.append(Voto)
    if(Voto>12 or Voto<-1): Ingresar_Votos(input('(Candidato No valido) Ingresa otro voto ----- > '),VotosTotales)
    if(Voto==-1): print('Fin')








Ingresar_Votos(input('Ingresar Voto ---- > '),[])