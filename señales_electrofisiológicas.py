"""
GUI sensor
"""

import sys
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Principal(QtWidgets.QMainWindow()):
    def __init__(self):
        super().__init__()

        #Directory
        #self.myPath = '''D:/Lucas/EscuelaL/Universidad Tecnológica Nacional/
        #                Becas/Señales Electrofisiológicas/Software/Python/'''
        self.my_path = os.getcwd()

        #Ventana
        self.resize(500, 500)
        self.move(500, 100)

        self.title = 'UTN FRBA - Señeles Electrofisológicas'
        self.icon_name = QtGui.QIcon(os.path.join(self.myPath, 'Imágenes/UTN FRBA icon.png'))


        #Botones de Comandos
        self.etiqueta_comandos = QtWidgets.QLabel('Comandos:', self)

        self.etiqueta_comandos.move(10, 270)


        self.button_conn = QtWidgets.QPushButton('Conectar', self)
        self.button_desconn = QtWidgets.QPushButton('Desconectar', self)
        self.button_reset = QtWidgets.QPushButton('Resetear', self)
        self.button_register = QtWidgets.QPushButton('Registrar', self)
        self.button_record = QtWidgets.QPushButton('Grabar', self)
        self.button_stop = QtWidgets.QPushButton('Pausar', self)
        self.button_out = QtWidgets.QPushButton('Salir', self)

        self.button_conn.move(10, 295)
        self.button_desconn.move(10, 325)
        self.button_reset.move(10, 355)
        self.button_register.move(10, 385)
        self.button_record.move(10, 415)
        self.button_stop.move(10, 445)
        self.button_out.move(395, 465)

        self.button_conn.clicked.connect(lambda: self.bot_pres_conn('Conectado y Calibrado'))
        self.button_desconn.clicked.connect(lambda: self.bot_pres_desconn('Desconectado'))
        self.button_reset.clicked.connect(lambda: self.bot_pres_reset('Reseteado'))
        self.button_register.clicked.connect(lambda: self.bot_pres_register('Registrando'))
        self.button_record.clicked.connect(lambda: self.bot_pres_record('Grabando'))
        self.button_stop.clicked.connect(lambda: self.bot_pres_stop('Pausado'))
        self.button_out.clicked.connect(lambda: self.bot_pres_out('Salir'))


        #Chips
        self.etiqueta_chip = QtWidgets.QLabel('Chip:', self)
        self.etiqueta_chip.move(10, 15)

        self.chip_select = QtWidgets.QComboBox(self)
        self.chip_select.move(40, 20)
        self.chip_select.resize(200, 22)


        #Campo de Información
        self.etiqueta_info = QtWidgets.QLabel('Información:', self)
        self.etiqueta_info.move(10, 40)

        self.campo_txt_info = QtWidgets.QTextEdit(self)
        self.campo_txt_info.setReadOnly(True)

        self.campo_txt_info.move(10, 65)
        self.campo_txt_info.resize(480, 200)


        #Explorador de archivos
        ##Boton
        self.button_explorer = QtWidgets.QPushButton(self)

        self.button_explorer.setIcon(QtGui.QIcon(os.path.join(
            self.my_path, 'Imágenes/Carpeta Icon1.png')))

        self.button_explorer.move(260, 18)
        self.button_explorer.resize(25, 25)

        self.button_explorer.clicked.connect(lambda: self.abrir_exp_arch(
            'Explorador de archivos abierto'))

        ##Directorio
        self.campo_txt_explorer = QtWidgets.QLineEdit(self)
        self.campo_txt_explorer.setReadOnly(True)


        self.campo_txt_explorer.move(290, 20)
        self.campo_txt_explorer.resize(200, 22)



        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.show()

    def abrir_exp_arch(self, estado):
        print(estado)

        self.campo_txt_info.insertPlainText('Explorador de archivos abierto\n')

        exp_arch = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Explorador de Archivos y carpetas')

        if str(self.sender()):
            self.campo_txt_explorer.setText(exp_arch)


    def bot_pres_conn(self,estado):
        print(estado)

        self.campo_txt_info.insertPlainText('Conectado\n')


    def bot_pres_desconn(self,estado):
        print(estado)

        self.campo_txt_info.insertPlainText('Desconectado\n')


    def bot_pres_reset(self,estado):
        print(estado)

        self.campo_txt_info.insertPlainText('Reseteado\n')


    def bot_pres_register(self,estado):
        print(estado)

        self.campo_txt_info.insertPlainText('Registrando\n')

        #Registro de datos
        # CantDatos = 1000
        # CantCanales = 4

        # Signal = np.random.rand(CantDatos, CantCanales)

        x_time = np.arange(0, 2*np.pi, 0.01)
        y_signal = np.sin(x_time)

        self.campo_txt_info.insertPlainText(str(y_signal))

        #Gráfico de datos
        plt.plot(y_signal)
        plt.show()

        #Guardar datos
        # np.save('Lucas.npy' , Señal)

        np.save('Lucas_{:%Y-%m-%d_%H-%M-%S}.npy'.format(datetime.datetime.now()), y_signal)


    def bot_pres_record(self,estado):
        print(estado)

        self.campo_txt_info.insertPlainText('Grabando\n')


    def bot_pres_stop(self,estado):
        print(estado)

        self.campo_txt_info.insertPlainText('Proceso parado\n')


    def bot_pres_out(self,estado):
        print(estado)

        self.close()



App = QtWidgets.QApplication(sys.argv)
ventana1 = Principal()
sys.exit(App.exec())
