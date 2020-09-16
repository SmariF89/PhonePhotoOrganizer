#!/usr/bin/env python

import argparse, os
from shutil import copy
from datetime import datetime as date

# This dictionary translates English abbreviations of months to Icelandic full names of months.
# Example: 'Aug' => 'Ágúst'
monthDic = {
    'Jan': 'Janúar',
    'Feb': 'Febrúar',
    'Mar': 'Mars',
    'Apr': 'Apríl',
    'May': 'Maí',
    'Jun': 'Júní',
    'Jul': 'Júlí',
    'Aug': 'Ágúst',
    'Sep': 'September',
    'Oct': 'Október',
    'Nov': 'Nóvember',
    'Dec': 'Desember'
}

# Clear screen while printing output
def clearScreen():

    # Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # Mac & Linux (os.name is 'posix')
    else:
        _ = os.system('clear')

# Takes in a file name and returns true iff file is a media file with an extension
# which is likely to be used by the phone (JPG, GIF, MP4).
def isMediaFile(fileName):
    return fileName.endswith('.jpg') or fileName.endswith('.mp4') or fileName.endswith('.gif')

# Takes in a string denoting seconds since epoch
# Returns a tuple where string has been converted to something like: (17, 'Ágúst', 2019)
def formatTime(secsSinceEpoch):
    formatted = date.utcfromtimestamp(secsSinceEpoch).strftime('%d %b %Y').split(' ')
    return (formatted[0], monthDic[formatted[1]], formatted[2])

# Calculates and returns total size (bytes) of photos in messy folder.
def calculateTotalSize(pathToMess):
    size = 0

    for file in os.scandir(pathToMess):
        currentPath = file.path
        if os.path.isfile(currentPath) and isMediaFile(file.name): 
            size += os.path.getsize(currentPath)

    return size

# Organizes a folder of photos (.jpg) into a more organized folder tree structure.
# It sorts by date. A file, photo.jpg, with a timestamp metadata of 18 Nov 2019 is
# put into the folder 'pathToOrganized/2019/Nóvember/18/photo.jpg.
def organizePhotos(pathToMess, pathToOrganized):
    totalSize = calculateTotalSize(pathToMess)

    if totalSize == 0:
        input('No photos could be found at ' + pathToMess + '.\nPress \'Enter\' to quit.')
        return

    accSize = 0
    currSize = 0
    percentageDone = 0

    photoCount = 0
    
    print('0%')
    for file in os.scandir(pathToMess):
        currentPath = file.path

        if os.path.isfile(currentPath) and isMediaFile(file.name): 
            currentDateModified = formatTime(file.stat().st_mtime)
            
            # Size and percentage calculations
            currSize = os.path.getsize(file.path)
            accSize += currSize
            percentageDone = str(round(((accSize / totalSize) * 100), 2))


            # Create organized path for current photo
            destinationPath = pathToOrganized + os.sep + currentDateModified[2] + os.sep + currentDateModified[1] + os.sep + currentDateModified[0]
            
            # Print feedback for user
            clearScreen()
            print('Copying to ' + destinationPath + ' (' + str(currSize / 1000) + ' kb)\n')
            if percentageDone == '100.0': clearScreen()
            print(percentageDone + '%\n')

            # Create the folder in the organized folder structure and copy photo to destination
            if not os.path.exists(destinationPath):
                os.makedirs(destinationPath)
            copy(currentPath, destinationPath)

            photoCount += 1

    input('Finished organizing ' + str(photoCount) + (' photo. It is ' if photoCount == 1  else ' photos. They are ') + 'located at ' + pathToOrganized + '.\nPress \'Enter\' to quit.')

def main(args):
    if not os.path.exists(args.pathToOrganized):
        os.mkdir(args.pathToOrganized)

    organizePhotos(args.pathToMess, args.pathToOrganized)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
        """This script organizes phone photo folder; creates a new organized one
         with same data""")

    parser.add_argument('pathToMess', metavar='FILE')
    parser.add_argument('pathToOrganized', metavar='FILE')
    args = parser.parse_args()
    main(args)