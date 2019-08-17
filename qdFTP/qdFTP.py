#title           :qdFTP.py
#description     :Quick and dirty FTP script.
#author          :Harsimran Grewal (Tr4pDad on github)
#date            :08/11/2018
#version         :3.0
#usage           :python qdFTP.py
#notes           : This is meant to be used as a quick way to connect a TRUSTED FTP site over a TRUSTED network. I am not responsible for any data leakage.
#                  This program is meant to be used through the command line only, any use in functional programs may result in unexpected behaviour/errors
#python_version  :3.7.0
#==============================================================================


import os                                                   #library containing operating system calls
from ftplib import FTP                                      #library for ftp calls

def ftpDownload():
    # FTP login
    ftp = FTP('ADDRESS')
    ftp.login('LOGIN', 'PASSWORD')            #ftp login call
    
    # mode A will be directory traversal, mode B will be file download
    userDone = False
    userInput = input('Enter "A" for directory traversal or "B" for file downloading or "exit" to exit: ',)

    if userInput == 'exit':
        userDone = True
        print('--Connection closed--')
        
    while userDone != True:
        mode = userInput
        
        while mode == 'A' or mode == 'a':
            print('**Enter "B" for file download mode or "exit" to exit**')
            currentDir = ftp.pwd()
            print('Current directory: "' + currentDir + '"')
            dirList = []
            
            ftp.dir(dirList.append )
            listObj = ftp.nlst()
            count = 0
            for item in dirList:
                count += 1
                print(str(count) + ": " + item)
            print('HINT: Enter "back" to go back a directory')
            userInput = input('Select directory to enter: ',)
            
            if userInput == 'B' or userInput == 'b':
                mode = 'B'
                continue
            elif userInput == 'A' or userInput == 'a':
                print("ERROR: You're already in this mode!")
                continue
            
            if userInput == 'exit':
                userDone = True
                print('--Connection closed--') 
                break            
            
            if userInput == 'back':
                ftp.cwd('..')
                continue
            
            ftp.cwd(listObj[int(userInput) - 1])      
            
        while mode == 'B' or mode == 'b':
            print('**Enter "A" for directory traversal mode or "exit" to exit**')
            currentDir = ftp.pwd()
            print('Current directory: "' + currentDir + '"')
            dirList = []
            ftp.dir(dirList.append)
            listObj = ftp.nlst()
            count = 0
            
            for item in dirList:
                count += 1
                print(str(count) + ": " + item)
            print('HINT: Enter "all" to download all files')
            userInput = input('Select file to download: ',)
                
                
            if userInput == 'A' or userInput == 'a':
                mode = 'A'
                continue
            
            elif userInput == 'B' or userInput == 'b':
                print("ERROR: You're already in this mode!")   
                continue
                
            if userInput == 'exit':
                userDone = True
                print('--Connection closed--') 
                break
            
            if userInput == 'all':
                for file in listObj:
                    sourceFileName = file
                    newFile = file
                    downloadedFile = os.path.join(r"C:\\Users\\hgrewal\\Desktop\\TestDownloads", newFile)   #assign path and filename for above file to be downloaded into
                    inputFile = open(downloadedFile, "wb")                                                  #set variable for file to retrieve and access type
                    ftp.retrbinary("RETR " + sourceFileName, inputFile.write)                               #call download function from FTP library
                    inputFile.close()                                                                       #close your open file
                    print(downloadedFile + ' has been sucessfully received')
                continue
                    
            sourceFileName = listObj[int(userInput) - 1]
            newFile = listObj[int(userInput) - 1]
            downloadedFile = os.path.join(r"C:\\Users\\hgrewal\\Desktop\\TestDownloads", newFile)   #assign path and filename for above file to be downloaded into
            inputFile = open(downloadedFile, "wb")                                                  #set variable for file to retrieve and access type
            ftp.retrbinary("RETR " + sourceFileName, inputFile.write)                               #call download function from FTP library
            inputFile.close()                                                                       #close your open file
            print(downloadedFile + ' has been sucessfully received')

