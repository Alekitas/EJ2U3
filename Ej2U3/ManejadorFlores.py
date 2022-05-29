from ClaseFlores import Flores
import numpy as np
import csv
class ManejadorF:
    __cantidad=0
    __dimension=10
    __incremento=5

    def __init__(self,dimension=10):
        self.__flores=np.empty(dimension,dtype=Flores)
        self.__cantidad=0
        self.__dimension=dimension

    def AgregarFlor(self,unaFlor):
        if self.__flores==self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
        self.__puntos[self.__cantidad]=unaFlor
        self.__cantidad+=1

    def Iniciar(self):
        archivo=open('Flores.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            unaFlor=Flores(fila[0],fila[1],fila[2],fila[3])
            self.AgregarFlor(unaFlor)
        archivo.close()

    def ObtenerFlor(self,num):
        return self.__flores[num]

    def ObtenerCantidad(self):
        return self.__cantidad