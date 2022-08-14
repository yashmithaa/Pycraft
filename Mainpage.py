import sys, os
from tkinter import *
from PIL import ImageTk,Image
canvas=Tk()
canvas.title('Pycraft - Menu')
canvas.geometry('1080x1920')
canvas.config(background='#DAF7C1')
canvas.iconbitmap('assets/icon.ico')
#def 
def AddQuest():
        pass
def helloAdmin():
    Ad=Tk()
    Ad.title('administrator')
    Ad.geometry('120x150')
    Ad.config(background='grey')
    B = Button(Ad, text='add',width=12)

        

def game():
        os.system('PycraftGame.py')
        
def ExitGame():
        canvas.destroy()


label = Label(canvas,text = 'PYCRAFT', relief=RAISED,bg="#128C74", width=40, height=2,
              fg='white',borderwidth=8, font=('Bauhaus 93',65))
label.pack()
myImage = ImageTk.PhotoImage(Image.open("assets/advert.png"))
myLabel1 = Label(image=myImage)
myLabel1.place(relx=.43, rely=0.4)

B1=Button(canvas,text="Admin",width=12,height=2,bg='#2D7164',fg='white',
          font=("Arial Black",10),command=helloAdmin)
B1.place(relx=0.2,rely=0.8)


B2=Button(canvas,text="Play",width=12,height=2,bg='#2D7164',fg='white',
          font=("Arial Black",10),command= game )
B2.place(relx=0.44,rely=0.8)



B3=Button(canvas,text="Quit",width=12,height=2,bg='#2D7164',fg='white',
          font=("Arial Black",10),command=ExitGame)
B3.place(relx=0.68,rely=0.8)

canvas.mainloop()
