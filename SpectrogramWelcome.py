# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpectrogramWelcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import numpy as np
from scipy import signal
import wave
from scipy.io.wavfile import write
import matplotlib.pyplot as plot
import pylab
from PIL import Image
from pydub import AudioSegment
import matplotlib.image as mpimg
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import (generate_binary_structure,iterate_structure, binary_erosion)
import imagehash
import pickle
from operator import itemgetter
from operator import add
from SpectrogramTable import Ui_Table





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 600)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.WelcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.WelcomeLabel.setEnabled(False)
        self.WelcomeLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.WelcomeLabel.setStyleSheet("color:blue ; background-color:white")
        self.WelcomeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.WelcomeLabel.setLineWidth(4)
        self.WelcomeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.verticalLayout.addWidget(self.WelcomeLabel)
        self.gridLayout_8.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet("color:rgb(255, 3, 3)")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_4.addWidget(self.horizontalSlider)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color:rgb(149, 149, 255);color:black")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_4.addWidget(self.spinBox)
        self.Browse1 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Browse1.sizePolicy().hasHeightForWidth())
        self.Browse1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Browse1.setFont(font)
        self.Browse1.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.Browse1.setObjectName("Browse1")
        self.verticalLayout_4.addWidget(self.Browse1)
        self.gridLayout_8.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Browse2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Browse2.sizePolicy().hasHeightForWidth())
        self.Browse2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Browse2.setFont(font)
        self.Browse2.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.Browse2.setObjectName("Browse2")
        self.verticalLayout_3.addWidget(self.Browse2)
        self.gridLayout_8.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.Mix = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Mix.setFont(font)
        self.Mix.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.Mix.setObjectName("Mix")
        self.gridLayout_8.addWidget(self.Mix, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Browse2.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.Mix.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WelcomeLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ff0000;\">Welcome</span></p></body></html>"))
        self.WelcomeLabel.setText(_translate("MainWindow", "Welcome"))
        self.Browse1.setText(_translate("MainWindow", "Choose your First Song "))
        self.Browse2.setText(_translate("MainWindow", "Choose your Second Song "))
        self.Mix.setText(_translate("MainWindow", "MIX and Show Similarity"))
        self.horizontalSlider.valueChanged.connect(self.SliderDetector)
        self.spinBox.valueChanged.connect(self.SpinDetector)
        self.Browse1.clicked.connect(lambda:self.Browse(1))
        self.Browse2.clicked.connect(lambda:self.Browse(2))
        self.Mix.clicked.connect(lambda:self.Mixing(MainWindow))



    def Browse(self,i):
        filename=QtWidgets.QFileDialog.getOpenFileName()
        directory=filename[0]
        # Time to miliseconds
        startTime = 0*60*1000+0*1000
        endTime = 1*60*1000+0*1000 
        if(i == 1):
            # Opening file and extracting segment
            self.FirstSong = AudioSegment.from_mp3( directory)
            self.FirstSong = self.FirstSong[startTime:endTime]
            self.FirstSong.export( 'FirstCroppedSong.wav', format="wav")
            self.Browse2.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.spinBox.setEnabled(True)
        
            
        elif(i == 2):
            # Opening file and extracting segment
            self.SecondSong = AudioSegment.from_mp3( directory)
            self.SecondSong = self.SecondSong[startTime:endTime]
            self.SecondSong.export( 'SecondCroppedSong.wav', format="wav")
            self.Mix.setEnabled(True)
            
            


    def Mixing(self,MainWindow):
        self.FirstSong=wave.open("FirstCroppedSong.wav",'r')
        FirstSongData=pylab.fromstring(self.FirstSong.readframes(-1),'Int16')
        self.SecondSong=wave.open("SecondCroppedSong.wav",'r')
        SecondSongData=pylab.fromstring(self.SecondSong.readframes(-1),'Int16')
        if(len(FirstSongData)!=len(SecondSongData)):
            _translate = QtCore.QCoreApplication.translate
            self.WelcomeLabel.setText(_translate("MainWindow", "Please Enter The Songs With The Same Properties 'Same Bitrate,Same Sampling Frequency,etc....' "))
            self.WelcomeLabel.setStyleSheet("color:red ; background-color:white")
            self.Browse2.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.Mix.setEnabled(False)
        else:    
            SliderValue=self.horizontalSlider.value()
            FirstSongPortion=SliderValue/100
            SecondSongPortion=1-FirstSongPortion
            MixedSong=np.add(((FirstSongPortion)*(np.array(FirstSongData))),((SecondSongPortion)*(np.array(SecondSongData))))
            write("MixedSong.wav", 88200, MixedSong)
            self.FirstSong.close
            self.SecondSong.close
            plotting = pylab.subplot()
            plotting.get_xaxis().set_visible(False)
            plotting.get_yaxis().set_visible(False)
            spectrogram= pylab.specgram(MixedSong,NFFT=4096,Fs=44100,window=pylab.window_hanning,noverlap=int(4096 *0.5))[0]
            # apply log transform since specgram() returns linear array
            spectrogram = 10 * np.log10(spectrogram)
            spectrogram[spectrogram == -np.inf] = 0  # replace infs with zeros
            self.get_2D_peaks(spectrogram, amp_min=10)
            hashvalue=imagehash.phash(Image.open('spectrogramPeaks.png'))
            with open('Database.pkl', 'rb') as f:
                Database = pickle.load(f)
            
            TableArr = []
            for i in Database:
                Final = hashvalue - i[1]
                Final = 100 - Final
                TableArr.append([i[0],Final])
            TableArr = sorted(TableArr, key=itemgetter(1))
            TableArr = TableArr[::-1]
            Temp=TableArr
            TableArr=[]
            for j in range(10) :
                TableArr.append(Temp[j])
                
            self.OpenTable(MainWindow,TableArr)    

            CD = os.getcwd()
            os.remove(CD+'/spectrogramPeaks.png')
            os.remove(CD+'/FirstCroppedSong.wav')
            os.remove(CD+'/SecondCroppedSong.wav')
            os.remove(CD+'/MixedSong.wav')
        


       
    


    def get_2D_peaks(self,arr2D, amp_min=10):
        struct = generate_binary_structure(2, 1)
        neighborhood = iterate_structure(struct, 20)
        # find local maxima using our filter shape
        local_max = maximum_filter(arr2D, footprint=neighborhood) == arr2D
        background = (arr2D == 0)
        eroded_background = binary_erosion(background, structure=neighborhood,border_value=1)
        # Boolean mask of arr2D with True at peaks (Fixed deprecated boolean operator by changing '-' to '^')
        detected_peaks = local_max ^ eroded_background
        # extract peaks
        amps = arr2D[detected_peaks]
        j, i = np.where(detected_peaks)
        # filter peaks
        amps = amps.flatten()
        peaks = zip(i, j, amps)
        peaks_filtered = filter(lambda x: x[2]>amp_min, peaks) # freq, time, amp
        # get indices for frequency and time
        frequency_idx = []
        time_idx = []
        for x in peaks_filtered:
            frequency_idx.append(x[1])
            time_idx.append(x[0])
        # scatter of the peaks
        fig,ax = pylab.subplots()
        ax.imshow(arr2D)
        ax.scatter(time_idx, frequency_idx)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        pylab.gca().invert_yaxis()
        pylab.savefig('spectrogramPeaks.png',bbox_inches='tight',pad_inches=0)




    def SliderDetector(self):
        val=self.horizontalSlider.value()
        self.spinBox.setValue(val)
                 
    def SpinDetector(self ,i):
        val=self.spinBox.value()
        self.horizontalSlider.setValue(val)



    def OpenTable(self,MainWindow,data):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Table(data)
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()



    # Creating Database for songs "one time use"   
    # def CreateDatabase(self):
    #     CD = os.getcwd()
    #     Database = []
    #     c = 1
    #     for filename in os.listdir(CD):
    #         if filename.endswith(".mp3"):
    #             # Time to miliseconds
    #             startTime = 0*60*1000+0*1000
    #             endTime = 1*60*1000+0*1000
    #             # Opening file and extracting segment
    #             song = AudioSegment.from_mp3( CD+'/'+filename)
    #             extract = song[startTime:endTime]
    #             # Saving
    #             extract.export( 'min.wav', format="wav")
    #             Songdata=wave.open("min.wav",'r')
    #             signalData=pylab.fromstring(Songdata.readframes(-1),'Int16')
    #             Songdata.close
    #             plotting = pylab.subplot()
    #             plotting.get_xaxis().set_visible(False)
    #             plotting.get_yaxis().set_visible(False)
    #             spectrogram= pylab.specgram(signalData,NFFT=4096,Fs=44100,window=pylab.window_hanning,noverlap=int(4096 *0.5))[0]
    #             spectrogram = 10 * np.log10(spectrogram)
    #             spectrogram[spectrogram == -np.inf] = 0  # replace infs with zeros
    #             self.get_2D_peaks(spectrogram, amp_min=10)
    #             hashvalue=imagehash.phash(Image.open('spectrogramPeaks.png'))
    #             SongName=os.path.splitext(filename)[0]
    #             Database.append([SongName,hashvalue])
    #             print(c)
    #             c=c+1
    #             os.remove(CD+'/min.wav')
    #             os.remove(CD+'/spectrogramPeaks.png')
    #     with open('Database.pkl', 'wb') as f:
    #         pickle.dump(Database, f)

