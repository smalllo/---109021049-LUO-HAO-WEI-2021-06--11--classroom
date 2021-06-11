from tkinter import *

def btntext(num):
    if num==1:
        btn1.config(text="O")
    elif num == 2:
        btn2.config(text="O")
    elif num == 3:
        btn3.config(text="O")
    elif num == 4:
        btn4.config(text="O")
    elif num == 5:
        btn5.config(text="O")
    elif num == 6:
        btn6.config(text="O")
    elif num == 7:
        btn7.config(text="O")
    elif num == 8:
        btn8.config(text="O")
    elif num == 9:
        btn9.config(text="O")

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