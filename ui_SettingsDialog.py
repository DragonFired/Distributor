# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/arana/PycharmProjects/Distributor/SettingsDialog.ui'
#
# Created: Tue Mar  4 17:04:38 2014
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

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName(_fromUtf8("settingsDialog"))
        settingsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        settingsDialog.resize(679, 357)
        font = QtGui.QFont()
        font.setPointSize(13)
        settingsDialog.setFont(font)
        settingsDialog.setStyleSheet(_fromUtf8("QDialog{ background-color: rgb(167, 167, 167); }"))
        self.gridLayout = QtGui.QGridLayout(settingsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(settingsDialog)
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(207, 207, 207);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.remoteServerEdit = QtGui.QLineEdit(settingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteServerEdit.sizePolicy().hasHeightForWidth())
        self.remoteServerEdit.setSizePolicy(sizePolicy)
        self.remoteServerEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.remoteServerEdit.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.remoteServerEdit.setFont(font)
        self.remoteServerEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.remoteServerEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.remoteServerEdit.setObjectName(_fromUtf8("remoteServerEdit"))
        self.verticalLayout.addWidget(self.remoteServerEdit)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(settingsDialog)
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(207, 207, 207);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.localMountPointEdit = QtGui.QLineEdit(settingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localMountPointEdit.sizePolicy().hasHeightForWidth())
        self.localMountPointEdit.setSizePolicy(sizePolicy)
        self.localMountPointEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.localMountPointEdit.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.localMountPointEdit.setFont(font)
        self.localMountPointEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.localMountPointEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.localMountPointEdit.setObjectName(_fromUtf8("localMountPointEdit"))
        self.verticalLayout.addWidget(self.localMountPointEdit)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(settingsDialog)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(207, 207, 207);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.remoteAdminUserNameEdit = QtGui.QLineEdit(settingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteAdminUserNameEdit.sizePolicy().hasHeightForWidth())
        self.remoteAdminUserNameEdit.setSizePolicy(sizePolicy)
        self.remoteAdminUserNameEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.remoteAdminUserNameEdit.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.remoteAdminUserNameEdit.setFont(font)
        self.remoteAdminUserNameEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.remoteAdminUserNameEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.remoteAdminUserNameEdit.setObjectName(_fromUtf8("remoteAdminUserNameEdit"))
        self.verticalLayout.addWidget(self.remoteAdminUserNameEdit)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem7 = QtGui.QSpacerItem(17, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.buttonBox = QtGui.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(settingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settingsDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Password Entry", None))
        self.label_4.setText(_translate("settingsDialog", "Remote Server Name:", None))
        self.label_3.setText(_translate("settingsDialog", "Local Mount Point:", None))
        self.label_2.setText(_translate("settingsDialog", "Remote Admin User Name:", None))

