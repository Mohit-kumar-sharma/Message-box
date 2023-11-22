from tkinter import *
import tkinter. messagebox as tmsg
root= Tk()
root.geometry("700x300")
root.title("Tkinter with message and dialog box")

def myfunc():
    print("For New file ")
def king():
    print(" open A New Page")
def Save():
    print("To save a file")
def SaveAs():
    print("Again save a same file with different name")
def prints():
    print("Printing a Page")
def undo():
    print("for come back anything shorcut key ctrl+z")
def Redo():
    print("To reverse your last undo shorcut key ctrl+Y")
def Cut():
    print("To cut a small thing")
def Copy():
    print("Copy anything shorcut key ctrl+C")
def Paste():
    print("paste any data from anywhere shorcut key ctrl+V")
def Find():
    print("To find the first letter or any word shorcut key Ctrl+F")
def Replace():
    print("To replace any thing from new thing")
def help():
    print ("what i can help you")
    tmsg.showinfo("Help","I will help you with this gui")
def Rate():
    print("Rate us")
    value=tmsg.askquestion("was your experience good","you used this gui..... was your experience good")
    if value == "yes":
        Message="great ? Rate us on appstore please"
    else:
        Message="tell us what is wrong We will call you"
    tmsg.showinfo("Experience" , Message)
def submit():
    Ans= tmsg.askretrycancel("you want to submit your project"," you late")
    if Ans:
        print("please submit it")
    else:
        print("your time is lost")


    

Mainmenu= Menu(root)
m1=Menu(Mainmenu , tearoff=0)


m1.add_command(label="New",command=myfunc)
m1.add_command(label="Open",command=king)
m1.add_separator()
m1.add_command(label="Save",command=Save)
m1.add_command(label="Save As",command=SaveAs)
m1.add_separator()
m1.add_command(label="Print",command=prints)
m1.add_command(label="quit",command=quit)
root.config(menu=Mainmenu)
Mainmenu.add_cascade(label="File",menu=m1)


m2=Menu(Mainmenu , tearoff=0)


m2.add_command(label="undo",command=undo)
m2.add_command(label="Redo",command=Redo)
m2.add_separator()
m2.add_command(label="Cut",command=Cut)
m2.add_command(label="Copy",command=Copy)
m2.add_command(label="Paste",command=Paste)
m2.add_separator()
m2.add_command(label="find",command=Find)
m2.add_command(label="replace",command=Replace)
root.config(menu=Mainmenu)
Mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(Mainmenu , tearoff=0)

m3.add_command(label="Select all")
m3.add_command(label="Expand selection")
m3.add_command(label="shrink selection")
m3.add_separator()
m3.add_command(label="Copy line up ")
m3.add_command(label="Copy Line Down")
m3.add_command(label="Move line up")
m3.add_command(label="Move line Down")
m3.add_command(label="Duplicate selction")
m3.add_separator()
root.config(menu=Mainmenu)
Mainmenu.add_cascade(label="Selection",menu=m3)

m4=Menu(Mainmenu , tearoff=0)

m4.add_command(label="Help",command=help)
m4.add_command(label="Rate us",command=Rate)
m4.add_command(label="Submit",command=submit)
Mainmenu.add_cascade(label="help",menu=m4)
root.config(menu=Mainmenu)

root.mainloop()