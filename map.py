from tkinter import *
import tkintermapview


root=Tk()
root.geometry("600x600")
root.title("Map")

my_label=Label(text="")
my_label.pack(pady=20)
map_widget=tkintermapview.TkinterMapView(my_label,width=1500,height=850,corner_radius=0)
map_widget.set_zoom(10)
map_widget.set_position(23.1745,88.5606)
map_widget.set_address("Nasra girl's high school,Ranaghat,West Bengal,India")
map_widget.pack()


root.mainloop()