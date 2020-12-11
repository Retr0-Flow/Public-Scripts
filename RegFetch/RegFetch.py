#title           :RegFetch.py
#description     :A tool for fetching the data a registry key has.
#author          :Harsimran Grewal (Retr0-Flow on github)
#date            :11/12/2020
#version         :1.0
#usage           :python RegFetch.py -i <Registry Keys File>
#notes           :Please feel free to share this script and suggestion any addition or changes that could be made!
#python_version  :3.7.2
#==========================================================================================================================================================

from winreg import HKEY_CLASSES_ROOT
from winreg import HKEY_CURRENT_USER
from winreg import HKEY_LOCAL_MACHINE
from winreg import HKEY_USERS
from winreg import HKEY_CURRENT_CONFIG
from winreg import ConnectRegistry
from winreg import OpenKey
from winreg import QueryInfoKey
from winreg import EnumValue
from argparse import ArgumentParser
from sys import argv

def regFetch(regList):
    try:
        with open(regList, "r") as keyFile:
            for line in keyFile:
                #clean and assign variables
                line = line.rstrip('\n')
                checkRegArr = line.split(',')
                aReg = None
                aRegLoc = checkRegArr[0]
                aKey = checkRegArr[1]
                try:
                    aRegKeyValue = checkRegArr[2]
                except IndexError:
                    aRegKeyValue = 'ALL'
                hKeyDict = {
                    "HKEY_CLASSES_ROOT" : HKEY_CLASSES_ROOT,
                    "HKEY_CURRENT_USER" : HKEY_CURRENT_USER,
                    "HKEY_LOCAL_MACHINE" : HKEY_LOCAL_MACHINE,
                    "HKEY_USERS" : HKEY_USERS,
                    "HKEY_CURRENT_CONFIG" : HKEY_CURRENT_CONFIG
                    }
                
                #connect and open registry address/key
                aReg = ConnectRegistry(None, hKeyDict[aRegLoc.upper()])
                opKey = OpenKey(aReg, aKey)

                if aRegKeyValue != 'ALL':            
                    try:    #Will output value:data pair for specific registry key value
                        if (QueryInfoKey(opKey)[1] == 0):   #Check for empty registry key
                            print("NO VALUES FOUND IN REGISTRY: %s\\%s\n" %(aRegLoc, aKey))
                        else:
                            for i in range(1024):
                                if EnumValue(opKey,i)[0] == aRegKeyValue:   #Check to ensure current registry key is the same as user specified key
                                    aKeyValData = EnumValue(opKey,i)[1]
                                    if (aKeyValData != ""):
                                        print("The registry value of %s\\%s -> %s, is:" %(aRegLoc, aKey, aRegKeyValue))
                                        print("--> %s  :  %s"  %(aRegKeyValue, aKeyValData))
                                    else:
                                        print("The registry value of %s\\%s -> %s, is:" %(aRegLoc, aKey, aRegKeyValue))
                                        print("--> %s  :  No Data Assigned"  %(aRegKeyValue))
                    except WindowsError as WinErr:
                        if WinErr.args[3] == 259: #If the WinErr code is 259 aka No more data available, continue loop
                            print("")
                            continue
                        else:
                            print(WinErr)
                else:
                    try:    #Will output all values:data pairs in a registry key
                        if (QueryInfoKey(opKey)[1] == 0):
                            print("NO VALUES FOUND IN REGISTRY: %s\\%s\n" %(aRegLoc, aKey))
                        else:
                            print("Found these in registry %s\\%s:" %(aRegLoc, aKey))
                            for i in range(1024):
                                bRegKeyValue = EnumValue(opKey,i)[0]
                                bKeyValData = EnumValue(opKey,i)[1]
                                print("--> %s  :  %s"  %(bRegKeyValue, bKeyValData))
                    except WindowsError as WinErr:
                        if WinErr.args[3] == 259: #If the WinErr code is 259 aka No more data available, continue loop
                            print("")
                            continue
                        else:
                            print(WinErr)
    except IndexError as indexErr:
        raise SystemExit("Usage: %s -r <registry_key_file>" %(argv[0]))
    except FileNotFoundError as noFile:
        raise SystemExit("File does not exist or cannot be found: %s" %(regList))
    except IsADirectoryError as dirError:
        raise SystemExit("Directory specified when looking for file: %s" %(regList))
    except PermissionError as permError:
        raise SystemExit("Incorrect permissions on file %s or %s" %(regList, argv[0]))

#setup arguments for command line use and run
parser = ArgumentParser(description='RegFetch will take a list of registry locations and output their specified values to the console.')
parser.add_argument("inputFile", metavar="<Registry list file>", type=str, help="Specify the file containing your list of registry keys to check.")
args = parser.parse_args()
registryList = args.inputFile
regFetch(regList=registryList)