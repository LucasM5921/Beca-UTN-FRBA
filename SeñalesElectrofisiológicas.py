import sys
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
from PyQt5.QtWidgets import (QTextEdit, QApplication, QPushButton,
                            QLabel, QLineEdit, QComboBox,
                            QMainWindow, QFileDialog)
from PyQt5.QtGui import QIcon


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Directory
        self.myPath = 'D:/Lucas/EscuelaL/Universidad Tecnológica Nacional/Becas/Señales Electrofisiológicas/Software/Python/'


        #Ventana
        self.resize(500, 500)
        self.move(500, 100)        

        self.title = 'UTN FRBA - Señeles Electrofisológicas'
        self.iconName = QIcon(self.myPath + 'Imágenes/UTN FRBA icon.png')
        

        #Botones de Comandos
        self.etiquetaComandos = QLabel('Comandos:', self)

        self.etiquetaComandos.move(10, 270)


        self.buttonConn = QPushButton('Conectar', self)
        self.buttonDesconn = QPushButton('Desconectar', self)
        self.buttonReset = QPushButton('Resetear', self)
        self.buttonRegister = QPushButton('Registrar', self)
        self.buttonRecord = QPushButton('Grabar', self)
        self.buttonStop = QPushButton('Pausar', self)
        self.buttonOut = QPushButton('Salir', self)

        self.buttonConn.move(10, 295)
        self.buttonDesconn.move(10, 325)
        self.buttonReset.move(10, 355)
        self.buttonRegister.move(10, 385)
        self.buttonRecord.move(10, 415)
        self.buttonStop.move(10, 445)
        self.buttonOut.move(395, 465)

        self.buttonConn.clicked.connect(lambda: self.BotPresConn('Conectado y Calibrado'))
        self.buttonDesconn.clicked.connect(lambda: self.BotPresDesconn('Desconectado'))
        self.buttonReset.clicked.connect(lambda: self.BotPresReset('Reseteado'))
        self.buttonRegister.clicked.connect(lambda: self.BotPresRegister('Registrando'))
        self.buttonRecord.clicked.connect(lambda: self.BotPresRecord('Grabando'))
        self.buttonStop.clicked.connect(lambda: self.BotPresStop('Pausado'))
        self.buttonOut.clicked.connect(lambda: self.BotPresOut('Salir'))


        #Chips
        self.etiquetaChip = QLabel('Chip:', self)
        self.etiquetaChip.move(10, 15)

        self.ChipSelect = QComboBox(self)
        self.ChipSelect.move(40, 20)
        self.ChipSelect.resize(200, 22)


        #Campo de Información
        self.etiquetaInfo = QLabel('Información:', self)
        self.etiquetaInfo.move(10, 40)

        self.CampoTxtInfo = QTextEdit(self)
        self.CampoTxtInfo.setReadOnly(True)

        self.CampoTxtInfo.move(10, 65)
        self.CampoTxtInfo.resize(480, 200)


        #Explorador de archivos
        ##Boton
        self.buttonExplorer = QPushButton(self)
    
        self.buttonExplorer.setIcon(QIcon(self.myPath + 'Imágenes/Carpeta Icon1.png'))
        
        self.buttonExplorer.move(260, 18)
        self.buttonExplorer.resize(25, 25)

        self.buttonExplorer.clicked.connect(lambda: self.abrir_ExpArch(
            'Explorador de archivos abierto'))

        ##Directorio
        self.CampoTxtExplorer = QLineEdit(self)
        self.CampoTxtExplorer.setReadOnly(True)


        self.CampoTxtExplorer.move(290, 20)
        self.CampoTxtExplorer.resize(200, 22)



        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconName))
        self.show()

    def abrir_ExpArch(self, estado):
        print(estado)

        self.CampoTxtInfo.insertPlainText('Explorador de archivos abierto\n')
        
        ExpArch = QFileDialog.getExistingDirectory(
            self, 'Explorador de Archivos y carpetas')
        
        if str(self.sender()):
            self.CampoTxtExplorer.setText(ExpArch)


    def BotPresConn(self,estado):
        print(estado)

        self.CampoTxtInfo.insertPlainText('Conectado\n')


    def BotPresDesconn(self,estado):
        print(estado)
        
        self.CampoTxtInfo.insertPlainText('Desconectado\n')


    def BotPresReset(self,estado):
        print(estado)

        self.CampoTxtInfo.insertPlainText('Reseteado\n')


    def BotPresRegister(self,estado):
        print(estado)

        self.CampoTxtInfo.insertPlainText('Registrando\n')

        #Registro de datos
        # CantDatos = 1000
        # CantCanales = 4

        # Señal = np.random.rand(CantDatos, CantCanales)

        x = np.arange(0, 2*np.pi, 0.01)
        Señal = np.sin(x)

        self.CampoTxtInfo.insertPlainText(str(Señal))

        #Gráfico de datos
        plt.plot(Señal)
        plt.show()

        #Guardar datos
        # np.save('Lucas.npy' , Señal)
        
        np.save('Lucas_{:%Y-%m-%d_%H-%M-%S}.npy'.format(datetime.now()), Señal)


    def BotPresRecord(self,estado):
        print(estado)

        self.CampoTxtInfo.insertPlainText('Grabando\n')


    def BotPresStop(self,estado):
        print(estado)

        self.CampoTxtInfo.insertPlainText('Proceso parado\n')


    def BotPresOut(self,estado):
        print(estado)

        self.close()
    


App = QApplication(sys.argv)
ventana1 = Principal()
sys.exit(App.exec())