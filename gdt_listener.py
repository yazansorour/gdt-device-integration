from classes.GDTNetworkConnection import GDTNetworkConnection
from classes.GDTMessage import GDTMessage

import time
import sys
import requests

localFolder = sys.argv[1] # ex : '/home/frappe/frappe-bench/sites/gdt/out'
remoteFolder = sys.argv[2] # ex : '/home/frappe/share/TestMod/gdt/out' its bind it with remote folder

print("GDT Listening Now !")

while True:
    newFiles = GDTNetworkConnection.getRemoteFiles( localFolder, remoteFolder )
    print(f'Copied Files {newFiles}')
    fileGDTPath = None
    if len(newFiles) > 0 : 
        for file in newFiles:
            if file.endswith('.gdt') == True:
                fileGDTPath = file
                break
        if fileGDTPath:
            try:
                testResult = ''
                with open(fileGDTPath  , 'r') as file:
                    testResult = file.read()

                response = requests.post('http://127.0.0.1/api/method/endo.api.uploadTestResult', json={'testResult':testResult ,'files':newFiles},timeout=10)
                if response.status_code == 200:
                    print("Result has been sent successfly")
                    print("Response JSON:", response.json()) 
                else:
                    print("Result sent error")
            except:
                print("There is an issue on gdt file")


    time.sleep(10)


