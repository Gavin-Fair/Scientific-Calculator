from tkinter import *

# window setup/ initial setup

window = Tk()
window.geometry("450x370")
window.resizable(width=False, height=False)
window.title("Scientific Calculator")
icon = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\cole\calc.png")
window.iconphoto(True, icon)
answer = []


# functions

def onenum():
    answer.append("1")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def twonum():
    answer.append("2")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def threenum():
    answer.append("3")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def fournum():
    answer.append("4")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def fivenum():
    answer.append("5")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def sixnum():
    answer.append("6")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def sevnum():
    answer.append("7")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def eightnum():
    answer.append("8")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def ninenum():
    answer.append("9")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def clearfun():
    answer.clear()
    total = Label(window,
                  text="                                          ",
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def pnfun():
    answer.insert(0, "-")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def equalfun():
    TotalC = Label(window,
                   text="                                       ",
                   font=("Arial", 30, "bold"),
                   bg="#f4e6b3")
    TotalC.place(x=0, y=15)
    str1 = ""
    answer1 = eval(str1.join(answer))
    total = Label(window,
                  text=answer1,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def multfun():
    answer.append("*")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def divfun():
    answer.append("/")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def subfunc():
    answer.append("-")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def addfunc():
    answer.append("+")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def percfunc():
    total3 = Label(window, text="                                       ",
                   font=("Arial", 30, "bold"),
                   bg="#f4e6b3")
    total3.place(x=0, y=15)
    str1 = ""
    answer2 = eval(str1.join(answer))
    answer3 = answer2 / 100
    total = Label(window,
                  text=answer3,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def decfunc():
    answer.append(".")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


def zerofunc():
    answer.append("0")
    total = Label(window,
                  text=answer,
                  font=("Arial", 30, "bold"),
                  bg="#f4e6b3")
    total.place(x=0, y=15)


# number Buttons

headerpic = PhotoImage(file="header3.png")
header = Label(window, image=headerpic)
header.pack()

clearpic = PhotoImage(file="button_c.png")
clear = Button(window, image=clearpic, highlightthickness=0, bd=0, command=clearfun)
clear.place(x=0, y=80)

pnpic = PhotoImage(file="neg.png")
pn = Button(window, image=pnpic, highlightthickness=0, bd=0, command=pnfun)
pn.place(x=115, y=80)

perpic = PhotoImage(file="per.png")
per = Button(window, image=perpic, highlightthickness=0, bd=0, command=percfunc)
per.place(x=230, y=80)

divpic = PhotoImage(file="div.png")
div = Button(window, image=divpic, highlightthickness=0, bd=0, command=divfun)
div.place(x=345, y=80)

sevpic = PhotoImage(file="7.png")
sev = Button(window, image=sevpic, highlightthickness=0, bd=0, command=sevnum)
sev.place(x=0, y=140)

eightpic = PhotoImage(file="8.png")
eight = Button(window, image=eightpic, highlightthickness=0, bd=0, command=eightnum)
eight.place(x=115, y=140)

ninepic = PhotoImage(file="9.png")
nine = Button(window, image=ninepic, highlightthickness=0, bd=0, command=ninenum)
nine.place(x=230, y=140)

multpic = PhotoImage(file="X.png")
mult = Button(window, image=multpic, highlightthickness=0, bd=0, command=multfun)
mult.place(x=345, y=140)

fourpic = PhotoImage(file="4.png")
four = Button(window, image=fourpic, highlightthickness=0, bd=0, command=fournum)
four.place(x=0, y=200)

fivepic = PhotoImage(file="5.png")
five = Button(window, image=fivepic, highlightthickness=0, bd=0, command=fivenum)
five.place(x=115, y=200)

sixpic = PhotoImage(file="6.png")
six = Button(window, image=sixpic, highlightthickness=0, bd=0, command=sixnum)
six.place(x=230, y=200)

subpic = PhotoImage(file="sub.png")
sub = Button(window, image=subpic, highlightthickness=0, bd=0, command=subfunc)
sub.place(x=345, y=200)

onepic = PhotoImage(file="1.png")
one = Button(window, image=onepic, highlightthickness=0, bd=0, command=onenum)
one.place(x=0, y=260)

twopic = PhotoImage(file="2.png")
two = Button(window, image=twopic, highlightthickness=0, bd=0, command=twonum)
two.place(x=115, y=260)

threepic = PhotoImage(file="3.png")
three = Button(window, image=threepic, highlightthickness=0, bd=0, command=threenum)
three.place(x=230, y=260)

pluspic = PhotoImage(file="+.png")
plus = Button(window, image=pluspic, highlightthickness=0, bd=0, command=addfunc)
plus.place(x=345, y=260)

zeropic = PhotoImage(file="0.png")
zero = Button(window, image=zeropic, highlightthickness=0, bd=0, command=zerofunc)
zero.place(x=0, y=320)

decpic = PhotoImage(file="..png")
dec = Button(window, image=decpic, highlightthickness=0, bd=0, command=decfunc)
dec.place(x=230, y=320)

equalpic = PhotoImage(file="=.png")
equal = Button(window, image=equalpic, highlightthickness=0, bd=0, command=equalfun)
equal.place(x=345, y=320)

window.mainloop()
