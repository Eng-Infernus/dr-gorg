from concurrent.futures import thread
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap,QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox,QMdiSubWindow, QErrorMessage
from PyQt5 import uic
import sys
from colorama import Fore, Back, Style
import qdarktheme
import json

class Signup(QMainWindow):
    def __init__(self):
        super(Signup, self).__init__()
        uic.loadUi("signup.ui", self)
        self.setStyleSheet(qdarktheme.load_stylesheet())
        self.textEdit.setEnabled(False)
        self.checkBox_4.stateChanged.connect(self.elsechronic)
        #self.lineEdit_2.textChanged.connect(self.numonly)
        self.data = {}
        self.pushButton.clicked.connect(self.datafunc)
    
        
    
    def datafunc (self):
        self.name = self.lineEdit.text()
        self.id = self.lineEdit_2.text()
        self.age = self.spinBox.value()
        if self.radioButton.isChecked() == True:
            self.sex = "Male"
        else: 
            self.sex = "Female"
        self.bloodtype = self.comboBox.currentText()
        self.chronic = []
        if self.checkBox.isChecked() == True:
            self.chronic.append("Hypertension")
        if self.checkBox_2.isChecked() == True:
            self.chronic.append("Hypotension")
        if self.checkBox_3.isChecked() == True:
            self.chronic.append("diabetes")
        if self.checkBox_4.isChecked() == True:
            self.chronic.append(self.textEdit.toPlainText())
        self.pheight = self.spinBox_2.value()
        self.pweight = self.spinBox_3.value()
        if self.radioButton_4.isChecked() == True:
            self.maritalstatus = "Married"
        else: 
            self.maritalstatus = "Bacholer"

        self.data['name'] = self.name
        self.data['id'] = self.id
        self.data['age'] = self.age
        self.data['sex'] = self.sex
        self.data['bloodtype'] = self.bloodtype
        self.data['chronic'] = self.chronic
        self.data['height'] = self.pheight
        self.data['weight'] = self.pweight
        self.data['maritalstatus'] = self.maritalstatus
        self.patients = {self.id : self.data}
        try:
            with open("data.json", "r") as f:
                self.last = json.load(f)
            for i in self.last:
                self.patients[i] = self.last[i]
        except:
            pass
        
        
        with open("data.json", "w") as f:
            json.dump(self.patients,f)

        self.hide()
    def elsechronic(self):
        if self.checkBox_4.isChecked() == True:
            self.textEdit.setEnabled(True)
            
        else:
            self.textEdit.setEnabled(False)
            self.textEdit.setText("")

class UI(QMainWindow):
    
    
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file 
        uic.loadUi("mainapp.ui", self)
        self.setWindowTitle("George project")
        #self.lineEdit.setText("Insert link here")
        #show app
        self.show()
        self.setStyleSheet(qdarktheme.load_stylesheet())
        self.pushButton_2.clicked.connect(self.showsu)
        self.pushButton.clicked.connect(self.login)

    def login (self):
        with open("data.json", "r") as f:
            self.currentdata = json.load(f)

        
            
        #try:
            self.mypateint = self.currentdata[self.lineEdit.text()]
            self.label_11.setText(self.mypateint["name"])
            #self.label_12.setText(self.mypateint["id"])
            self.label_12.setText(str(self.mypateint["age"]))
            self.label_13.setText(self.mypateint["sex"])
            self.label_14.setText(self.mypateint["bloodtype"])
            self.label_9.setText(" ,".join(self.mypateint["chronic"]))
            self.label_15.setText(str(self.mypateint["height"]))
            self.label_16.setText(str(self.mypateint["weight"]))
            self.label_17.setText(self.mypateint["maritalstatus"])
        #except:
        #    error_dialog = QErrorMessage()
        #    error_dialog.showMessage('No such Id registered.')

        with open("data.json", "w") as f:
            json.dump(self.currentdata,f)


    def showsu(self):
        self.w = Signup()
        self.w.show()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()