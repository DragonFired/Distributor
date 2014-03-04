# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/arana/PycharmProjects/Distributor/AddDestinationDialog.ui'
#
# Created: Tue Mar  4 14:38:11 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_addDestinationDialog(object):
    def setupUi(self, addDestinationDialog):
        addDestinationDialog.setObjectName(_fromUtf8("addDestinationDialog"))
        addDestinationDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        addDestinationDialog.resize(414, 135)
        font = QtGui.QFont()
        font.setPointSize(13)
        addDestinationDialog.setFont(font)
        addDestinationDialog.setStyleSheet(_fromUtf8("QDialog{ background-color: rgb(106, 129, 255); }"))
        self.gridLayout = QtGui.QGridLayout(addDestinationDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(addDestinationDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(207, 207, 207);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.newDestinationLineEdit = QtGui.QLineEdit(addDestinationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newDestinationLineEdit.sizePolicy().hasHeightForWidth())
        self.newDestinationLineEdit.setSizePolicy(sizePolicy)
        self.newDestinationLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.newDestinationLineEdit.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newDestinationLineEdit.setFont(font)
        self.newDestinationLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.newDestinationLineEdit.setObjectName(_fromUtf8("newDestinationLineEdit"))
        self.verticalLayout.addWidget(self.newDestinationLineEdit)
        spacerItem = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(addDestinationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(addDestinationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), addDestinationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), addDestinationDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), addDestinationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addDestinationDialog)

    def retranslateUi(self, addDestinationDialog):
        addDestinationDialog.setWindowTitle(_translate("addDestinationDialog", "Add Destination", None))
        self.label.setText(_translate("addDestinationDialog", "Enter a destination folder name:", None))

