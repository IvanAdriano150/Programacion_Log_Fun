def Ingresar_Lista(Lista):
    determinar_Valor((Lista.split(',')),0,0,0)


def determinar_Valor(lista,c,p,n):
   if(len(lista)!=0): 
    if(int(lista[0])==0): determinar_Valor(lista[1:],(c+1),p,n)
    if(int(lista[0])>0):determinar_Valor(lista[1:],c,(p+1),n)
    if(int(lista[0])<0):determinar_Valor(lista[1:],c,p,(n+1))
   else: print('Cantidad de Ceros ----> ',c),print('Cantidad de Positivos---->',p),print('Cantidad de Negativos-----> ',n)

Ingresar_Lista(input('Ingresar Lista de Numeros ---------- > '))