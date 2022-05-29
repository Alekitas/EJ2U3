class Flores:
    __numero=None
    __nombre=None
    __color=None
    __descrip=None
    def __init__(self,numero,nombre,color,descrip):
        self.__numero=numero
        self.__nombre=nombre
        self.__color=color
        self.__descrip=descrip
    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getColor(self):
        return self.__color
    def getDescrip(self):
        return self.__descrip
    def __str__(self):
        return 'Numero: {} Nombre: {} Color: {} Descripcion: {}'.format(self.__numero,self.__nombre, self.__color, self.__descrip)