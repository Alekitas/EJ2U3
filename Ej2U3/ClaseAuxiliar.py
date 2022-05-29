class Aux:
    __codigo=None
    __cont=None
    def __init__(self,cont,codigo):
        self.__cont=cont
        self.__codigo=codigo

    def getCont(self):
        return self.__cont

    def getCod(self):
        return self.__codigo

    def Contar(self):
        self.__cont+=1
    
    def __gt__(self,other):
        if type(other)==Aux: 
            return other.getCont()>self.__cont