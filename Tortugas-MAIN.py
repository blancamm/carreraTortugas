import turtle
import random


class Circuito():
    
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, ancho, altura): #se va a dejar en publico
        
        self.__screen = turtle.Screen() #se pone en privado porque si no cualquiera con
                                        #nombre.screen puede modificar mi pantalla
                                        #PERO ESTO ES UNA CLASE(DEFINICION DE OBJETO), QUE SE ASIGNA A UN ATRIBUTO(VARIABLE) Y PASA A SER UNA INSTACIA
                                        #Screen()
                                            #Return the singleton screen object.
                                            #If none exists at the moment, create a new one and return it,
                                            #else return the existing one
        self.__screen.setup (ancho, altura)
        self.__screen.bgcolor('lightgray') #tipo asfalto
        self.__startLine = -ancho/2 + ((5/100)*ancho)
        self.__finishLine = ancho/2 - ((5/100)*ancho)
        
        self.corredores = []
        self.__crearCorredores() #si no lo pongo no se crean los corredores
        
    def __crearCorredores(self):

        for i in range(4): #ira de 0, 1, 2,3
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.color(self.__colorTurtle[i]) #IMPORTANTE EL SELF
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
    def competir(self):
        hayGanador = False
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                   hayGanador = True
                   print('la tortuga {} ha ganado'.format(tortuga.color()[1]))
                   break

            '''
MI METODO:
        inicio = [self.__startLine, self.__startLine, self.__startLine, self.__startLine]
        hayGanador = False
        while hayGanador == False:
            for i in range(4):
                avance = random.randint(1,6)
                inicio[i] += avance
                self.corredores[i].setpos(inicio[i], self.__posStartY[i])
                if inicio[i] >= self.__finishLine:
                    ganador = i +1
                    hayGanador = True
                   
        return print('la tortuga ganadora es la tortuga numero {}'.format(ganador))
    '''



if __name__ == '__main__':   #esto es buena costumbre para probarlo y si luego se importa, no sale
    circuito = Circuito(640,480)
    circuito.competir()


        
    
        