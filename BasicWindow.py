from tkinter import *

root = Tk()

topFrame = Frame (root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg="red")
button2 = Button(topFrame, text = "Button 2", fg="yellow")
button3 = Button(topFrame, text = "Button 3", fg="green")
button4 = Button(topFrame, text = "Button 4", fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
button4.pack(side=BOTTOM)
root.mainloop()

