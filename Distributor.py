#!/bin/env python3
__author__ = 'arana'
import os
from sudo import sudo
import pexpect
from subprocess import *
from path import path
from time import sleep
from getpass import getpass

# localPassword = getpass("Enter the local admin password: ")
# remotePassword = getpass("Enter the remote admin password: ")
passFileHandle = open("passwords.txt")
localPassword = passFileHandle.readline().rstrip('\r\n')
remotePassword = passFileHandle.readline().rstrip('\r\n')

destinationPaths = [r"Preferences", r"Home Folder"]
instructorsDir = r"AC008 Instructors"
majorsDir = r"CSMajors"
othersDir = r"AC008Users"
remoteServer = r"isis.newbury.edu"
localDirectoryMountPoint = "~/"
adminUserPassword = r"admin:remotePassSlot"
allDirectories = [instructorsDir, majorsDir, othersDir]
mountCommand = r"/sbin/mount -t afp"
mountCommands = []

for directory in allDirectories:
    mountCommands.append(mountCommand + r" afp://" + adminUserPassword + "@" + remoteServer + "/" + directory.replace(" ", '\ ') + " " + os.path.expanduser(localDirectoryMountPoint) + directory.replace(" ", ''))

    fullDirectoryPath = localDirectoryMountPoint + directory.replace(' ', '')

    child = Popen([r'/bin/mkdir ' + fullDirectoryPath], shell = True)
    stdout, stderr = child.communicate()

    # if stderr:
    #     print("Make directory command failed for: ", directory)

for mountCommand in mountCommands:
    print("Running mount command: ", mountCommand)
    child = Popen([mountCommand.replace("remotePassSlot", remotePassword)], shell = True)
    stdout, stderr = child.communicate()

    # if stderr != 0:
    #     print("Mount command failed.\n\t", mountCommand)
    #     continue

for directory in allDirectories:
    fullLocalMountPoint = os.path.expanduser(localDirectoryMountPoint)
    fullDirectoryPath = os.path.expanduser(localDirectoryMountPoint) + directory.replace(" ", '')
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

for directory in allDirectories:
    fullDirectoryPath = os.path.expanduser(localDirectoryMountPoint) + directory.replace(" ", '')
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

