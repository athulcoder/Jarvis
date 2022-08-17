

from xmlrpc.client import DateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from datetime import datetime
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
import pyttsx3
from speech_recognition import Microphone, Recognizer
import os
import wave
import time
import webbrowser
from PyQt5.QtWidgets import QLabel
import wikipedia
import pywhatkit
import random
import pyaudio

listener = Recognizer()
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish():
    current_time = datetime.now().strftime("%I:%M")
    hour = int(datetime.now().strftime('%H'))
    if 0 <= hour < 12:
        print('Good Morning Sir')
        speak("Good Morning Sir")
        speak("It's " + current_time + "am ")
    elif 12 < hour < 18:
        print("Good Afternoon Sir")
        speak('Good Afternoon Sir')
        speak("It's " + current_time+"pm ")
    else:
        print("Good Evening Sir")
        speak('Good Evening Sir')



class MainThread(QThread):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.command = None

    def __int__(self):
        super(MainThread, self).__init__()

    def run(self):
        wish()
        self.jarvis()

    def speech_to_text(self):

        try:
            with Microphone() as source:
                print('lisenting.....')
                voice = listener.listen(source)
                try:
                    print('Recognizing...')
                    command = listener.recognize_google(voice)
                    print(f'User : {command}')
                    command = command.lower()
                    if command == '':
                        self.speech_to_text()
                except Exception:
                    speak("Sir ...Is there any other thing to do ?")
                    self.jarvis()
        except Exception as e:
            print(e)
            print("Something went wrong sir")
            speak("Something went wrong sir")
        command = command.lower()
        return command

    def jarvis(self):
        pyaudio.PyAudio()
        while True:
            self.command = self.speech_to_text()
            if 'jarvis' in self.command:
                self.command = self.command.replace('jarvis', '')
            if ' hi' in self.command or 'hello' in self.command:
                print(f"computer : Hello , Sir")
                speak("hello  sir...How can I help you?")




            elif "open google" in self.command:
                print(f'computer :  Opening Google')
                speak(' OK ...Opening Google ...')
                webbrowser.open("google.com")
            elif 'shutdown' in self.command:
                os.system('shutdown /s /t 1')

            elif 'open youtube' in self.command:
                print(f'computer : Opening Youtube')
                speak('OK...Opening Youtube ...')
                webbrowser.open('youtube.com')
            elif 'play' in self.command:
                song = self.command.replace("play", "")
                print(f" computer : playing {song}")
                speak(f"OK...playing {song}")
                pywhatkit.playonyt(song)
            elif 'open cmd' in self.command or 'open command prompt' in self.command:
                print(f'computer : Opening Command Prompt')
                speak('Ok...Opening Command Prompt ...')
                dir_cmd = 'C:\\Users\\athul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu' \
                          '\\Programs\\System Tools\\Command Prompt.lnk'
                os.startfile(dir_cmd)
            elif 'open my website' in self.command:
                print(f'computer : Opening Your Website')
                speak('OK...Opening Your Website...')
                webbrowser.open('https:\\athulcoder.github.io')
            elif 'open pycharm' in self.command:
                print(f'computer : Opening Pycharm...')
                speak('OK...Opening Pycharm...')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains'
                             '\\PyCharm Community Edition 2022.1.3.lnk')
            elif 'open whatsapp' in self.command:
                print(f'computer : Opening Your Whatsapp')
                speak('OK...Opening WhatsApp.')
                webbrowser.open('https://web.whatsapp.com/')
            elif 'open instagram' in self.command:
                print(f'computer : Opening Instagram')
                speak('OK...Opening Instagram.')
                webbrowser.open('https://instagram.com/')
            elif 'quit' in self.command or 'bye' in self.command or 'stop' in self.command or 'exit' in self.command or 'sleep' in self.command:
                speak("OK Sir...You can call Me anytime")
                sys.exit(app.exit())

            elif 'wikipedia' in self.command:
                self.command = self.command.replace("wikipedia", "")
                search = wikipedia.summary(self.command, sentences=2)
                print(search)
                speak(f'According to Wikipedia...{search}')

            elif 'notepad' in self.command:
                print(f'computer : Opening Notepad')
                speak('OK...Opening Notepad.')
                os.startfile('C:\\Windows\\notepad.exe')
            elif 'song' in self.command:
                print(f'computer : searching')
                speak('OK...playing song From your Computer.')
                song_list = os.listdir('D:\\songs')
                list_index = random.randint(0,59)
                os.startfile("D:\\songs\\"+ song_list[list_index])
            else:
                print("computer : Sorry Sir ... Please say that again")
                speak('Sorry sir...Please say that again ')


online = MainThread()


class Ui_Form(object):



    def on_run_clicked(self):
        online.start()
        self.movie = QMovie("lib/circle gif.gif")
        self.circle_1.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/circle gif.gif")
        self.circle_2.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/circle gif.gif")
        self.circle_3.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/load gif.gif")
        self.initial_loading.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/new 2.gif")
        self.load_1.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/new 2.gif")
        self.load_2.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/new 2.gif")
        self.load_3.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/new 2.gif")
        self.load_5.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/new 2.gif")
        self.load_6.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/load gif 2.gif")
        self.circle_4.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/load gif 2.gif")
        self.circle_5.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/new type.gif")
        self.circle_6.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/new type.gif")
        self.circle_7.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie("lib/iron man.gif")
        self.iron_man.setMovie(self.movie)
        self.movie.start()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1696, 829)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-10, -60, 1771, 941))
        self.background.setAutoFillBackground(False)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("lib/pure black.webp"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.circle_1 = QtWidgets.QLabel(Form)
        self.circle_1.setGeometry(QtCore.QRect(1540, 170, 161, 161))
        self.circle_1.setText("")
        self.circle_1.setPixmap(QtGui.QPixmap("lib/circle gif.gif"))
        self.circle_1.setScaledContents(True)
        self.circle_1.setObjectName("circle_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 301, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("lib/bar.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.initial_loading = QtWidgets.QLabel(Form)
        self.initial_loading.setGeometry(QtCore.QRect(0, -20, 451, 291))
        self.initial_loading.setText("")
        self.initial_loading.setPixmap(QtGui.QPixmap("lib/load gif.gif"))
        self.initial_loading.setScaledContents(True)
        self.initial_loading.setObjectName("initial_loading")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 520, 55, 16))
        self.label.setObjectName("label")
        self.circle_5 = QtWidgets.QLabel(Form)
        self.circle_5.setGeometry(QtCore.QRect(930, 640, 171, 161))
        self.circle_5.setText("")
        self.circle_5.setPixmap(QtGui.QPixmap("lib/load gif 2.gif"))
        self.circle_5.setScaledContents(True)
        self.circle_5.setObjectName("circle_5")
        self.circle_7 = QtWidgets.QLabel(Form)
        self.circle_7.setGeometry(QtCore.QRect(-40, 630, 271, 201))
        self.circle_7.setText("")
        self.circle_7.setPixmap(QtGui.QPixmap("lib/new type.gif"))
        self.circle_7.setScaledContents(True)
        self.circle_7.setObjectName("circle_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 490, 301, 141))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("lib/bar.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.load_1 = QtWidgets.QLabel(Form)
        self.load_1.setGeometry(QtCore.QRect(-10, 10, 191, 41))
        self.load_1.setText("")
        self.load_1.setPixmap(QtGui.QPixmap("lib/new 2.gif"))
        self.load_1.setScaledContents(True)
        self.load_1.setObjectName("load_1")
        self.load_2 = QtWidgets.QLabel(Form)
        self.load_2.setGeometry(QtCore.QRect(180, 10, 191, 41))
        self.load_2.setText("")
        self.load_2.setPixmap(QtGui.QPixmap("lib/new 2.gif"))
        self.load_2.setScaledContents(True)
        self.load_2.setObjectName("load_2")
        self.load_3 = QtWidgets.QLabel(Form)
        self.load_3.setGeometry(QtCore.QRect(370, 10, 191, 41))
        self.load_3.setText("")
        self.load_3.setPixmap(QtGui.QPixmap("lib/new 2.gif"))
        self.load_3.setScaledContents(True)
        self.load_3.setObjectName("load_3")
        self.date = QtWidgets.QLabel(Form)
        self.date.setGeometry(QtCore.QRect(70, 380, 191, 51))
        self.date.setScaledContents(True)
        self.date.setObjectName("date")
        self.weekday = QtWidgets.QLabel(Form)
        self.weekday.setGeometry(QtCore.QRect(50, 540, 231, 41))
        self.weekday.setScaledContents(True)
        self.weekday.setObjectName("weekday")
        self.load_5 = QtWidgets.QLabel(Form)
        self.load_5.setGeometry(QtCore.QRect(560, 10, 191, 41))
        self.load_5.setText("")
        self.load_5.setPixmap(QtGui.QPixmap("lib/new 2.gif"))
        self.load_5.setScaledContents(True)
        self.load_5.setObjectName("load_5")
        self.load_6 = QtWidgets.QLabel(Form)
        self.load_6.setGeometry(QtCore.QRect(750, 10, 191, 41))
        self.load_6.setText("")
        self.load_6.setPixmap(QtGui.QPixmap("lib/new 2.gif"))
        self.load_6.setScaledContents(True)
        self.load_6.setObjectName("load_6")
        self.circle_6 = QtWidgets.QLabel(Form)
        self.circle_6.setGeometry(QtCore.QRect(160, 630, 271, 201))
        self.circle_6.setText("")
        self.circle_6.setPixmap(QtGui.QPixmap("lib/new type.gif"))
        self.circle_6.setScaledContents(True)
        self.circle_6.setObjectName("circle_6")
        self.circle_4 = QtWidgets.QLabel(Form)
        self.circle_4.setGeometry(QtCore.QRect(640, 640, 171, 161))
        self.circle_4.setText("")
        self.circle_4.setPixmap(QtGui.QPixmap("lib/load gif 2.gif"))
        self.circle_4.setScaledContents(True)
        self.circle_4.setObjectName("circle_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(410, 610, 81, 51))
        self.label_6.setObjectName("label_6")
        self.jarvis_logo = QtWidgets.QLabel(Form)
        self.jarvis_logo.setGeometry(QtCore.QRect(700, 510, 331, 161))
        self.jarvis_logo.setText("")
        self.jarvis_logo.setPixmap(QtGui.QPixmap("lib/jarvis logo.png"))
        self.jarvis_logo.setScaledContents(True)
        self.jarvis_logo.setObjectName("jarvis_logo")
        self.iron_man = QtWidgets.QLabel(Form)
        self.iron_man.setGeometry(QtCore.QRect(620, 120, 481, 501))
        self.iron_man.setText("")
        self.iron_man.setPixmap(QtGui.QPixmap("lib/iron man.gif"))
        self.iron_man.setScaledContents(True)
        self.iron_man.setObjectName("iron_man")
        self.circle_3 = QtWidgets.QLabel(Form)
        self.circle_3.setGeometry(QtCore.QRect(1540, 480, 161, 161))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.circle_3.setFont(font)
        self.circle_3.setText("")
        self.circle_3.setPixmap(QtGui.QPixmap("lib/circle gif.gif"))
        self.circle_3.setScaledContents(True)
        self.circle_3.setObjectName("circle_3")
        self.circle_2 = QtWidgets.QLabel(Form)
        self.circle_2.setGeometry(QtCore.QRect(1540, 320, 161, 161))
        self.circle_2.setText("")
        self.circle_2.setPixmap(QtGui.QPixmap("lib/circle gif.gif"))
        self.circle_2.setScaledContents(True)
        self.circle_2.setObjectName("circle_2")
        self.run_btn = QtWidgets.QPushButton(Form)
        self.run_btn.setGeometry(QtCore.QRect(1380, 770, 111, 31))
        self.run_btn.setAutoFillBackground(False)
        self.run_btn.setStyleSheet("background-color:orange;\n"
"border-radius:15px;\n"
"text-align:center;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"color:blue;")
        self.run_btn.clicked.connect(self.on_run_clicked)
        self.run_btn.setAutoDefault(False)
        self.run_btn.setDefault(False)
        self.run_btn.setFlat(False)
        self.run_btn.setObjectName("run_btn")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(1530, 770, 93, 28))
        self.exit_btn.setStyleSheet("background-color:red;\n"
"border-radius: 12px;\n"
"text-align:center;\n"
"font-size : 20px;\n"
"font-weight:bold;\n"
"color:black;\n"
"")

        self.exit_btn.setObjectName("exit_btn")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(1340, 20, 256, 91))
        self.textBrowser.setStyleSheet("background:white;")
        self.textBrowser.setObjectName("textBrowser")
        self.listen_btn = QtWidgets.QPushButton(Form)
        self.listen_btn.setGeometry(QtCore.QRect(1240, 770, 101, 31))
        self.listen_btn.setStyleSheet("background-color:green;\n"
"border-radius:13px;\n"
"text-align:center;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"color:red;")
        self.listen_btn.setObjectName("pushButton")
        self.background.raise_()
        self.circle_6.raise_()
        self.circle_1.raise_()
        self.initial_loading.raise_()
        self.label.raise_()
        self.circle_7.raise_()
        self.label_8.raise_()
        self.load_1.raise_()
        self.load_2.raise_()
        self.load_3.raise_()
        self.weekday.raise_()
        self.load_5.raise_()
        self.load_6.raise_()
        self.label_6.raise_()
        self.iron_man.raise_()
        self.jarvis_logo.raise_()
        self.circle_4.raise_()
        self.circle_5.raise_()
        self.label_3.raise_()
        self.date.raise_()
        self.circle_3.raise_()
        self.circle_2.raise_()
        self.run_btn.raise_()
        self.exit_btn.raise_()
        self.textBrowser.raise_()
        self.listen_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        

    def retranslateUi(self, Form):
        current_date = datetime.now().strftime("%d  %b  %y")
        current_time = datetime.now().strftime("%I: %M :%S")
        current_weekday = datetime.now().strftime('%A')

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.date.setText(_translate("Form", F"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#11814d;\" > {current_date} </span></p></body></html>"))
        self.weekday.setText(_translate("Form", F"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#3aa880;\">{current_weekday}</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.run_btn.setText(_translate("Form", "RUN"))
        self.exit_btn.setText(_translate("Form", "EXIT"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
F"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\">{current_time}</span></p></body></html>"))
        self.listen_btn.setText(_translate("Form", "Listen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
