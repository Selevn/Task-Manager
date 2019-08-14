import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Task import *

class Windowa():
    def __init__(self, mw):
        self.tasks = DataBase()
        self.tasks.createtable()
        
        
        self.stylebuttonbotbar = ttk.Style()
        #self.stylebuttonbotbar.map("BotBut", pady = '10')
        self.stylebuttonbotbar.map("BotBut",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'white')]
            )        
        
        
        
        
        self.mainwindow = mw
        self.toolbar = tk.Frame(self.mainwindow, height = '90', bg = '#c0c0c0', borderwidth=4)
        self.toolbar.pack(fill = tk.X)
        
        self.mainbar = tk.Frame(self.mainwindow, bg = '#fefefe')
        self.mainbar.pack(fill = tk.BOTH, expand=tk.YES)
        
        self.botbar = tk.Frame(self.mainwindow, bg = '#e0e0e0', height = '90')
        self.botbar.pack(fill = tk.X)
        
        self.butstartwork = tk.Button(self.botbar, text = 'Start working', bg = "#5CFFAB", font = 'Arial 16', command =self.work_def)
        self.butstartwork.place(relx = .5, rely = .47, anchor = tk.CENTER)
        
        self.maintree = tk.ttk.Treeview(self.mainbar, columns=('Id', 'Header', 'Body', 'Status'), height=15, show='headings')
        self.maintree.pack()
        
        self.maintree.column('Id', width = '10', anchor=tk.W)
        self.maintree.column('Header', width = '120', anchor=tk.W)
        self.maintree.column('Body', width = '280', anchor=tk.W)
        self.maintree.column('Status', width = '75', anchor=tk.W)
        
        self.maintree.heading('Id', text = 'Id')
        self.maintree.heading('Header', text = 'Header')
        self.maintree.heading('Body', text = 'Body')
        self.maintree.heading('Status', text = 'Status')
        self.load_and_show_db()
        
    def load_and_show_db(self):
        array = self.tasks.get_all()
        for everylist in array:
            self.maintree.insert('','end',values = everylist)
        
        
        
    def work_def(self):
        if self.butstartwork['text'] == 'Start working':
            self.butstartwork['text'] = 'Stop working'
            self.butstartwork['bg'] = '#EC5951'
            self.alert_enable = True
            self.butstartwork.after(1200000, self.alert) #1200000
        else:
            self.butstartwork['text'] = 'Start working'
            self.butstartwork['bg'] = "#5CFFAB"
            self.alert_enable = False
            
    def alert(self):
        if self.alert_enable:
            #self.mainwindow.focus_set()
            messagebox.showinfo("Time to relax!", "Whatch out for 20 seconds please!")
            self.butstartwork.after(1200000, self.alert)
            
        
        




if __name__ == '__main__':
    root = tk.Tk()
    root.title('Task Manager')
    root.geometry('600x500')
    q = Windowa(root)
    root.mainloop()