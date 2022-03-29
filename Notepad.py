from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled-Notepad")
    file= None
    TextArea.delete(1.0, END)

def Openfile():
    global file
    file= askopenfilename(defaultextension="text", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

    if file == "" :
        file= None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def Savefile():
    global file
    if file == None:
        file= asksaveasfilename(initialfile=" Untitled.txt",defaultextension="text", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
           file= None
        else:
         f = open(file,"w")
         f.write(TextArea.get(1.0, END))
         f.close()
         root.title(os.path.basename(file)+ " - Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitapp():
    root.destroy()
def cut():
    TextArea.event_generate("<<Cut>>")
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")
def about():
    showinfo("Notepad", "Notepad by Jaya Mishra")

if __name__ == '__main__':
    root=Tk()
    root.title("Untitled- Notepad")
    root.wm_iconbitmap("wheel.ico")
    root.geometry("644x788")

    TextArea= Text(root, font="lucida 13")
    file= None
    TextArea.pack(fill=BOTH, expand=True)
    MenuBar = Menu(root)
    Filemenu = Menu(MenuBar, tearoff=0)

    Filemenu.add_command(label="New", command=newfile)
    Filemenu.add_command(label="Open", command=Openfile)
    Filemenu.add_command(label="Save", command=Savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=quitapp)
    MenuBar.add_cascade(label="File", menu=Filemenu)

    root.config(menu=MenuBar)


    Editmenu= Menu(MenuBar, tearoff=0)
    Editmenu.add_command(label="Cut", command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu= Editmenu)

    Helpmenu = Menu(MenuBar, tearoff=0)
    Helpmenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=Helpmenu)
    root.config(menu=MenuBar)

    scrollbar= Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)






    root.mainloop()