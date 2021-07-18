from tkinter import *
from random import randint

#creating window

window = Tk()
window.title("Number guessing game")
window.geometry("600x600")


#create whole bg window
label_number=Label(window , text="Pick number between\n1 - 10" , font=("comic sans Ms",28) )
label_number.pack(pady=20)

#submit button function
def guesser():
    if guess_box.get().isdigit():
        #reset our label
        label_number.config(text="Pick number between\n1 - 10")
         #find how war away we are
        dif=abs(num- int(guess_box.get()))
        #check if is correct
        if int(guess_box.get())== num:
            bc = "SystemButtonFace"
            label_number.config(text="Hey! You're genius")
        elif dif==5:
            bc ="white"
        elif dif<5:
            bc = f"#ff{dif}{dif}{dif}{dif}"
        else:
            bc=f"#{dif}{dif}{dif}{dif}ff"
        #change bg of app
        window.config(bg=bc)
        #change bg of label
        label_number.config(bg=bc)

        




    else:
        guess_box.delete(0,END)
        
        label_number.config(text="Hey! this not a number")
       

    
        
#newgame button function
def randomnew():
    global num 
    #generating new number
    num=randint(1, 10)
    guess_box.delete(0, END)
    #change color to normal
    label_number.config(bg = "SystemButtonFace", text="Pick number between\n1 - 10")
    window.config(bg = "SystemButtonFace")

guess_box=Entry(window, font=("Helvetica",90), width=2)
guess_box.pack(pady=20)

guess_button=Button(window, text="Submit", command=guesser)
guess_button.pack(pady=20)

reset_button=Button(window, text="New Game", command=randomnew)
reset_button.pack(pady=20)

#call random function starting new game
randomnew()
window.mainloop()