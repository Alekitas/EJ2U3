from ManejadorFlores import ManejadorF
from ManejadorRamos import ManejadorR
class Menu:
    __opcion=None
    def __init__(self):
        self.__opcion=0
    def Iniciar(self):
        unManejadorR=ManejadorR()
        unManejadorF=ManejadorF()
        print('1-')
        print('2-')
        print('3')
        self.__opcion=input('\nIngrese numero de opcion: ')
        if self.__opcion=='1':
            tam=input('Ingrese tamaño del ramo: ')
            unManejadorR.CargadeRamos(tam,unManejadorF)
        if self.__opcion=='2':
            unManejadorR.ContadorFlores(unManejadorF)
            unManejadorR.MostrarTotalR()
        if self.__opcion=='3':
            tamano=input('1-Chico\n2-Mediano\n3-Grande\nIngrese el tipo de ramo: ')
            unManejadorR.MostrarporTamano(unManejadorF,tamano)