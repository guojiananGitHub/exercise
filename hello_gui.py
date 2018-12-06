# from tkinter import *
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text="Quit", command=self.quit)
#         self.quitButton.pack()
#
#
# app = Application()
# app.master.title("Hello world")
# app.mainloop()

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
