# Project: Blackjack Card Counter
# Program Name: BlackjackCardCounter.py
# Author: Allen Li
# Date Created: 8/16/2019
# Version: 0.1

from PyQt5 import QtCore, QtGui, QtWidgets
import re

from PyQt5.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar


# Generated with Qt Designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deckCount = QtWidgets.QSpinBox(self.centralwidget)
        self.deckCount.setGeometry(QtCore.QRect(30, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.deckCount.setFont(font)
        self.deckCount.setMinimum(1)
        self.deckCount.setProperty("value", 6)
        self.deckCount.setObjectName("deckCount")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.shuffled = QtWidgets.QPushButton(self.centralwidget)
        self.shuffled.setGeometry(QtCore.QRect(20, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.shuffled.setFont(font)
        self.shuffled.setObjectName("shuffled")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.textInput = QtWidgets.QLineEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(20, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.textInput.setFont(font)
        self.textInput.setObjectName("textInput")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.countingSystem = QtWidgets.QComboBox(self.centralwidget)
        self.countingSystem.setGeometry(QtCore.QRect(30, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.countingSystem.setFont(font)
        self.countingSystem.setObjectName("countingSystem")
        self.countingSystem.addItem("")
        self.countingSystem.addItem("")
        self.countingSystem.addItem("")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.trueCountWidget = QtWidgets.QWidget(self.centralwidget)
        self.trueCountWidget.setGeometry(QtCore.QRect(190, 80, 301, 171))
        self.trueCountWidget.setObjectName("trueCountWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.trueCountWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.remainingCardWidget = QtWidgets.QWidget(self.centralwidget)
        self.remainingCardWidget.setGeometry(QtCore.QRect(20, 289, 471, 171))
        self.remainingCardWidget.setObjectName("remainingCardWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.remainingCardWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame.raise_()
        self.deckCount.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.shuffled.raise_()
        self.label_3.raise_()
        self.lcdNumber.raise_()
        self.textInput.raise_()
        self.label_4.raise_()
        self.countingSystem.raise_()
        self.label_5.raise_()
        self.trueCountWidget.raise_()
        self.remainingCardWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number of Decks"))
        self.label_2.setText(_translate("MainWindow", "Card Values (2-10, J-A)"))
        self.shuffled.setText(_translate("MainWindow", "Shuffled"))
        self.label_3.setText(_translate("MainWindow", "True Count"))
        self.label_4.setText(_translate("MainWindow", "Card Counting System"))
        self.countingSystem.setItemText(0, _translate("MainWindow", "Wong Halves"))
        self.countingSystem.setItemText(1, _translate("MainWindow", "Omega II"))
        self.countingSystem.setItemText(2, _translate("MainWindow", "Hi-Lo"))
        self.label_5.setText(_translate("MainWindow", "Remaining Card Probabilities"))


cardValues = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
groupedCardValues = ["2","3","4","5","6","7","8","9","10 - K","A"]

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        self.remainingCardCount = 312
        self.individualCardCount = {}
        self.individualCardCount.update(dict.fromkeys(cardValues, 24))
        self.totalRunningCount = 0
        self.trueCount = 0
        self.trueCountHistory = [0]
        
        self.mousePressEvent = self.deselect
        self.keyPressEvent = self.inputCardValues
        self.countingSystem.currentTextChanged.connect(self.reset)
        self.deckCount.valueChanged.connect(self.reset)
        self.shuffled.clicked.connect(self.reset)
        
        self.textInput.setFocus()

    def inputCardValues(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            inputText = self.textInput.text().upper()
            if inputText == "":
                return
            inputFormattedText = inputText.replace(",", " ")
            inputCardValueList = re.split("\s", inputFormattedText)
            formattedCardValueList = [value for value in inputCardValueList if value in cardValues]
            for value in formattedCardValueList:
                self.individualCardCount[value] -= 1
            countingSystemText = self.countingSystem.currentText()
            if countingSystemText == "Hi-Lo":
                self.hiLo(formattedCardValueList)
            elif countingSystemText == "Omega II":
                self.omega(formattedCardValueList)
            else:
                self.wong(formattedCardValueList)
    
    def hiLo(self, formattedCardValueList):
        cardCount = 0
        runningCount = 0
        for value in formattedCardValueList:
            if value in ["2","3","4","5","6"]:
                runningCount += 1
            elif value in ["10","J","Q","K","A"]:
                runningCount -= 1
            cardCount += 1
        self.textInput.setText("")
        self.updateOutput(cardCount, runningCount)

    def omega(self, formattedCardValueList):
        cardCount = 0
        runningCount = 0
        for value in formattedCardValueList:
            if value in ["2","3","7"]:
                runningCount += 1
            elif value in ["4","5","6"]:
                runningCount += 2
            elif value in ["9"]:
                runningCount -= 1
            elif value in ["10","J","Q","K"]:
                runningCount -= 2
            cardCount += 1
        self.textInput.setText("")
        self.updateOutput(cardCount, runningCount)

    def wong(self, formattedCardValueList):
        cardCount = 0
        runningCount = 0
        for value in formattedCardValueList:
            if value in ["2","7"]:
                runningCount += 0.5
            elif value in ["3","4","6"]:
                runningCount += 1
            elif value in ["5"]:
                runningCount += 1.5
            elif value in ["9"]:
                runningCount -= 0.5
            elif value in ["10","J","Q","K","A"]:
                runningCount -= 1
            cardCount += 1
        self.textInput.setText("")
        self.updateOutput(cardCount, runningCount)
    
    def addCountsPlot(self):
        self.trueCountFigure = Figure()
        self.trueCountFigure.subplots_adjust(left=0.13,right=0.94,bottom=0.1,top=0.9)
        self.trueCountPlot = self.trueCountFigure.add_subplot(1,1,1)
        self.trueCountPlot.axhline(0, linewidth=0.6, color='black')
        self.trueCountPlot.plot(self.trueCountHistory, "C0-")
        self.trueCountPlot.axes.set_ylim([-10,10])
        self.trueCountPlot.tick_params(labelsize=7)
        self.trueCountPlot.axes.get_xaxis().set_visible(False)
        self.trueCountCanvas = FigureCanvas(self.trueCountFigure)
        self.trueCountWidget.layout().addWidget(self.trueCountCanvas)
        self.trueCountCanvas.draw()

    def updateCountsPlot(self):
        self.trueCountPlot.remove()
        self.trueCountPlot = self.trueCountFigure.add_subplot(1,1,1)
        self.trueCountPlot.axhline(0, linewidth=0.6, color='black')
        self.trueCountPlot.plot(self.trueCountHistory, "C0-")
        self.trueCountPlot.axes.set_ylim([-10,10])
        self.trueCountPlot.tick_params(labelsize=7)
        self.trueCountPlot.axes.get_xaxis().set_visible(False)
        self.trueCountCanvas.draw()

    def addremainingCardHist(self):
        self.remainingCardFigure = Figure()
        self.remainingCardFigure.subplots_adjust(left=0.08,right=0.965,bottom=0.16,top=0.9)
        self.remainingCardBar = self.remainingCardFigure.add_subplot(1,1,1)
        defaultRemainingCardProbabilities = [1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,4.0/13,1.0/13]
        self.remainingCardBar.bar(groupedCardValues, height=defaultRemainingCardProbabilities)
        for cardValue, probability in enumerate(defaultRemainingCardProbabilities):
            self.remainingCardBar.text((groupedCardValues[cardValue]), probability+max(defaultRemainingCardProbabilities)*0.05, str(probability)[:5], ha='center', fontsize=6)
        self.remainingCardBar.set_ylim(top=max(defaultRemainingCardProbabilities)*1.2)
        self.remainingCardBar.tick_params(labelsize=7)
        self.remainingCardCanvas = FigureCanvas(self.remainingCardFigure)
        self.remainingCardWidget.layout().addWidget(self.remainingCardCanvas)
        self.remainingCardCanvas.draw()

    def updateremainingCardHist(self):
        groupedCardCountList = [ self.individualCardCount["2"],
                                 self.individualCardCount["3"],
                                 self.individualCardCount["4"],
                                 self.individualCardCount["5"],
                                 self.individualCardCount["6"],
                                 self.individualCardCount["7"],
                                 self.individualCardCount["8"],
                                 self.individualCardCount["9"],
                                 self.individualCardCount["10"] + self.individualCardCount["J"] + self.individualCardCount["Q"] + self.individualCardCount["K"],
                                 self.individualCardCount["A"] ]
        remainingCardProbabilities = [ count / self.remainingCardCount for count in groupedCardCountList]
        self.remainingCardBar.remove()
        self.remainingCardBar = self.remainingCardFigure.add_subplot(1,1,1)
        self.remainingCardBar.bar(groupedCardValues, height=remainingCardProbabilities)
        for cardValue, probability in enumerate(remainingCardProbabilities):
            self.remainingCardBar.text((groupedCardValues[cardValue]), probability+max(remainingCardProbabilities)*0.05, str(probability)[:5], ha='center', fontsize=6)
        self.remainingCardBar.set_ylim(top=max(remainingCardProbabilities)*1.2)
        self.remainingCardBar.tick_params(labelsize=7)
        self.remainingCardCanvas.draw()

    def updateOutput(self, cardCount, runningCount):
        self.remainingCardCount -= cardCount
        remainingCardDeckCount = self.remainingCardCount / 52.0
        self.totalRunningCount += runningCount
        self.trueCount = self.totalRunningCount / remainingCardDeckCount
        self.trueCountHistory.append(self.trueCount)
        roundedTrueCount = round(self.trueCount, 3)
        if roundedTrueCount > 0:
            self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: green; }")
        elif roundedTrueCount < 0:
            self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: red; }")
        else:
            self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
        self.lcdNumber.display(roundedTrueCount)
        self.updateCountsPlot()
        self.updateremainingCardHist()

    def deselect(self, event):
        self.textInput.clearFocus()
        self.countingSystem.clearFocus()
        self.deckCount.clearFocus()

    def reset(self):
        self.remainingCardCount = self.deckCount.value() * 52.0
        individualCardCount = self.deckCount.value() * 4
        self.individualCardCount.update(dict.fromkeys(cardValues, individualCardCount))
        self.totalRunningCount = 0
        self.trueCount = 0
        self.trueCountHistory = [0]
        self.textInput.setText("")
        self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
        self.lcdNumber.display(0)
        self.updateCountsPlot()
        self.updateremainingCardHist()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    
    MainWindow.addCountsPlot()
    MainWindow.addremainingCardHist()

    MainWindow.setFixedSize(MainWindow.size())
    MainWindow.show()
    sys.exit(app.exec_())
