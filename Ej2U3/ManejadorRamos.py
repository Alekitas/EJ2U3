from ClaseRamo import Ramo
from ClaseAuxiliar import Aux
class ManejadorR:
    __listaramos=[]
    def __init__(self):
        self.__listaramos=[]

    def getLista(self):
        return self.__listaramos

    def CargadeRamos(self,tamano,unManejadorF):
        tamano=tamano.lower()
        unRamo=Ramo(tamano)

        if tamano=="chico":
            for i in range(2):
                unRamo.AgregarFlor(unManejadorF.ObtenerFlor(int(input(' \n1-Azucenas\n2-Margaritas\n3-Violetas\n4-Lirio\n5-Rosas\nIngrese un numero de flor a agregar al ramo:'))-1))
                print('Flor Agregada')
        elif tamano=="mediano":
            for i in range(4):
                unRamo.AgregarFlor(unManejadorF.ObtenerFlor(int(input('\n1-Azucenas\n2-Margaritas\n3-Violetas\n4-Lirio\n5-Rosas\nIngrese un numero de flor a agregar al ramo:'))-1))
        elif tamano=="grande":
            for i in range(6):
                unRamo.AgregarFlor(unManejadorF.ObtenerFlor(int(input('\n1-Azucenas\n2-Margaritas\n3-Violetas\n4-Lirio\n5-Rosas\nIngrese un numero de flor a agregar al ramo:'))-1))
        else:
            print("Ingrese un tamaño valido")

        if unRamo!=None:
            self.__listaramos.append(unRamo)
        
    def ContadorFlores(self,unManejadorF):
        Contador=[]
        for i in range(unManejadorF.ObtenerCantidad()):
            Contador.append(Aux(0,i))
        
        for i in range(len(self.__listaramos)):
            Arreglo=self.__listaramos[i].getFlores()
            for j in range(len(Arreglo)):
                Contador[Arreglo[j].getNumero()-1].Contar()

        Contador.sort()

        for i in range(5):
            print(unManejadorF.ObtenerFlor(Contador[i].getCod()))

    def MostrarTotalR(self):
        for i in range(len(self.__listaramos)):
            Arreglo=self.__listaramos[i].getFlores()
            for j in range(len(Arreglo)):
                print(Arreglo[j])
    
    def MostrarporTamano(self,unManejadorF,tamano):
        Contador=[]
        for i in range(unManejadorF.ObtenerCantidad()):
            Contador.append(Aux(0,i))
        
        for i in range(len(self.__listaramos)):
            if self.__listaramos[i].getTamano()==tamano:
                Arreglo=self.__listaramos[i].getFlores()
                for j in range(len(Arreglo)):
                    Contador[Arreglo[j].getNumero()-1].Contar()

        Contador.sort()

        for i in range(len(Contador)):
            print(unManejadorF.ObtenerFlor(Contador[i].getCod()))