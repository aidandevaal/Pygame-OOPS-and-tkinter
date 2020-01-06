from tkinter import *
root = Tk()

class Win(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_win()

    def init_win(self):
        
        self.master.title("GUI")
        
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)

        file.add_command(label="New", command=self.client_new)
        
        file.add_command(label="Exit", command=self.client_exit)
        
        menu.add_cascade(label="File", menu=file)
        
        edit = Menu(menu)
        
        edit.add_command(label="Undo")
        
        menu.add_cascade(label="Edit", menu=edit)

    def client_exit(self):
        exit ()

root.geometry("400x300")

app = Win(root)

root.mainloop()
root.destroy()


