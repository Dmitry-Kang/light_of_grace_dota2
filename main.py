import os
from tkinter import *
 
root = Tk()
root.title("The light of grace v2.28:1337")
root.geometry("400x300+300+250")

# path = 'C:/'
path = ['C:/', 'D:/', 'E:/', 'F:/', 'G:/', 'H:/', 'I:/', 'J:/', 'K:/']
# to_find = "dota 2 beta"
to_find = "Counter-Strike Global Offensive"

def lets_go():
    res = "Ненашлось :("
    for where_find in path:
        print("founding 1")
        found = False
        for dirs, folder, files in os.walk(where_find):
            if found == True:
                break
            for fol in folder:
                if (fol == to_find):
                    found = True
                    print("found", fol, "here", dirs, "*pow*pow*pow*")
                    res = res + "found " + fol + " here " + dirs + "\n"
                    break
    poetry.set(res)
    return

# lets_go()

btn = Button(text="~Жмякни~",          # текст кнопки 
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             command=lets_go
             )
btn.pack()

poetry = StringVar()
poetry.set("Ожидание ~жмяка~")
label2 = Label(textvariable=poetry, justify=LEFT)
label2.place(relx=.2, rely=.3)
 
root.mainloop()
        