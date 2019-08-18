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
        self.load_header_buttons()
        
    def load_header_buttons(self):
        self.add_but = tk.Button(self.toolbar, text = 'Add', font = 'Arial 14', command = self.add)
        self.delete_but = tk.Button(self.toolbar, text = 'Delete', font = 'Arial 14')
        self.to_daily_but = tk.Button(self.toolbar, text = 'Add to daily', font = 'Arial 14')
        self.add_but.place(rely = 0.5, relx = 0.1, anchor = tk.CENTER, width = 110)
        self.delete_but.place(rely = 0.5, relx = 0.3, anchor = tk.CENTER, width = 110)
        self.to_daily_but.place(rely = 0.5, relx = 0.5, anchor = tk.CENTER, width = 110)
        
    def add(self):
        Dialog()
        
        
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
            
class Dialog(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.title('Add new task')
        self.geometry('370x350')
        self.resizable(False, False)
        
        label1 = tk.Label(self, text = 'Header:', font = 'Arial 12')
        label1.place(x = 20, y = 20)
        label2 = tk.Label(self, text = 'Body:', font = 'Arial 12')
        label2.place(x = 20, y = 50)
        
        entry1 = tk.Entry(self, font = 'Arial 12')
        entry1.place(x = 100, y = 20)
        entry2 = tk.Text(self, height = 10, width = 20, font = 'Arial 12')
        entry2.place(x = 100, y = 50)
        
        add_but = tk.Button(self, text = "Add", font = 'Arial 12')
        add_but.place(relx = 0.5, rely = 0.83, anchor = tk.CENTER, command = put)
        
        
        
        self.grab_set()
        self.focus_set()  
        
    def put():
        header = entry1.get()
        body = entry2.get()
        status = ''
        
        #self.add_window.mainloop()        
        




if __name__ == '__main__':
    root = tk.Tk()
    root.title('Task Manager')
    root.geometry('600x500')
    q = Windowa(root)
    root.mainloop()