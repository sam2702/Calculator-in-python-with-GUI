from tkinter import *
 
window = Tk()
 
window.title("Cal")
 
window.geometry('350x200')
 

 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)
txt1 = Entry(window,width=10)
 
txt1.grid(column=2, row=0)
lbl = Label(window, text="=")
 
lbl.grid(column=0, row=0)

res=0
res1=0
res2=0
res3=0
 
def clicked():
    global res,res1,res2,res3
 
    res =  int(txt.get())+ int(txt1.get())
 
    lbl = Label(window, text=res)
 
    lbl.grid(column=0, row=7)

    res1 =  int(txt.get())* int(txt1.get())
 
    lbl = Label(window, text=res1)
 
    lbl.grid(column=1, row=7)
    res2 =  int(txt.get())- int(txt1.get())
 
    lbl = Label(window, text=res2)
 
    lbl.grid(column=2, row=7)

    res3 =  int(txt.get())/ int(txt1.get())
 
    lbl = Label(window, text=res3)
 
    lbl.grid(column=3, row=7)


btn = Button(window, text="Add", command=clicked)
 
btn.grid(column=0, row=4)

btn = Button(window, text="Mul", command=clicked)
 
btn.grid(column=1, row=4)

btn = Button(window, text="Sub", command=clicked)
 
btn.grid(column=2, row=4)

btn = Button(window, text="Div", command=clicked)
 
btn.grid(column=3, row=4)
 
window.mainloop()

