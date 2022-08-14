import sys, os
from tkinter import *
from turtle import down
from PIL import ImageTk,Image
canvas=Tk()
canvas.title('Pycraft - Menu')
canvas.geometry('1080x1078')
canvas.config(background='#6B3DC2')
canvas.iconbitmap('assets/icon.ico')
#def 
def AddQuest():
        pass

        

def game():
        os.system('PycraftGame.py')
        
def ExitGame():
        canvas.destroy()


label = Label(canvas,text = 'PYCRAFT', relief=RAISED,bg="#94C23D", width=40, height=2,
              fg='white',borderwidth=8, font=('Bauhaus 93',65))
label.pack()
'''myImage = ImageTk.PhotoImage(Image.open("assets/blocky.png"))
myLabel1 = Label(image=myImage)
myLabel1.place(relx=.36, rely=0.35)'''
bimage = PhotoImage(file="assets/blocky.png") 
img=Canvas(canvas,height=500,width=300,bg='#6B3DC2',highlightbackground='#6B3DC2')
img.create_image(0,50, image=bimage, anchor =NW)
img.pack()



B2=Button(canvas,text="Play",width=54,height=2,bg='#94C23D',fg='white',
          font=("Arial Black",10),command= game )
B2.place(relx=0.04,rely=0.8)



B3=Button(canvas,text="Quit",width=54,height=2,bg='#94C23D',fg='white',
          font=("Arial Black",10),command=ExitGame)
B3.place(relx=0.49,rely=0.8)

canvas.mainloop()
