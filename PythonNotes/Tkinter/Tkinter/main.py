from tkinter import *
window = Tk() ##Instatiated window
window.title("New Title") ##Changes title of the window
icon = PhotoImage(file='SJW_MEWING.png') ##Holds container for photo
window.iconphoto(True, icon) ##Changes icon of the GUI
window.config(background="Black")
label = Label(window, text = "Did you mew today?",
               font= ('Arial', 40, 'bold'), 
               fg= 'blue', 
               bg = "white",
               relief= RAISED,
               bd = 10,
               padx = 40,
                pady= 40,
                image= icon,
                compound= 'top'              ) 
##Fg = foreground 
## bg = background
label.pack()
window.mainloop() ##Display window
