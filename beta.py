from tkinter import *

def test():
    print("a")

window = Tk()
window.title("First Python Window") #設定名稱
window.geometry("600x400+100+50") #要用字串(寬x高)+橫向位移量+直向位移量
window.rowconfigure(0, weight=1) #直向
window.rowconfigure(1, weight=2)
window.rowconfigure(2, weight=3)
window.columnconfigure(0, weight=1) #橫向
window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=3)

btn0 = Button(window, text="", command=test)
btn0.grid(row=0, column=0, sticky=NSEW) #NSEW四面放大 NS上下放大 EW左右放大
btn1 = Button(window, text="", command=test)
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 = Button(window, text="", command=test)
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 = Button(window, text="", command=test)
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 = Button(window, text="", command=test)
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 = Button(window, text="", command=test)
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 = Button(window, text="", command=test)
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 = Button(window, text="", command=test)
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 = Button(window, text="", command=test)
btn8.grid(row=2, column=2, sticky=NSEW)

window.mainloop()