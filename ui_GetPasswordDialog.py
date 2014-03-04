# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/arana/PycharmProjects/Distributor/GetPasswordDialog.ui'
#
# Created: Tue Mar  4 17:05:26 2014
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

class Ui_getPasswordDialog(object):
    def setupUi(self, getPasswordDialog):
        getPasswordDialog.setObjectName(_fromUtf8("getPasswordDialog"))
        getPasswordDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        getPasswordDialog.resize(522, 151)
        font = QtGui.QFont()
        font.setPointSize(13)
        getPasswordDialog.setFont(font)
        getPasswordDialog.setStyleSheet(_fromUtf8("QDialog{ background-color: rgb(106, 129, 255); }"))
        self.gridLayout = QtGui.QGridLayout(getPasswordDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(getPasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(207, 207, 207);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.passwordLineEdit = QtGui.QLineEdit(getPasswordDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.verticalLayout.addWidget(self.passwordLineEdit)
        spacerItem = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(getPasswordDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(getPasswordDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), getPasswordDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), getPasswordDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), getPasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(getPasswordDialog)

    def retranslateUi(self, getPasswordDialog):
        getPasswordDialog.setWindowTitle(_translate("getPasswordDialog", "Password Entry", None))
        self.label.setText(_translate("getPasswordDialog", "Enter the remote system password", None))

