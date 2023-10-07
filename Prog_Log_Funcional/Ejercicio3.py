def Abrir_Archivo(Direccion,Palabras):
    Leer_Linea(open(Direccion),Palabras)

def Leer_Linea(Archivo,Palabras):
    Leer_Linea2(Archivo.readline(),Archivo,Palabras)
    
def Leer_Linea2(ListaL,Archivo,ListaP):
     if(ListaL==''):print(Ordenar_Lista(ListaP))
     else:
          Comprar_Listas(ListaL.split(),Archivo,ListaP)
     
def Comprar_Listas(Lista,Archivo,Palabras):
            if(len(Palabras)==0): Comprar_Listas(Lista[1:],Archivo,Agregar_Lista(Palabras,Lista[0]))
            else: 
                if(len(Lista)!=0):
                    Lista_Palabra(Palabras,Lista,Palabras,Archivo)
                else: 
                    Leer_Linea(Archivo,Palabras)

def Lista_Palabra(ListaExperimental,Palabra,Lista,Archivo):
     if(len(ListaExperimental)!=0):
        if(ListaExperimental[0]==Palabra[0]): Comprar_Listas(Palabra[1:],Archivo,Lista)
        else:Lista_Palabra(ListaExperimental[1:],Palabra,Lista,Archivo)
     else: Comprar_Listas(Palabra[1:],Archivo,Agregar_Lista(Lista,Palabra[0]))
          
def Ordenar_Lista(LISTA):
     LISTA.sort()
     return LISTA

def Agregar_Lista(Lista,palabra):
    Lista.append(palabra)
    return Lista






Abrir_Archivo('1Romeo.txt',[])