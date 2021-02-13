from tkinter import *
import subprocess
import re
import sys
import os





from tkinter import messagebox

window = Tk()


window.title("FIEK-2021")
window.configure(background='#D6D4E9')
text = Label(window, text="Wi-Fi Passwords",fg = "black",bg = "#D6D4E9" ,
		 font = "Arial 19   ")
text.place(relx=0.40,rely=0.35)

window.geometry('750x500')



def help():  
    
    
    messagebox.showinfo('Help', 'Click the buttons to see the results!')
  
# create a toplevel menu  
menubar = Menu(window)  
menubar.add_command(label="Help", command=help)  
menubar.add_command(label="Quit", command=window.quit) 
  
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(window) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("700x600") 
  
    # A Label widget to show in toplevel 
    
    #execfile('1.py')
    #exec(open("1.py").read())
    os.system("password.py")
   

    with open("final1.txt", "r") as f:
     Label(newWindow, text=f.read()).pack()

    window.mainloop()
 

def openNewWindow1(): 
      
    
    os.system("kompleksiteti.py")
    
   

    window.mainloop()

btn2 = Button(window,text='Show Complexity', command=openNewWindow1)
btn = Button(window,text='Show Wi-Fi', command=openNewWindow)


btn.grid(column=0,row=0)
btn.place(relx=0.3, rely=0.5)
btn2.grid(column=0,row=0)
btn2.place(relx=0.6, rely=0.5)

     
window.config(menu=menubar)  

window.mainloop()



window.mainloop()