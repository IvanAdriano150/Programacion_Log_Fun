def Lista_Desordenada(Lista,Numero,x):
    if(x==len(Lista)): print('No existe dicho numero en la lista')
    else: 
        if(Lista[x]==Numero):print('El numero --> ',Numero,'  Esta en la posicion ---> ',x)
        else:Lista_Desordenada(Lista,Numero,x+1)





Lista_Desordenada(['2','3','2','2','0','1','3'],'1',0)