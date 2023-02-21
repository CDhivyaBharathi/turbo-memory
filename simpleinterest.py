from tkinter import *
def calInterest():
    p = int(p_box.get())
    t = int(t_box.get())
    r = int(p_box.get())
    interest = p*t*r/100
    final = round(interest,2)
    msg = Label(res_box,text=f"The amount is {final}",font=("comicsans",14),bg="white")
    msg.pack()


window = Tk()
window.geometry("500x500")
window.configure(bg="cyan")

a_label = Label(window,text="Simple interest.",fg="black",font=("comicsans",14),bg="cyan")
a_label.place(x=50,y=50)

p_label = Label(window,text="Enter the amount(Rs): ",fg="black",font=("comicsans",14),bg="cyan")
p_label.place(x=50,y=100)
p_box = Entry(window,font=("comicsans",14),width=10,bd=5)
p_box.place(x=230,y=100)

t_label = Label(window,text="Enter the time(yrs): ",fg="black",font=("comicsans",14),bg="cyan")
t_label.place(x=50,y=150)
t_box = Entry(window,font=("comicsans",14),width=10,bd=5)
t_box.place(x=230,y=150)

r_label = Label(window,text="Enter the interest(%): ",fg="black",font=("comicsans",14),bg="cyan")
r_label.place(x=50,y=200)
r_box = Entry(window,font=("comicsans",14),width=10,bd=5)
r_box.place(x=230,y=200)

cal_button = Button(window,text="Calculate",bg="red",fg="black",font=("comicsans",14),command=calInterest)
cal_button.place(x=250,y=250)


res_box = LabelFrame(window,text="Result",bg="white",font=("comicsans",14))
res_box.place(x=20,y=300)
res_label = Label(res_box,text="Final amount: ",bg="white",font=("comicsans",14),width=10)
res_label.place(x=0,y=300)
res_label.pack()

window.mainloop()