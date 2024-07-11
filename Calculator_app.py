import customtkinter as ctk



def get_label(label):
    print("label :", label)


# THE CALCULATOR UI
def main():
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("dark-blue")
    
    global wn
    wn = ctk.CTk()
    wn.title("Calculator")
    wn.configure(bg="system") # system theme
    wn.geometry("235x400")
    wn.resizable(False, False) # can't expand the window, fixed height and width


    frame = ctk.CTkFrame(wn, height=100, width=215, fg_color="black")
    frame.place(x=10, y=10)

    # Initialising buttons    
    b1 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("1"), text="1", font=("Helvetica", 15))
    b2 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("2"), text="2", font=("Helvetica", 15))
    b3 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("3"), text="3", font=("Helvetica", 15))
    b4 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("4"), text="4", font=("Helvetica", 15))
    b5 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("5"), text="5", font=("Helvetica", 15))
    b6 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("6"), text="6", font=("Helvetica", 15))
    b7 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("7"), text="7", font=("Helvetica", 15))
    b8 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("8"), text="8", font=("Helvetica", 15))
    b9 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("9"), text="9", font=("Helvetica", 15))
    b0 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("0"), text="0", font=("Helvetica", 15))
    b00 = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7,command=lambda:get_label("00"), text="00" , font=("Helvetica", 15))
    bp = ctk.CTkButton(master=wn, fg_color="gray", height=50, width=50, corner_radius=7, command=lambda:get_label("."), text='.', font=("Helvetica", 15))
    # operators
    be = ctk.CTkButton(master=wn, fg_color="orange", height=105, width=50, corner_radius=7, command=lambda:get_label("="),text='=', font=("Helvetica", 20))
    bdiv = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("/"), text='/', font=("Helvetica", 15))
    bmul = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("x"), text='x', font=("Helvetica", 15))
    bsub = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("-"), text='-', font=("Helvetica", 25))
    badd = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("+"), text='+', font=("Helvetica", 20))
    # clearing buttons
    bac = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, text="AC", command=lambda:get_label("all"), font=("Helvetica", 15, "bold"))
    bc = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, text="C", command=lambda:get_label("one"), font=("Helvetica", 15, "bold"))


    # placing buttons
    b00.place(x=10, y=340)
    b0.place(x=65, y=340)
    bp.place(x=120, y=340)
    be.place(x=175, y=285)

    # 2nd row from bottom
    b7.place(x=10, y=285)
    b8.place(x=65, y=285)
    b9.place(x=120, y=285)

    # 3rd row from bottom
    b4.place(x=10, y=230)
    b5.place(x=65, y=230)
    b6.place(x=120, y=230)
    bdiv.place(x=175, y=230)

    # 4th row from bottom
    b1.place(x=10, y=175)
    b2.place(x=65, y=175)
    b3.place(x=120, y=175)
    bmul.place(x=175, y=175)

    # first row
    bac.place(x=10, y=120)
    bc.place(x=65, y=120)
    badd.place(x=120, y=120)
    bsub.place(x=175, y=120)




    wn.mainloop()
    
main()