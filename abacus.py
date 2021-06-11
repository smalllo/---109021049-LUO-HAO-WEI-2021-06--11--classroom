from tkinter import *

allFlag = False
all = 0
a1 = 0

def change(num):
    if int(lab0["text"]) != 0:
        lab0["text"] = lab0["text"] + num
    else:
        lab0["text"] = num
#清0輸入數字
def allset(allvalue):
    global all
    global a1  
    global allFlag
    a1 = int(lab0["text"])
    all = allvalue

def change_2():
    a2 = int(lab0["text"])
    global all
    if all == 1:
        lab0["text"] = a1 + a2
    elif all == 2:
        lab0["text"] = a1 - a2
    elif all == 3:
        lab0["text"] = a1 * a2
    elif all == 4:
        lab0["text"] = a1 // a2
        #還未完成

# def clearTextInput():
#     lab0.delete("1.0","end")
# #清除lab內數字(有bug)

window = Tk()
window.geometry("400x400+200+100")
window.title="OOXXgmae"

lab0 = Label(window, text="0", justify="left", anchor="w")
lab0.grid(row=0, column=0, columnspan=3, sticky="ew")

window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
#直
window.columnconfigure(1, weight=1) 
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
#橫

btn1 = Button(window, text="7", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("7"))
btn1.grid(row=1, column=1, sticky="nsew") 
btn2 = Button(window, text="8", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("8"))
btn2.grid(row=1, column=2, sticky="nsew")
btn3 = Button(window, text="9", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("9"))
btn3.grid(row=1, column=3, sticky="nsew")
btn4 = Button(window, text="X", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:allset("3"))
btn4.grid(row=1, column=4, sticky="nsew")

btn5 = Button(window, text="4", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("4"))
btn5.grid(row=2, column=1, sticky="nsew")
btn6 = Button(window, text="5", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("5"))
btn6.grid(row=2, column=2, sticky="nsew")
btn7 = Button(window, text="6", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("6"))
btn7.grid(row=2, column=3, sticky="nsew")
btn8 = Button(window, text="-", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:allset("2"))
btn8.grid(row=2, column=4, sticky="nsew")

btn9 = Button(window, text="1", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("1"))
btn9.grid(row=3, column=1, sticky="nsew")
btn10 = Button(window, text="2", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("2"))
btn10.grid(row=3, column=2, sticky="nsew")
btn11 = Button(window, text="3", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("3"))
btn11.grid(row=3, column=3, sticky="nsew")
btn12 = Button(window, text="+", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:allset("1"))
btn12.grid(row=3, column=4, sticky="nsew")

btn13 = Button(window, text="離開", font=("Times new Roman", 15 , "bold", "italic"), command=window.destroy)
btn13.grid(row=4, column=1, sticky="nsew")
btn14 = Button(window, text="0", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change("0"))
btn14.grid(row=4, column=2, sticky="nsew")
btn15 = Button(window, text=".", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:allset("."))
btn15.grid(row=4, column=3, sticky="nsew")
btn16 = Button(window, text="/", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:allset("4"))
btn16.grid(row=4, column=4, sticky="nsew")

btn17 = Button(window, text="清除", font=("Times new Roman", 15 , "bold", "italic"), )
btn17.grid(row=5, column=1, sticky="nsew")#還無法清除
btn18 = Button(window, text="=", font=("Times new Roman", 15 , "bold", "italic"), command=lambda:change_2("4"))
btn18.grid(row=5, column=2, sticky="nsew")

window.mainloop()