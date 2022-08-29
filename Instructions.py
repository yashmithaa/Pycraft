from tkinter import *
from tkinter import Canvas
from PIL import ImageTk, Image
page = Tk()
page.configure(bg='white') 
page.title('Instructions') 
page.geometry('500x700')
#page.iconbitmap('assets/icon.ico') <bcoz i have the file>


label = Label(page,text = 'How to Play', relief=RAISED, width=25, height=2,
              fg='black',font=('Bauhaus 93',30)) #for fonts just open ur word n search for good fonts,copy its name and paste
label.pack()
label = Label(page,text = 'Q - Quit',fg='black',font=('Bauhaus 93',30)) #for fonts just open ur word n search for good fonts,copy its name and paste
label.pack()

#for bg image #I'll attach the pic after this code
bimage = PhotoImage(file="assets/inst_forground.png") 
canvas=Canvas(page,height=700,width=500,bg='#282828')
canvas.create_image(0,0, image=bimage, anchor =NW)
canvas.pack()


#button to stop running
okbtn = Button(page, text='Okay Boss', bg='white', fg='black',width=10,command=page.destroy)
okbtn.place(relx=0.45,rely=0.9)
page.mainloop()