from tkinter import *

admst=Tk()
admst.title('Pycraft - Admin')
admst.geometry('1080x1920')
admst.config(background='white')
admst.iconbitmap('assets/icon.ico')

label = Label(admst,text = 'Admin', relief=RAISED, width=25, height=2,
              fg='black',font=('Bauhaus 93',30))
label.pack()
admst.mainloop()