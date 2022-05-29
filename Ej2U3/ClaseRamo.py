from ManejadorFlores import ManejadorF

class Ramo:
    __tamano=str
    __flores=[]
    def __init__(self,tamano):
        self.__tamano=tamano
        self.__flores=[]

    def AgregarFlor(self,flor):
        return self.__flores.append(flor)

    def getTamano(self):
        return self.__tamano

    def getFlores(self):
        return self.__flores