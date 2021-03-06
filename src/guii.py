# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, uic, QtCore, QtSql
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2,imutils
import PyQt5.QtWidgets
import os
import PIL
from PIL import Image
import subprocess
import shutil
from src.InferenceSettings import InferenceSettings
from PyQt5.QtCore import QCoreApplication
# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys


class Ui_MainWindow(QtWidgets.QMainWindow):
    
    filename=''
    saving_dir=''
    opening_dir=''
    main_image=''
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1605, 916)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.opendir = QtWidgets.QPushButton(self.centralwidget)
        self.opendir.setGeometry(QtCore.QRect(40, 130, 151, 151))
        self.opendir.setObjectName("opendir")
        self.opendir.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        
        # self.loadimage = QtWidgets.QPushButton(self.centralwidget)
        # self.loadimage.setGeometry(QtCore.QRect(40, 140, 151, 51))
        # self.loadimage.setObjectName("loadimage")
        # self.savedir = QtWidgets.QPushButton(self.centralwidget)
        # self.savedir.setGeometry(QtCore.QRect(40, 200, 151, 51))
        # self.savedir.setObjectName("savedir")
        # self.save = QtWidgets.QPushButton(self.centralwidget)
        # self.save.setGeometry(QtCore.QRect(40, 240, 151, 51))
        # self.save.setObjectName("save")
        # self.predict = QtWidgets.QPushButton(self.centralwidget)
        # self.predict.setGeometry(QtCore.QRect(40, 340, 151, 51))
        # self.predict.setObjectName("predict")
        self.predictall = QtWidgets.QPushButton(self.centralwidget)
        self.predictall.setGeometry(QtCore.QRect(40, 430, 151, 51))
        self.predictall.setObjectName("predictall")
        self.nextimage = QtWidgets.QPushButton(self.centralwidget)
        self.nextimage.setGeometry(QtCore.QRect(40, 230, 151, 51))
        self.nextimage.setObjectName("nextimage")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(230, 10, 1231, 881))
        self.image.setText("")
        
        self.image.setScaledContents(False)
        self.image.setObjectName("image")
        self.preimage = QtWidgets.QPushButton(self.centralwidget)
        self.preimage.setGeometry(QtCore.QRect(40, 330, 151, 51))
        self.preimage.setObjectName("preimage")
        self.config = QtWidgets.QPushButton(self.centralwidget)
        self.config.setGeometry(QtCore.QRect(40, 30, 151, 51))
        self.config.setObjectName("config")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(40, 730, 151, 51))
        self.back.setObjectName("back")
        self.back_Action = QtWidgets.QPushButton(self.centralwidget)
        self.back_Action.setGeometry(QtCore.QRect(40, 530, 151, 51))
        self.back_Action.setObjectName("back_Action")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(40, 630, 151, 51))
        self.help.setObjectName("Help")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1605, 20))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))
        self.actionSave.triggered.connect(lambda: self.clicked("Save was clicked"))
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
        self.actionPaste.triggered.connect(lambda: self.clicked("Paste was clicked"))
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dirIterator = None
        self.fileList = []
        self.currentIndex = 0
        self.tmp=None

        self.opendir.clicked.connect(self.open_dir)
        # self.loadimage.clicked.connect(self.load_image)
        # self.savedir.clicked.connect(self.save_dir)
        # self.save.clicked.connect(self.save_image)
        self.preimage.clicked.connect(self.pre_image)
        self.nextimage.clicked.connect(self.next_image)
        # self.predict.clicked.connect(self.predicted)
        self.predictall.clicked.connect(self.predict_all)
        self.config.clicked.connect(self.configuration)
        self.back.clicked.connect(self.backButton)
        self.back_Action.clicked.connect(self.backButton_Action)
        self.help.clicked.connect(self.helpButton)
        self.predictall.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        self.preimage.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        self.config.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        self.back_Action.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        self.help.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        self.back.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        self.nextimage.setStyleSheet("color: white;border-style: none;border-width: none;border-radius: 0px;border-color: black;font:bold 14px;min-width: 7em;padding: 6px;background-color: grey;")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Automated Visual Inspection"))
        self.opendir.setText(_translate("MainWindow", "Open Dir"))
                # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        # self.loadimage.setText(_translate("MainWindow", "LOAD IMAGE"))
        # self.savedir.setText(_translate("MainWindow", "SAVE DIR"))
        # self.save.setText(_translate("MainWindow", "SAVE IMAGE"))
        # self.predict.setText(_translate("MainWindow", "PREDICT"))
        self.predictall.setText(_translate("MainWindow", "PREDICT ALL"))
        self.nextimage.setText(_translate("MainWindow", "NEXT IMAGE"))
        self.preimage.setText(_translate("MainWindow", "PREV. IMAGE"))
        self.config.setText(_translate("MainWindow", "Config. "))
        self.back.setText(_translate("MainWindow", "Quit "))
        self.back_Action.setText(_translate("MainWindow", "Back"))
        self.help.setText(_translate("MainWindow", "Help"))

        

        # self.opendir.setIcon(QIcon('vesit.png'))

    def load_image(self):
        global filename
        global main_image
        filename= QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        #print(filename)
        textcv=os.path.basename(filename)
        #print(textcv)
        main_image=cv2.imread(filename)
        textcv=os.path.basename(filename)

        main_image=cv2.putText(main_image,textcv,(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        self.tmp=main_image
        frame=cv2.cvtColor(main_image,cv2.COLOR_BGR2RGB)
        image=QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
    
        if filename:
            pixmap = QtGui.QPixmap(image).scaled(self.image.size(), 
                    QtCore.Qt.KeepAspectRatio)
            if pixmap.isNull():
                return
            self.image.setPixmap(pixmap)
            
    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()
    def load_imagetext(self):
        global filename
        global main_image
        textcv=os.path.basename(filename)
        print("text on file----------------"+textcv)
        main_image=cv2.imread(filename)
        main_image=cv2.putText(main_image,textcv,(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        self.tmp=main_image
        frame=cv2.cvtColor(main_image,cv2.COLOR_BGR2RGB)
        image=QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        if filename:
            pixmap = QtGui.QPixmap(image).scaled(self.image.size(), 
                    QtCore.Qt.KeepAspectRatio)
            if pixmap.isNull():
                return
            self.image.setPixmap(pixmap)
    def Close(self):
        print(self)
        self.MainWindow.close()
    def backButton_Action(self):
        """
        Go back to main page
        
        Arguments: None
        Returns: None
        """
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to Logout?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No )
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            from main import LoginWindow
            self.main = LoginWindow()
            self.main.show()

            self.Close()
        if buttonReply == QMessageBox.No:
            print('No clicked.')
    
        # sys.exit()
        # QtWidgets.qApp.quit
        # self.parentWidget().show()

    def helpButton (self):
        # msg_box_name.setIcon(QMessageBox.about(self, "Title", "Message"))
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(" 1. Config. - It is use to set all the configuration file \n\n 2. Open Dir - It is use to open a directory \n\n 3. Next Image -  It is used to access next image \n\n 4. Prev Image -  It is used to access previous image \n\n 5. Predict all - It is used to predict all the images \n\n 6. Back - It is used to access login page \n\n 7. Help - It gives Information of all the pages \n\n 8. Quit - It is used to quit the application ")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok)
        # msgBox.buttonClicked.connect(msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
        # msg_box_name.setIcon(QMessageBox.Information)

    def backButton(self):
        """
        Go back to main page
        
        Arguments: None
        Returns: None
        """
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to quit?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No )
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            sys.exit()
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        # if buttonReply == QMessageBox.Cancel:
        #     print('Cancel')
        # d = QDialog()
        # b1 = QPushButton("ok",d)
        # b1.move(50,50)
        # d.setWindowTitle("Dialog")
        # d.setWindowModality(Qt.ApplicationModal)
        # d.exec_()
        # text,ok =QInputDialog.getText(self, "enter","hjha")
        # print(text)
        # print(ok)
        # if ok:
        #     QCoreApplication.instance().quit
        # print('ypoooooooooooooooo')
        # self.quit()

        # self.parentWidget().show()
    # def next_image(self):
    #     global filename
    #     print(self.fileList,"asasa")
    #     # fileList = reversed(self.fileList)
    #     if self.fileList:
    #         try:
    #             print(self.dirIterator)
    #             filename = next(self.dirIterator)
    #             print(filename,"inside next")
    #             pixmap = QtGui.QPixmap(filename).scaled(self.image.size(), 
    #                 QtCore.Qt.KeepAspectRatio)
    #             if pixmap.isNull():
    #                 print("gvygj")
    #                 self.fileList.remove(filename)
    #                 self.next_image()
    #             else:
    #                 self.load_imagetext()
    #         except:
    #             self.dirIterator = iter(self.fileList)
    #             self.next_image()
    #     else:
    #         self.load_image()

    def next_image(self):
        global filename
        if self.currentIndex >= 0 and self.currentIndex < len(self.fileList)-1:
            self.currentIndex += 1
        else:
            self.currentIndex = 0
        pixmap = QtGui.QPixmap(self.fileList[self.currentIndex]).scaled(self.image.size(), QtCore.Qt.KeepAspectRatio)
        if pixmap.isNull():
            return
        self.image.setPixmap(pixmap)
        filename = self.fileList[self.currentIndex]
        self.load_imagetext()

    def pre_image(self):
        global filename
        if self.currentIndex > 0 and self.currentIndex <= len(self.fileList)-1:
            self.currentIndex -= 1
        else:
            self.currentIndex = len(self.fileList)-1
        pixmap = QtGui.QPixmap(self.fileList[self.currentIndex]).scaled(self.image.size(), QtCore.Qt.KeepAspectRatio)
        if pixmap.isNull():
            return
        self.image.setPixmap(pixmap)
        filename = self.fileList[self.currentIndex]
        self.load_imagetext()
    
    # def pre_image(self):
    #     global filename
    #     # print(self.fileList,"asasa")
    #     if self.fileList:
    #         try:
    #             filename = next(self.dirIterator)
    #             # print(filename,"inside next")
    #             pixmap = QtGui.QPixmap(filename).scaled(self.image.size(), 
    #                 QtCore.Qt.KeepAspectRatio)
    #             if pixmap.isNull():
    #                 # print("gvygj")
    #                 self.fileList.remove(filename)
    #                 self.next_image()
    #             else:
    #                 self.load_imagetext()
    #         except:
    #             self.dirIterator = iter(self.fileList)
    #             self.next_image()
    #     else:
    #         self.load_image()


    def save_image(self):
        global filename
        global main_image

        print(filename)
        splitted_filename = filename.split("\\")

        print(splitted_filename)
        
        result_dir=''
        for i in range(len(splitted_filename)-1):
            result_dir+=splitted_filename[i]+"/"

        img_name = splitted_filename[-1]

        if not os.path.exists(result_dir + "results"):
            print("MAKING RESULT FOLDER in "+ result_dir + "results")
            os.makedirs(result_dir + "results")

        fn = QFileDialog.getSaveFileName(directory=result_dir + 'results/' + img_name , filter="JPG(.jpg);;PNG(.png);;TIFF(.tiff);;BMP(.bmp)")[0]
        cv2.imwrite(fn,self.tmp)
        print('Image saved as:',fn)


    # def save_dir(self):
    #     global saving_dir
    #     saving_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)
    #     if saving_dir=='':
    #         return
    #     print(saving_dir)


    def open_dir(self):

        global filename
        global opening_dir

        opening_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)
        if opening_dir=='':
            return


        print("opening dir -----------:"+opening_dir)
        self.fileList = []
        for f in os.listdir(opening_dir):
            fpath = os.path.join(opening_dir, f)
            if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg','.bmp')):
                self.fileList.append(fpath)
        self.fileList.sort()
        self.dirIterator = iter(self.fileList)
        print(self.fileList)
        filename=self.fileList[0]
        self.load_imagetext()

    def save_predict(self):
        savePredict, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Predict", "", "Image File (*.png *.PNG *.jpg *.JPG)")
        pixmap2 = self.image.pixmap()
        pixmap2.save(savePredict)

    def predicted(self):
        values = InferenceSettings.getValuetry(self)
        prevDir = os.getcwd()
        os.chdir(values[0])
        train_cmd_str = './darknet detector test '+ values[3]+' ' + values[1]+ ' ' + values[2] + ' ' + filename +   ' -thresh 0.5 -dont_show' 
        print("\n calling ", train_cmd_str,"\n")
        subprocess.call(train_cmd_str,shell=True)
        imgDetect = 'predictions.jpg' #pass prediction.jpg
        print(filename)
        print(imgDetect)

        main_image=cv2.imread(imgDetect)
        textcv=os.path.basename(filename)
        main_image=cv2.putText(main_image,textcv,(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        self.tmp=main_image
        frame=cv2.cvtColor(main_image,cv2.COLOR_BGR2RGB)

        image=QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
    
        if imgDetect:
            pixmap = QtGui.QPixmap(image).scaled(self.image.size(), 
                    QtCore.Qt.KeepAspectRatio)
            if pixmap.isNull():
                return
            self.image.setPixmap(pixmap)
            # self.load_imagetext()

        #self.save_predict()
        #self.save_image()
    def _createStatusBar(self):
        """
        Create status bar to display messages
        
        Arguments: None
        Returns: None
        """
        self.statusbar = self.statusBar()
        # Adding a temporary message
        self.statusBar().showMessage("Ready", 10000)
    def configuration(self):
        self.settings = QtCore.QSettings("TIFR", "Cms-App")
        # MainWindow = QtWidgets.QMainWindow()
        values = InferenceSettings.launch(self)
        
        if values:
    
            self.darknetPath = values[0]
            self.configPath = values[1]
            self.weightPath = values[2]
            self.dataPath = values[3]
            
            self.settings.setValue("inferenceDarknet", self.darknetPath)
            self.settings.setValue("inferenceConfig", self.configPath)
            self.settings.setValue("inferenceWeights", self.weightPath)
            self.settings.setValue("inferenceData", self.dataPath)
            print(self.darknetPath,'9999999999')
            self.statusBar().showMessage("New Settings Saved", 10000)
            
        else:
            self.statusBar().showMessage("New settings not saved. Press OK after making changes to save", 10000)
      
    def predict_all(self):
        global opening_dir
        global filename
        print("IN PREDICT ALL FUNCTION")
        test_Path = opening_dir
        print(test_Path)
        d=0
        f_name =[]
        values = InferenceSettings.getValuetry(self)
        print(values[0],"hooooooooooooooooooooooooooooo")
        # print(prevDir)
        prevDir = os.getcwd()
        print(prevDir)
        os.chdir(values[0])
        for images in os.listdir(test_Path):
            if images.endswith(('.png', '.jpg', '.jpeg','.bmp')):
                print(images)
                pref ='chmod +x ' + values[0]
                subprocess.call(pref,shell=True)
                img_path= filename.split("/")
                print(img_path,"sddddddddddddddddddd")
                img = images.split(".")
                # commands = " ./darknet  detector test" + ' ' + values[3] + ' ' + values[1]+ ' ' + values[2] + ' ' + opening_dir + "/" + images + " -thresh 0.5 -dont_show"
                commands = './darknet detector test '+ values[3]+' ' + values[1]+ ' ' + values[2] + ' ' + opening_dir + "/" + images +  ' -thresh 0.5 -dont_show -ext_output < '+ opening_dir + "/" + images+' > results/'+img[0]+'.txt '
                print('done')
                textFileName = 'results/'+img[0]+'.txt'
                
                print(commands)
                os.system(commands)
                a_file = open(textFileName, "r")
                lines = a_file.readlines()
                a_file.close()
                del lines[:12]
                new_file = open(textFileName, "w+")
                for line in lines:
                    new_file.write(line)
                new_file.close()
                print(filename,"gggggggggggggggggg")
                # image_path = "/content/gdrive/MyDrive/test3/predictions_%d.jpg"%d
                # print(image_path, " ---------------------------------------")
                print(images,"rashmiiiiiiiiiiiiiiiiiiiiiiiii")
                main_image_1=cv2.imread('predictions.jpg')
                main_image_1=cv2.putText(main_image_1,img[0] + ".jpg",(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                shutil.copy('predictions.jpg',  "results/"+ img[0] +".jpg")
                f_name.append( values[0]+"/results/" + img[0] + ".jpg")
                print("done")

        self.fileList = []
        for f in os.listdir( values[0] + "/results/"):
            fpath = os.path.join(opening_dir, f)
            print(fpath,"amit")
            if f.endswith(('.png', '.jpg', '.jpeg','.bmp')):
                self.fileList.append(fpath)
        self.fileList.sort()
        self.dirIterator = iter(self.fileList)
        print(self.fileList)
        filename=self.fileList[0]
        predfile = filename.split('/')[-1]
        imgDetect = "results/"+predfile  #pass prediction.jpg
        filename = values[0] + "/" + imgDetect
	
        print(filename)

        main_image=cv2.imread(imgDetect)
        #main_image=cv2.putText(main_image,textcv,(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        self.tmp=main_image
        main_image_1=cv2.imread('predictions.jpg')
        main_image_1=cv2.putText(main_image_1,predfile,(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        frame=cv2.cvtColor(main_image_1,cv2.COLOR_BGR2RGB)

        image=QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
    
        if imgDetect:
            print(predfile,"gbjhkuhjbjhnnkhn")
            
            pixmap = QtGui.QPixmap(image).scaled(self.image.size(), 
                    QtCore.Qt.KeepAspectRatio)
            if pixmap.isNull():
                return
            self.image.setPixmap(pixmap)
        main_image_1=cv2.imread('predictions.jpg')
        main_image_1=cv2.putText(main_image_1,img[0] + ".jpg",(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        self.fileList = f_name[:]
        #for f in os.listdir( "/home/root1/cms/darknet/results/"):
            #fpath = os.path.join()
           # print(fpath,"amit")
          #  if f.endswith(('.png', '.jpg', '.jpeg','.bmp')):
         #       self.fileList.append(fpath)
        #print(self.fileList, "predict")
        os.chdir(prevDir)


            
            

   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
