
# coding: utf-8

# In[4]:

import sys
import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QtGui.QMainWindow):
    
    #Le da las propiedades a la ventana y la muestra
    def __init__(self):
        super(Window, self).__init__()
        
        self.button = QtGui.QPushButton("Apriétame",self)#Boton que va a calcular los días restantes para el 15 de sep.
        self.button.clicked.connect(self.diasRestantes)#El escucha para el boton
        self.button.resize(100,100)
        self.button.move(190,150)
        
        self.setGeometry(250, 200, 500, 300)#Ajustando el tamanho de la ventana
        self.setWindowTitle("¡Viva México!") #Agregando el titulo
        self.setWindowIcon(QtGui.QIcon('flaggy.png')) #Agregando el icono de la bandera
        
        #Anadiendo personajes de la independencia
        self.styleChoice = QtGui.QLabel("Mientras esperas, te mencionaremos a estos heroes. Quienes merecen ser recordados \n por su valentia y honor\n 1- Jose Maria Morelos y Pavon.\n 2.-Josefa Ortiz de Dominguez\n 3.-Vicente Guerrero", self)
        self.styleChoice.move(0,20)
        self.styleChoice.resize(self.styleChoice.sizeHint())
        
        #Cambiando el color de las letras
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        self.styleChoice.setPalette(palette)
        
        #Adornando la ventana con color :P
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(p)        
        #Finalmente mostrando la ventana
        self.show()
     
    #Calcula los días que faltan para el 15 de septiembre a partir del día que se pregunte
    def diasRestantes(self):
        hoy = datetime.date.today()#La fecha del día que se pregunte
        diaIndependencia = datetime.date(hoy.year, 9,15)#Fecha (para el anho que se pregunte) del 15 de septiembre
        if hoy > diaIndependencia:
            diaIndependencia = datetime.date(hoy.year+1,9,15)#Compara las fechas, si la fecha ya paso, calcula los días para el anho siguiente
        diasRestantes = diaIndependencia - hoy #Días que faltan para la fecha
        self.button.setText("Dias hasta el 15 de septiembre: " + str(diasRestantes.days) + " (No contando hoy)")#Cambia el texto del boton
        self.button.resize(self.button.sizeHint())#Adapta el tamanio del boton al texto nuevo
        self.button.move(150,200)#Lo mueve para que no estorbe con su nuevo tamanho en el 
            
#Inicia la aplicacion.
def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
main()

    

