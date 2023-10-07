#CCON PROGRAMACION FUNCIONAL
def Abrir_Archivo(Direccion):
    Divir(open(Direccion))

def Divir(ArchivoA):
    Empezar_from(ArchivoA.readline(),ArchivoA)

def Empezar_from(Arreglo,ArchivoA):
    if(Arreglo.startswith('From')):print(Imprimir_DIA(Dividir_Linea(Arreglo))), Divir(ArchivoA)
    if(Arreglo!=''):Divir(ArchivoA)

def Dividir_Linea(Arreglo):
    return Arreglo.split()

def Imprimir_DIA(Arreglo):
    return Arreglo[2]

Abrir_Archivo('Correo.txt')


#SIN PROGRAMACION FUNCIONAL
#manejador=open('Correo.txt')
#for linea in manejador:
 #   palabras= linea.split()
 # if len(palabras)==0 or palabras[0]!='From': continue
 # print(palabras[2])



