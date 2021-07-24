import winreg as reg
import os
import shutil
import winshell
import win32com.client

deleter_name = "Doka2_deleter" 

path = ['C:/', 'D:/', 'E:/', 'F:/', 'G:/', 'H:/', 'I:/', 'J:/', 'K:/']
to_find = "dota 2 beta"

startup = winshell.startup()
try:
    os.remove(startup + "\\" + deleter_name + ".lnk")
    print("Removed from start")
except Exception as e:
    print("Already not in start")

" Deletes Doka2_deleter.exe"
def deleteDeleter():
    for entry in path:
        if not os.path.exists(str(entry) + "\\"+ deleter_name + ".exe"):
            pass
        else:
            to_del = os.path.join(os.path.abspath(entry), deleter_name + ".exe")
            os.remove(to_del)
            print("Deleted from path " + to_del)

deleteDeleter()

input("All ok, press Enter")