from tkinter import *

root =Tk()
root.title('Windows')
root.geometry('1024x620')


btn = Button(text="Hello")
btn.place(relx=.2, rely=.7, anchor="c", height=20, width=130, bordermode=OUTSIDE)

root.mainloop()
