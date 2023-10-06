from tkinter import *
from PIL import Image,ImageTk
from random import randint


#main window
root = Tk()
root.title("Rock-Paper-Scissors")
root.configure(background = "#3b0053")

#pictures section
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor-user.png"))
rock_img_sys = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_sys = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_sys = ImageTk.PhotoImage(Image.open("scissor.png"))

#insert picture
user_label = Label(root,image = scissor_img, bg="#3b0053")
sys_label = Label(root,image = scissor_img_sys, bg="#3b0053")
sys_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
playerScore = Label(root,text=0,font=100,
                    bg="#3b0053",fg="white")
systemScore = Label(root,text=0,font=100,
                    bg="#3b0053",fg="white")
systemScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#messages
msg=Label(root,font=50,bg="#3b0053",fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#update system score
def updateSystemScore():
    score = int(systemScore["text"])
    score += 1
    systemScore["text"] = str(score)

#check winner
def checkWin(player, system):
    if player == system:
        updateMessage("It's a tie!!")
    elif player == "rock":
            if system == "paper":
                updateMessage("You loose :(")
                updateSystemScore()
            else:
                updateMessage("You win :)")
                updateUserScore()
    elif player == "paper":
            if system == "scissor":
                updateMessage("You loose :(")
                updateSystemScore()
            else:
                updateMessage("You win :)")
                updateUserScore()
    elif player == "scissor":
            if system == "rock":
                updateMessage("You loose :(")
                updateSystemScore()
            else:
                updateMessage("You win :)")
                updateUserScore()
    else:
        pass





#update choices
choices=["rock", "paper", "scissor"]
def updateChoice(x):

#for system

    sysChoice=choices[randint(0,2)]
    if sysChoice == "rock":
        sys_label.configure(image=rock_img_sys)
    elif sysChoice == "paper":
        sys_label.configure(image=paper_img_sys)
    else:
        sys_label.configure(image=scissor_img_sys)

#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,sysChoice)


#indicators
user_indicator=Label(root,font=50,text="USER",bg="#3b0053",fg="white")
sys_indicator=Label(root,font=50,text="SYSTEM",bg="#3b0053",fg="white")
user_indicator.grid(row=0,column=3)
sys_indicator.grid(row=0,column=1)


#buttons
rock=Button(root,width=20,height=2,text="ROCK",
            bg="#0046c0",fg="white",command=lambda:updateChoice("rock")).grid(row=2, column=1)
paper=Button(root,width=20,height=2,text="PAPER",
             bg="#5d6bd0",fg="white",command=lambda:updateChoice("paper")).grid(row=2, column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",
               bg="#0087ff",fg="white",command=lambda:updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()