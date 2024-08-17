from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
if __name__ == '__main__':
    root=Tk()
    root.geometry("600x500")
    root.title("Untitle-Notepad")
    #Functions
    def NewFile():
        global file
        root.title("Untitle-Notepad")
        text.delete(0,END)
    def OpenFile():
        global file
        file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
            root.title(os.path.basename(file)+"- Notepad")
            text.delete(1.0,END)
            f=open(file,"r")
            text.insert(1.0,f.read())
            f.close()
    def SaveFile():
        global file
        if file==None:
            file=asksaveasfilename(initialfile="Untitle.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
            if file=="":
                file=None
            else:
                f = open(file,"w")
                f.write(text.get(1.0, END))
                f.close()

                root.title(os.path.basename(file)+"- Notepad")
                print("File save")
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

    def QuitFile():
        root.destroy()
    def UndoFile():
        pass
    def RedoFile():
        pass
    def CutFile():
        text.event_generate("<<Cut>>")
    def CopyFile():
        text.event_generate("<<Copy>>")
    def PasteFile():
        text.event_generate("<<Paste>>")
    def HelpFile():
        tmsg.showinfo("Notepad","This software made by Debayan paul")



    #menu bar
    Menubar=Menu(root)

    #File Menu
    Filemenu=Menu(Menubar,tearoff=0)
    Filemenu.add_command(label="New",command=NewFile)
    Filemenu.add_command(label="Open",command=OpenFile)
    Filemenu.add_command(label="Save",command=SaveFile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit", command=QuitFile)
    Menubar.add_cascade(label="File", menu=Filemenu)
    #Edit menu
    Editmenu=Menu(Menubar,tearoff=0)
    Editmenu.add_command(label="Undo",command=UndoFile)
    Editmenu.add_command(label="Redo", command=RedoFile)
    Editmenu.add_separator()
    Editmenu.add_command(label="Cut", command=CutFile)
    Editmenu.add_command(label="Copy", command=CopyFile)
    Editmenu.add_command(label="Paste", command=PasteFile)
    Menubar.add_cascade(label="Edit", menu=Editmenu)
    #Help menu
    Helpmenu=Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label="About",command=HelpFile)
    Menubar.add_cascade(label="Help",menu=Helpmenu)

    root.configure(menu=Menubar)

    #Editor
    Scr=Scrollbar(root)
    Scr.pack(side=RIGHT,fill=Y)
    text=Text(root,font="calibri 13",yscrollcommand=Scr.set)
    text.pack(padx=5,fill=BOTH,expand=True)
    file=None

    Scr.config(command=text.yview())
    root.mainloop()