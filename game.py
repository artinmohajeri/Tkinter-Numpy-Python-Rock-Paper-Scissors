from tkinter import *
from numpy import random
def reset():
    lbl_result_computer["text"] = 0
    lbl_result_user["text"] = 0
    lbl["text"] = "Computer chosse: "

def rock():
    lbl["text"] = f"Computer chosse: {random.choice(["Rock","Paper","Scissor"])}"
    if lbl["text"] == "Computer chosse: Paper":
        lbl_result_computer["text"] +=1
    elif lbl["text"] == "Computer chosse: Scissor":
        lbl_result_user["text"] +=1
def paper():
    lbl["text"] = f"Computer chosse: {random.choice(["Rock","Paper","Scissor"])}"
    if lbl["text"] == "Computer chosse: Scissor":
        lbl_result_computer["text"] +=1
    elif lbl["text"] == "Computer chosse: Rock":
        lbl_result_user["text"] +=1
def scissor():
    lbl["text"] = f"Computer chosse: {random.choice(["Rock","Paper","Scissor"])}"
    if lbl["text"] == "Computer chosse: Rock":
        lbl_result_computer["text"] +=1
    elif lbl["text"] == "Computer chosse: Paper":
        lbl_result_user["text"] +=1

WIDTH, HEIGHT = 600,500
WIN = Tk()
WIN.title("Rock Paper Scissors Game")
WIN.minsize(WIDTH, HEIGHT)
WIN.iconbitmap("./img/icon.ico")

WIN.rowconfigure([0,1], weight=1)
WIN.columnconfigure(0, weight=1)

lbl = Label(WIN, text="Computer choose: ",height=2, font=("None",20,"bold"), bg="lightgrey")
lbl.grid(row=0, column=0, sticky="nwe")

frm_btn = Frame(WIN, height=100)
frm_btn.grid(row=1, column=0, sticky="wen")

frm_btn.rowconfigure(0, weight=1)
frm_btn.columnconfigure([0,1,2], weight=1)

stone_btn = Button(frm_btn, text="Rock", height=3, command=rock, bg="lightgrey")
paper_btn = Button(frm_btn, text="Paper", height=3, command=paper, bg="lightgrey")
scissor_btn = Button(frm_btn, text="Scissor", height=3, command=scissor, bg="lightgrey")

stone_btn.grid(row=0, column=0, sticky="nwes",padx=2)
paper_btn.grid(row=0, column=1, sticky="nwes", padx=2)
scissor_btn.grid(row=0, column=2, sticky="nwes", padx=2)

frm_result = Frame(WIN, height=200)
frm_result.rowconfigure([0,1], weight=1)
frm_result.columnconfigure([0,1], weight=1)

lbl_result_name_user = Label(frm_result, text="Your Score: ", font=("None",14), relief="ridge" , height=2, bg="lightgreen")
lbl_result_name_computer = Label(frm_result, text="Computer Score: ", font=("None",14), relief="ridge" , height=2, bg="lightcoral")

lbl_result_name_user.grid(row=0, column=0, sticky="nswe")
lbl_result_name_computer.grid(row=0, column=1, sticky="nswe")

lbl_result_user = Label(frm_result, text=0,bg="lightgreen", font=("None",20, "bold"), height=6, relief="ridge")
lbl_result_user.grid(row=1, column=0, sticky="nswe",)
lbl_result_computer = Label(frm_result, text=0,bg="lightcoral", font=("None",20, "bold"), height=6, relief="ridge")
lbl_result_computer.grid(row=1, column=1, sticky="nswe",)

frm_result.grid(row=2, column=0, sticky="nswe")

btn_reset = Button(WIN, text="start again", font=("None",15), relief="ridge", command=reset)
btn_reset.grid(row=3,column=0, sticky="nwse")

WIN.mainloop()