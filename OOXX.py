from tkinter import *

total = 0
def btntext(num):
    global  total
    if num==1:
        if total%2==0:
            btn1.config(text="O")
            total=total+1
        else:
            btn1.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    elif num == 2:
        if total%2==0:
            btn2.config(text="O")
            total=total+1
        else:
            btn2.config(text="X")
            total=total+1
        btn2.config(state=DISABLED)
    elif num == 3:
        if total%2==0:
            btn3.config(text="O")
            total=total+1
        else:
            btn3.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    elif num == 4:
        if total%2==0:
            btn4.config(text="O")
            total=total+1
        else:
            btn4.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    elif num == 5:
        if total%2==0:
            btn5.config(text="O")
            total=total+1
        else:
            btn5.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    elif num == 6:
        if total%2==0:
            btn6.config(text="O")
            total=total+1
        else:
            btn6.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    elif num == 7:
        if total%2==0:
            btn7.config(text="O")
            total=total+1
        else:
            btn7.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    elif num == 8:
        if total%2==0:
            btn8.config(text="O")
            total=total+1
        else:
            btn8.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    elif num == 9:
        if total%2==0:
            btn9.config(text="O")
            total=total+1
        else:
            btn9.config(text="X")
            total=total+1
        btn1.config(state=DISABLED)
    #判斷OX

    if btn1.cget("text") == btn2.cget("text") and btn1.cget("text") == btn3.cget("text"):
        if btn1.cget("text") == "O":
            print("先手者勝利")
        elif btn1.cget("text") == "X":
            print("後手者勝利")
    
    if btn4.cget("text") == btn5.cget("text") and btn4.cget("text") == btn6.cget("text"):
        if btn4.cget("text") == "O":
            print("先手者勝利")
        elif btn4.cget("text") == "X":
            print("後手者勝利")
    
    if btn7.cget("text") == btn8.cget("text") and btn7.cget("text") == btn9.cget("text"):
        if btn7.cget("text") == "O":
            print("先手者勝利")
        elif btn7.cget("text") == "X":
            print("後手者勝利")

    if btn1.cget("text") == btn4.cget("text") and btn1.cget("text") == btn7.cget("text"):
        if btn1.cget("text") == "O":
            print("先手者勝利")
        elif btn1.cget("text") == "X":
            print("後手者勝利")
    
    if btn2.cget("text") == btn5.cget("text") and btn2.cget("text") == btn8.cget("text"):
        if btn2.cget("text") == "O":
            print("先手者勝利")
        elif btn2.cget("text") == "X":
            print("後手者勝利")

    if btn3.cget("text") == btn6.cget("text") and btn3.cget("text") == btn9.cget("text"):
        if btn3.cget("text") == "O":
            print("先手者勝利")
        elif btn3.cget("text") == "X":
            print("後手者勝利")

    if btn1.cget("text") == btn5.cget("text") and btn1.cget("text") == btn9.cget("text"):
        if btn1.cget("text") == "O":
            print("先手者勝利")
        elif btn1.cget("text") == "X":
            print("後手者勝利")

    if btn3.cget("text") == btn5.cget("text") and btn3.cget("text") == btn7.cget("text"):
        if btn3.cget("text") == "O":
            print("先手者勝利")
        elif btn3.cget("text") == "X":
            print("後手者勝利")
    #判斷輸贏

window = Tk()
window.geometry("800x800+400+200")
window.title="OOXXgmae"

window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
#直
window.columnconfigure(1, weight=1) 
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
#橫

btn1 = Button(window, text="", command=lambda:btntext(1))
btn1.grid(row=1, column=1, sticky="nsew") 
btn2 = Button(window, text="", command=lambda:btntext(2))
btn2.grid(row=1, column=2, sticky="nsew")
btn3 = Button(window, text="", command=lambda:btntext(3))
btn3.grid(row=1, column=3, sticky="nsew")

btn4 = Button(window, text="", command=lambda:btntext(4))
btn4.grid(row=2, column=1, sticky="nsew")
btn5 = Button(window, text="", command=lambda:btntext(5))
btn5.grid(row=2, column=2, sticky="nsew")
btn6 = Button(window, text="", command=lambda:btntext(6))
btn6.grid(row=2, column=3, sticky="nsew")

btn7 = Button(window, text="", command=lambda:btntext(7))
btn7.grid(row=3, column=1, sticky="nsew")
btn8 = Button(window, text="", command=lambda:btntext(8))
btn8.grid(row=3, column=2, sticky="nsew")
btn9 = Button(window, text="", command=lambda:btntext(9))
btn9.grid(row=3, column=3, sticky="nsew")

window.mainloop()