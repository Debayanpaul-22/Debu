from tkinter import *
from PIL import ImageTk,Image
import pyqrcode
from tkinter.filedialog import asksaveasfilename
root=Tk()
root.geometry("600x650")
root.configure(background="light gray")
root.title("QR code generetor")
root.minsize(600,650)
root.maxsize(600,650)
root.iconbitmap("QR Code.png")
#Functions'
def convert(event):
        input_path=asksaveasfilename(title="Save Code",initialfile="QR Code",defaultextension=".png",filetypes=[("All file","*.*"),("png file",".png")])
        if input_path:
            if input_path.endswith(".png"):
                get_code=pyqrcode.create(input_link.get())
                get_code.png(input_path,scale=5)
            else:
                input_path=f"{input_path}.png"
                get_code = pyqrcode.create(input_link.get())
                get_code.png(input_path, scale=5)
                #put image in screen
            global get_image
            get_image=ImageTk.PhotoImage(Image.open(input_path))
            #set it in label
            my_label.config(image=get_image)
            input_link.delete(0,END)
            input_link.insert(0,"Finished")
def clear(event):
    input_link.delete(0,END)
    my_label.config(image='')



#Body
Label(root,text="QR Code genaretor",font="Algerian 30 underline",bg="light gray").pack()
Label(root,text="Type the link Hear",font="calibri 20",bg="light gray").pack()
input_link=Entry(root,font="Calibri 20",width=30)
input_link.pack(pady=20)
button=Button(root,text="Convert",font="Calibri 20",width=20,bg="blue",fg="white")
button.pack(pady=10)
button.bind('<Button-1>',convert)
clear_button=Button(root,text="Clear all",font="calibri 16",bg="red",fg="white")
clear_button.pack()
clear_button.bind('<Button-1>',clear)
my_label=Label(root,text='',bg="light gray")
my_label.pack(pady=10)

root.mainloop()