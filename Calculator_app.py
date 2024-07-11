import customtkinter as ctk


# FUNCTION TO SHOW THE RESULT TO THE USER
def show_label(char_list, result):
    
    # FRAME TO SHOW THE RESULT
    frame = ctk.CTkFrame(wn, height=100, width=215, fg_color="black")
    frame.place(x=10, y=10)
    
    # FETCHING THE DATA TO SHOW
    if result != None:
        char = str(result)
    else:
        char = ""
        for chr in char_list:
            if chr == None:
                pass
            else:
                chr = str(chr)
                char += chr
    
    # IF LEN OF ENTERED CHAR IS MORE THAN ENOUGH TO SHOW
    if char != None:          
        if len(char) < 14:
            labels = ctk.CTkLabel(frame, text=char, font=("Helvetica", 24, "bold"))
            labels.place(x=10, y=50)
        else:
            # MAKING THE LABEL SMALLER TO SHOW MORE
            labels = ctk.CTkLabel(frame, text=char, font=("Helvetica", 18, "bold"))
            labels.place(x=10, y=50)


# FUNCTION TO DO THE MATHEMATICAL OPEARIONS
def math_operation(x, y, operator):
    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "x":
        return x*y
    elif operator == "/":
        # CANNOT DIVISABLE WITH ZERO
        if x == 0 or y == 0:
            return 0
        else :
            return x/y


x, y, oper, result = None, None, None, None
labels = []

# THE BACKEND FUNCTION TO GET THE RESULT
def get_label(label):
    global x, oper, y, labels, result
    operators = ["+", "-", "x", "/"]
    funcs = ["all", "one", "="] 
    
    length_of_char = 0
    values_in_labels = [x for x in labels]
    for value in values_in_labels:
        if value == None:
            pass
        else:
            value=str(value)
            length_of_char += len(value)
    
    # TO NOT TAKE ANY VALUES AFTER ENTERING 17 VALUES
    if length_of_char > 17 and label not in funcs:
        pass
    
    elif result != None:
        if label in operators:
            y = result
            result=None
            oper = label
        elif label in funcs:
            if label == "=":
                pass
            elif label == "one":
                result = str(result)
                result_list = [x for x in result]
                result_list.pop(-1)
                result = "".join(result_list)
            elif label == "all":
                result = None
        else:
            result=None
            get_label(label)
    
    # TO PERFORM NOTHING WHEN NOT ENTERED ANY VALUE   
    elif x==None and y==None and label in operators:
        pass
        
    elif label in operators or label in funcs:
        if label in operators:
            if oper == None:
                oper = label
                if y == None:
                    y = x
                    x = None
                else:
                    pass
                
            else:
                if x==None and label in operators:
                    oper = label
                else:
                    try:
                        if type(y) == int:
                            x = int(x)
                        else:
                            x, y = int(x), int(y)
                            
                    except:
                        x, y = float(x), float(y)
                    y = math_operation(x, y, oper)
                    x, oper = None, label
                    
        else: # IF LABEL IS A FUCNTION
            
            #  FUNCTION TO REMOVE ALL ENTERED ITEMS  (ALL CLEAR)
            if label == "all":
                labels = []
                x, y, oper = None, None, None
                
            # FUNCTION TO REMOVE ONE BY ONE  (CLEAR)
            elif label == "one":
                if x != None:
                    if len(x) >= 2:
                        list_x = [i for i in x]
                        list_x.pop(-1)
                        x = "".join(list_x)
                    else:
                        x = None
                elif oper != None:
                    oper = None
                elif y != None:
                    if len(y) >= 2:
                        list_y = [i for i in y]
                        list_y.pop(-1)
                        y = "".join(list_y)
                    else:
                        y = None
                else:
                    pass
                
            # IF THE ENTERED FUNCTION IS EQUAL  (EQUAL)
            else:
                if x != None and y != None:
                    if type(y) == int:
                        x = int(x)
                    elif type(y)==float:
                        x = int(x)
                    else:
                        try:
                            x, y = int(x), int(y)
                        except:
                            x, y = float(x), float(y)
                    result = math_operation(y, x, oper) # we are changing the x value to y in the previous step, why so we giving x as second and y as first value
                    x, y, oper = None, None, None
                else:
                    pass
    
    # IF . ENTERED BEFORE ENTERING ANY NUMBER
    elif label == "." and x==None:
        x = "0."               
                    
    else:
        if x == None:
            x = label
        else:
            x += label
                    

    labels = [y, oper, x]
    show_label(labels, result)



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

    # INITIALISING BUTTONS  
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
    # OPERATORS
    be = ctk.CTkButton(master=wn, fg_color="orange", height=105, width=50, corner_radius=7, command=lambda:get_label("="),text='=', font=("Helvetica", 20))
    bdiv = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("/"), text='/', font=("Helvetica", 15))
    bmul = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("x"), text='x', font=("Helvetica", 15))
    bsub = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("-"), text='-', font=("Helvetica", 25))
    badd = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, command=lambda:get_label("+"), text='+', font=("Helvetica", 20))
    # BUTTONS FOR CLEARING
    bac = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, text="AC", command=lambda:get_label("all"), font=("Helvetica", 15, "bold"))
    bc = ctk.CTkButton(master=wn, fg_color="orange", height=50, width=50, corner_radius=7, text="C", command=lambda:get_label("one"), font=("Helvetica", 15, "bold"))


    # PLACING BUTTONS
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

    # TO RUN ALL CODES
    wn.mainloop()

# CALLING THE FUNCTION    
main()