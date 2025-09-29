from tkinter import *

window = Tk()
window.geometry("420x420")
window.configure(bg="black")
window.resizable(False, False)





def click_me():
    button_for_greeting.destroy()


    # Entry Widget
    def on_entry_click(event):
        if user_name.get() == "What is your name?: ":
            user_name.delete(0,END)
            user_name.config(fg = "black", bg = "white")
    def on_focus_out(event):
        if user_name.get() == "":
            user_name.insert(0, "What is your name? ")
            user_name.config(fg = "grey", bg = "white")
    user_name = Entry(window,
                      fg= "black",
                      bg = "white",
                      font= ('Arial', 20)
                      )
    user_name.insert(0, "What is your name?: ")
    user_name.bind("<FocusIn>", on_entry_click)
    user_name.bind("<FocusOut>", on_focus_out)
    user_name.grid(row= 0, column= 0, pady = 160, padx = 20)

    # Submit Widget
    def submit():
        
        user = user_name.get()
        if user == "What is your name?: ":
            user = ""
        user_name.destroy()
        submet.destroy()
    
        label = Label(window, text= f"Hello {user}", 
                    height= 120,
                    width= 60,
                    fg = "white",
                    bg = "black",
                    font= ('Arial', 20))
        label.pack(pady=160)
    ##Submit Button

    submet = Button(window, text = "Submit", command= submit)
    submet.grid(row = 0, column= 1)


button_for_greeting = Button(window, text="Click Me! ",
                             fg= "Black",
                             width= 10,
                             height= 5,
                             command= click_me)
button_for_greeting.pack(pady=160)



window.mainloop()