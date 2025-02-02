# 2/2/2025 Python 3
# Project under development
# Formula calculator prototype for the project

# NOTE: THIS IS NOT THE FINAL PRODUCT (project)!
# This is just a prototype for calculating some calculations that will be used in the project

from tkinter import *

root = Tk()
root.geometry("800x200")
root.title("Formula")
root.resizable(False,False)
root.wm_attributes("-toolwindow",True)
root.wm_attributes("-topmost", True)

class VarScale:
    def __init__(self, master,x,y,orient,length=100,from_=0.0,to=100.0):
        super().__init__()

        self.x, self.y = x,y
        self.var = DoubleVar()
        self.orient = orient

        if orient == 0: self.orient = VERTICAL
        if orient == 1: self.orient = HORIZONTAL

        self.scale = Scale(master, variable=self.var, from_=from_, to=to, resolution=0.1, orient=self.orient, length=length)

    def update(self):
        self.scale.place(x=self.x, y=self.y)

labelA = Label(root, text="A").place(x=10,y=25)
labelB = Label(root, text="B").place(x=10,y=75)
labelC = Label(root, text="C").place(x=10,y=125)

x = VarScale(root, 140,10,0,140,100.0,0.0)
a = VarScale(root,40,10,1)
b = VarScale(root,40,60,1)
c = VarScale(root, 40,110,1)


for scale in [x,a,b,c]:
    scale.update()

labelMath = Label(root, font=(None, 20), text=f"ƒ({x.var.get()}) = ({a.var.get()}+{b.var.get()}+{c.var.get()}) mod {x.var.get()}\n\r= {str(sum((a.var.get(),b.var.get(),c.var.get())) % x.var.get() if x.var.get() > 0.0 else 0.0)} %", bd=10, bg="white")
labelMath.place(x=240, y=10)

def update_math():
    while True:
        labelMath.config(text=f"ƒ({x.var.get()}) = ({a.var.get()}+{b.var.get()}+{c.var.get()}) mod {x.var.get()}\n\r= {str(sum((a.var.get(),b.var.get(),c.var.get())) % x.var.get() if x.var.get() > 0.0 else 0.0):.6} %")
        root.update()


root.after(1,update_math)
root.update()
root.mainloop()
