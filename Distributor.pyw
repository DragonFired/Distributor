#!/usr/bin/env python

# from dirstibutor import *
import sys, os
import pickle
import DistributorResources_rc
from subprocess import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_Distributor import *
from ui_AddDestinationDialog import *
from ui_GetPasswordDialog import *
from ui_SettingsDialog import  *

class Distributor( QtGui.QMainWindow ):
    """A game of Dice."""

    def __init__( self, parent=None ):
        """Build a game with two dice."""

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settingsFilename = "distributorPreferences.txt"
        self.settingsFile = ''

        self.sourceFilename = ""
        self.targetFolders = [r"Home Folder", r"Preferences"]
        self.destinationFolderName = ""
        # self.destinationPaths = [r"Preferences", r"Home Folder"]
        self.instructorsDir = r"AC008 Instructors"
        self.majorsDir = r"CSMajors"
        self.othersDir = r"AC008Users"
        self.remoteServer = r"isis.newbury.edu"
        self.localDirectoryMountPoint = "~/"
        self.adminUserPassword = r"admin:remotePassSlot"
        self.allDirectories = [self.instructorsDir, self.majorsDir, self.othersDir]
        self.mountCommand = r"/sbin/mount -t afp"
        self.mountCommands = []
        self.progressValue = 0
        self.selectedDestinationRow = -1

        if os.path.exists(self.settingsFilename):
            with  open( self.settingsFilename, "rb" ) as self.settingsFile:
                self.restorePreferences(self.settingsFile)



        self.destinationItemModel = QStandardItemModel(self.ui.destinationListView)
        for destinationPath in self.targetFolders:
            newDestinationItem = QStandardItem(destinationPath)        # Create an item with a caption
            newDestinationItem.setCheckable(True)                      # Add a checkbox to it
            self.destinationItemModel.appendRow(newDestinationItem)    # Add the item to the model
            newDestinationItem.setCheckState(Qt.Unchecked)
        if self.selectedDestinationRow >= 0:
            self.destinationItemModel.item(self.selectedDestinationRow).setCheckState(Qt.Checked)    # Check the selected item
        self.ui.destinationListView.setModel(self.destinationItemModel)
        self.ui.destinationListView.show()

        self.volumeItemModel = QStandardItemModel(self.ui.volumeListView)
        for volumePath in self.allDirectories:
            newVolumeItem = QStandardItem(volumePath)                  # Create an item with a caption
            newVolumeItem.setIcon(QIcon(":/diskIcon"))                 # Create an item with a caption
            newVolumeItem.setCheckState(Qt.Checked)
            newVolumeItem.setCheckable(True)                           # Add a checkbox to it
            self.volumeItemModel.appendRow(newVolumeItem)              # Add the item to the model
        self.ui.volumeListView.setModel(self.volumeItemModel)
        self.ui.volumeListView.show()

        for directory in self.allDirectories:
            self.mountCommands.append(self.mountCommand + r" afp://" + self.adminUserPassword + "@" + self.remoteServer + "/" + directory.replace(" ", '\ ') + " " + os.path.expanduser(self.localDirectoryMountPoint) + directory.replace(" ", ''))
            self.fullDirectoryPath = self.localDirectoryMountPoint + directory.replace(' ', '')


    def getPreferencesFilename(self):
        return self.settingsFilename

    def restorePreferences(self, fileHandle):
        self.sourceFilename = pickle.load( fileHandle )
        self.targetFolders = pickle.load( fileHandle )
        self.targetFolders.sort()
        self.destinationFolderName = pickle.load( fileHandle )
        self.selectedDestinationRow = pickle.load( fileHandle )
        self.remoteServer = pickle.load( fileHandle )
        self.localDirectoryMountPoint = pickle.load( fileHandle )
        self.adminUserPassword = pickle.load( fileHandle )

    def savePreferences(self, fileHandle):
        pickle.dump( self.sourceFilename, fileHandle )
        pickle.dump( self.targetFolders, fileHandle )
        pickle.dump( self.destinationFolderName, fileHandle )
        pickle.dump( self.selectedDestinationRow, fileHandle )
        pickle.dump( self.remoteServer, fileHandle )
        pickle.dump( self.localDirectoryMountPoint, fileHandle )
        pickle.dump( self.adminUserPassword, fileHandle )


    def updateUI ( self ):
        self.ui.selectedSourceEditBox.setText(self.sourceFilename)
        self.destinationItemModel.removeRows(0, self.destinationItemModel.rowCount())    # Delete all rows
        for path in self.targetFolders:
            newDestinationItem = QStandardItem(path)                                # Create an item with a caption
            newDestinationItem.setCheckState(Qt.Unchecked)
            newDestinationItem.setCheckable(True)                                   # Add a checkbox to it
            self.destinationItemModel.appendRow(newDestinationItem)                 # Add the item to the model
            newDestinationItem.setCheckState(Qt.Unchecked)
        if self.selectedDestinationRow >= 0 and self.selectedDestinationRow < self.destinationItemModel.rowCount():
            self.destinationItemModel.item(self.selectedDestinationRow).setCheckState(Qt.Checked)    # Check the selected item
        self.ui.destinationListView.setModel(self.destinationItemModel)
        self.ui.progressBar.setValue(self.progressValue)

    def distribute(self, sourceFilename, targetFolders, destinationFolderName):
        getPasswordDialog = GetPasswordDialog()
        getPasswordDialog.exec_()
        self.remotePassword = getPasswordDialog.getText()
        getPasswordDialog.close()
        if destinationFolderName == "":
            return
        for directory in self.allDirectories:
            fullDirectoryPath = self.localDirectoryMountPoint + directory.replace(' ', '')
            child = Popen([r'/bin/mkdir ' + fullDirectoryPath], shell = True)
            stdout, stderr = child.communicate()

        for mountCommand in self.mountCommands:
            print("Running mount command: ", mountCommand)
            child = Popen([mountCommand.replace("remotePassSlot", self.remotePassword)], shell = True)
            stdout, stderr = child.communicate()

        for directory in self.allDirectories:
            fullLocalMountPoint = os.path.expanduser(self.localDirectoryMountPoint)
            fullDirectoryPath = os.path.expanduser(self.localDirectoryMountPoint) + directory.replace(" ", '')
            try:
                if os.path.exists(fullDirectoryPath):
                    print("\nListing for: " + fullDirectoryPath)
                    studentsList = os.listdir(fullDirectoryPath)
                    if '.TemporaryItems' in studentsList:
                        studentsList.remove('.TemporaryItems')
                        print(studentsList)

                    for filename in studentsList:
                        if filename[0] == '.' or 'temp' in filename or 'test' in filename:
                            studentsList.remove(filename)
                            print("Removing file: %s" % filename)
                        else:
                            print(filename)
            except Exception as e:
                print("Directory listing failed.\n\t", directory)
                continue

        child = Popen(['touch /Users/arana/AC008Instructors/aranafireheart/Desktop/testfile.txt'], shell = True)
        stdout, stderr = child.communicate()

        for directory in self.allDirectories:
            fullDirectoryPath = os.path.expanduser(self.localDirectoryMountPoint) + directory.replace(" ", '')
            if os.path.exists(fullDirectoryPath):
                command = '/sbin/umount ' + fullDirectoryPath
                print("Cleaning up: ", command)
                Popen([command], shell = True)
                stdout, stderr = child.communicate()
                if os.path.exists(fullDirectoryPath):
                    command = '/bin/rmdir ' + fullDirectoryPath
                    Popen([command], shell = True)
                    stdout, stderr = child.communicate()
                    print("\t\t\t ", command)


    @QtCore.pyqtSignature("")
    def on_selectSourceButton_clicked ( self ):
        self.sourceFilename = QFileDialog.getOpenFileName(self, 'Open File', '.')
        with  open( self.settingsFilename, "wb" ) as self.settingsFile:
            self.savePreferences( self.settingsFile)
        self.updateUI()

    @QtCore.pyqtSignature("")
    def on_distributeButton_clicked ( self ):
        self.distribute(self.sourceFilename, self.targetFolders, self.destinationFolderName)
        self.updateUI()

    @QtCore.pyqtSignature("")
    def on_addDestinationButton_clicked ( self ):
        addDestinationDialog = AddDestinationDialog()
        addDestinationDialog.exec_()
        newDestination = addDestinationDialog.getText()
        if newDestination != "":
            self.targetFolders.append(newDestination)
            self.targetFolders.sort()
        self.updateUI()

    @QtCore.pyqtSignature("")
    def on_deleteDestinationButton_clicked ( self ):
        del self.targetFolders[self.selectedDestinationRow]
        if self.destinationItemModel.item(self.selectedDestinationRow).checkState():    # Is the item is checked?
            self.selectedDestinationRow = -1
        if self.selectedDestinationRow == self.destinationItemModel.rowCount() - 1:     # If deleting the last row
            self.selectedDestinationRow = -1                                            # then no row is selected.
        self.updateUI()

    @QtCore.pyqtSignature("")
    def on_settingsButton_clicked ( self ):
        settingsDialog = SettingsDialog()
        settingsDialog.exec_()
        settingsList = settingsDialog.getText()
        self.updateUI()


    @QtCore.pyqtSignature("")
    def on_selectedSourceEditingFinished ( self ):
        self.sourceFilename = self.ui.selectedSourceEditBox.text()
        with  open( self.settingsFilename, "wb" ) as self.settingsFile:
            self.savePreferences( self.settingsFile)
        self.updateUI()

    @QtCore.pyqtSignature("")
    def on_destinationFolderItemChanged(self, item):
        self.selectedDestinationRow = item.row()
        print("Destination Folder Item Changed", self.selectedDestinationRow)
        for itemNumber in range(0, self.destinationItemModel.rowCount()):           # Clear all check marks
            self.destinationItemModel.item(itemNumber).setCheckState(Qt.Unchecked)

        self.destinationItemModel.item(item.row()).setCheckState(Qt.Checked)        # Check the selected item
        self.destinationFolderName = "%s" % (self.destinationItemModel.item(item.row()).text())
        print(self.destinationFolderName)

    def closeEvent(self, event):
        print "closing PyQtTest"
        with  open( DistributorApp.getPreferencesFilename(), "wb" ) as settingsFile:
            DistributorApp.savePreferences(settingsFile)


class AddDestinationDialog( QtGui.QDialog ):

    def __init__( self, parent=None ):
        QtGui.QDialog.__init__(self, parent)
        self.addDestinationUi = Ui_addDestinationDialog()
        self.addDestinationUi.setupUi(self)

    @QtCore.pyqtSignature("")
    def getText ( self ):
        self.show()
        return self.addDestinationUi.newDestinationLineEdit.text()

class GetPasswordDialog( QtGui.QDialog ):

    def __init__( self, parent=None ):
        QtGui.QDialog.__init__(self, parent)
        self.getPasswordUi = Ui_getPasswordDialog()
        self.getPasswordUi.setupUi(self)

    @QtCore.pyqtSignature("")
    def getText ( self ):
        self.show()
        return self.getPasswordUi.passwordLineEdit.text()

class SettingsDialog( QtGui.QDialog ):

    def __init__( self, parent=None ):
        QtGui.QDialog.__init__(self, parent)
        self.settingsUi = Ui_settingsDialog()
        self.settingsUi.setupUi(self)

    @QtCore.pyqtSignature("")
    def getText ( self ):
        self.settingsUi.remoteServerEdit.setText(DistributorApp.remoteServer)
        self.settingsUi.localMountPointEdit.setText(DistributorApp.localDirectoryMountPoint)
        self.settingsUi.remoteAdminUserNameEdit.setText(DistributorApp.adminUserPassword)

        self.show()
        return [self.settingsUi.remoteServerEdit.text(), self.settingsUi.remoteServerEdit.text(), self.settingsUi.remoteAdminUserNameEdit.text()]


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    DistributorApp = Distributor()
    DistributorApp.updateUI()
    DistributorApp.show()
    returned = app.exec_()
    # Your code that must run when the application closes goes here
    # with  open( DistributorApp.getPreferencesFilename(), "wb" ) as settingsFile:
    #     DistributorApp.savePreferences(settingsFile)
    sys.exit(returned)
