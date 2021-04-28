#imports

#definicion de clases

class edificio:
    nombre=""
    costoMineral=0
    costoGas=0
    costoCapacidad=0
    costoTiempo=0

    def __init__(self, nombre, costoMineral, costoGas, costoCapacidad, costoTiempo):
        self.nombre = nombre
        self.costoMineral= costoMineral
        self.costoGas=costoGas
        self.costoCapacidad=costoCapacidad
        self.costoTiempo=costoTiempo
    def mostrarClase(self):
        print(self.nombre)

class unidad:
    nombre=""
    costoMineral=0
    costoGas=0
    costoCapacidad=0
    costoTiempo=0
    damage=0
    recoleccion=0
    vida=0
    defensa=0
    origen=""

    def __init__(self, nombre, costoMineral, costoGas, costoCapacidad, costoTiempo, damage, recoleccion, vida, defensa, origen):
        self.nombre = nombre
        self.costoMineral= costoMineral
        self.costoGas=costoGas
        self.costoCapacidad=costoCapacidad
        self.costoTiempo=costoTiempo
        self.damage = damage
        self.recoleccion = recoleccion
        self.vida = vida
        self.defensa = defensa
        self.origen = origen
    def mostrarClase(self):
        print(self.nombre)
#datos INICIALES

MINERAL=0
GAS=0
CAPACIDAD=0
SEGUNDOS=0
recolectores=6
unidades=[]
#funciones


def leerArchivo(listaE, listaU, nombreArchivo):
    f = open ('prueba.txt','r')
    for linea in f:
        if (linea[0]=="E"):
            line2=linea.split(" ")
            e=edificio(line2[1],int(line2[2]),int(line2[3]),int(line2[4]),int(line2[5]))
            listaE.append(e)
        if (linea[0]=="U"):
            line2=linea.split(" ")
            u=unidad(line2[1],int(line2[2]),int(line2[3]),int(line2[4]),int(line2[5]),int(line2[6]),int(line2[7]),int(line2[8]), int(line2[9]),line2[10])
            listaU.append(u)
    f.close()
    return
def escribirArchivo():
    return

def tecnologiaTanto():
    return

def mostrarlistas(lista):
    fila="elementos: "
    for elemento in lista:
        fila = fila+", " + elemento.nombre
    print( fila)
#algoritmo
#listas temporales
listaEdificios=[]
listaUnidades=[]
nombreArchivo= input("Ingrese el nombre del archivo que desea usar: ")
leerArchivo(listaEdificios,listaUnidades, nombreArchivo+".txt")
mostrarlistas(listaUnidades)
mostrarlistas(listaEdificios)
#lista objetivo
buildOrder=[]
