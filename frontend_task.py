import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Task import *

class Windowa():
    def add_bind(self,event):
        self.add()
    def del_bind(self,event):
        self.delete()   
        
    def quit_bind(self,event):
        self.quit()
        
    def quit(self):
        new = tk.Tk()
        #self.mainwindow.quit()        
        dw = Daily_window(new)
        new.mainloop()        
        
        
    def __init__(self, mw):
        self.mainwindow = mw
        self.mainwindow.title('Task Manager')
        self.mainwindow.geometry('600x500')
        
        self.tasks = DataBase()
        self.tasks.createtable()
        self.workingtable = 'tasks'   
        
        
        
        
        
        
        self.binds()
        self.toolbar = tk.Frame(self.mainwindow, height = '90', bg = '#c0c0c0', borderwidth=4)
        self.toolbar.pack(fill = tk.X)
        
        self.mainbar = tk.Frame(self.mainwindow, bg = '#fefefe')
        self.mainbar.pack(fill = tk.BOTH, expand=tk.YES)
        
        self.botbar = tk.Frame(self.mainwindow, bg = '#e0e0e0', height = '90')
        self.botbar.pack(fill = tk.X)
        
        self.butstartwork = tk.Button(self.botbar, text = 'Work with Daily', bg = "#c0c0c0", font = 'Arial 16', command =self.quit)
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
        
        
    def read(self):
        idis = self.return_read()
        if idis == False:
            return False
        if isinstance(idis, list):
            messagebox.showinfo(idis[0],idis[1])
        else:
            messagebox.showerror('Error','For reading must be selected 1 task')
            
            
    def return_read(self):
        if len(self.maintree.selection()) == 0:
            messagebox.showerror('Error','Select 1 task at least')
            return False
        elif len(self.maintree.selection()) == 1:
            quit = []
            quit.append(self.maintree.set(self.maintree.selection()[0], '#2'))
            quit.append(self.maintree.set(self.maintree.selection()[0], '#3'))
            if len(quit[1])==1:
                quit[1] = quit[0]
            return quit
        else:
            messagebox.showerror('Error','Select 1 task at least')
            return False        
            
            
    
        
    def binds(self):
        self.mainwindow.bind("<Control-Key-n>", self.add_bind)
        self.mainwindow.bind("<Delete>", self.del_bind)       
        self.mainwindow.bind("<Control-Key-z>", self.quit_bind)
        
    def load_header_buttons(self):
        self.add_but = tk.Button(self.toolbar, text = 'Add', font = 'Arial 14', command = self.add)
        self.delete_but = tk.Button(self.toolbar, text = 'Delete', font = 'Arial 14', command = self.delete)
        self.to_daily_but = tk.Button(self.toolbar, text = 'Add to daily', font = 'Arial 14', command = self.add_to_daily)
        self.read_but = tk.Button(self.toolbar, text = 'Read', font = 'Arial 14', command = self.read)
        self.add_but.place(rely = 0.5, relx = 0.1, anchor = tk.CENTER, width = 110)
        self.delete_but.place(rely = 0.5, relx = 0.3, anchor = tk.CENTER, width = 110)
        self.to_daily_but.place(rely = 0.5, relx = 0.5, anchor = tk.CENTER, width = 110)
        self.read_but.place(rely = 0.5, relx = 0.7, anchor = tk.CENTER, width = 110)
        
    
    
        
    def delete(self):
        idis = self.return_id()
        if idis == False:
            return False
        string = 'DELETE FROM {0} WHERE id'.format(self.workingtable)
        if isinstance(idis, str):
            string += ' = \"{0}\"'.format(idis)
        else:
            pos = 0
            string += ' in ('
            for i in idis:
                pos+=1
                string += '\"{0}\"'.format(i)
                if pos!=len(idis):
                    string += ', '
                else:
                    string += ')'
        self.tasks.send(string)
        
       
    
    def add_to_daily(self):
        '''adds to daily-list'''
        idis = self.return_id()
        if idis == False:
            return False
        string = 'UPDATE {0} SET status="daily" WHERE id in ('.format(self.workingtable)
        pos = 0
        if isinstance(idis, str):
            string = 'UPDATE {0} SET status="daily" WHERE id = "{1}"'.format(self.workingtable, idis)
        else:
            for i in idis:
                pos+=1
                string += '\"{0}\"'.format(i)
                if pos!=len(idis):
                    string += ', '
                else:
                    string += ')'
        self.tasks.send(string)
    
    
    def return_id(self):
        if len(self.maintree.selection()) == 0:
            messagebox.showerror('Error','Select 1 task at least')
            return False
        elif len(self.maintree.selection()) == 1:
            return self.maintree.set(self.maintree.selection()[0], '#1')
        else:
            arr = []
            for i in self.maintree.selection():
                arr.append(self.maintree.set(i, '#1'))
            return(arr)
        
    def add(self, status = 'waits'):
        Dialog(status)
        
        
    def load_and_show_db(self):
        array = self.tasks.get_all()
        self.maintree.delete(*self.maintree.get_children())
        for everylist in array:
            self.maintree.insert('','end',values = everylist)
        self.maintree.after(5000, self.load_and_show_db)
        
        
        
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
    def put(self):
        global q
        header = self.hd.get()
        body = self.entry2.get(1.0, tk.END)
        DataBase().add(header, body, self.status)
        #q.load_and_show_db()
        self.destroy()
        
    def __init__(self, status = 'waits'):
        self.status = status
        super().__init__(root)
        self.title('Add new task')
        self.geometry('370x350')
        self.resizable(False, False)
        
        label1 = tk.Label(self, text = 'Header:', font = 'Arial 12')
        label1.place(x = 20, y = 20)
        label2 = tk.Label(self, text = 'Body:', font = 'Arial 12')
        label2.place(x = 20, y = 50)
        
        
        self.hd = tk.StringVar()
        entry1 = tk.Entry(self, font = 'Arial 12', textvariable=self.hd)
        entry1.place(x = 100, y = 20)
        

        #self.bd = tk.StringVar()        
        self.entry2 = tk.Text(self, height = 10, width = 20, font = 'Arial 12')
        self.entry2.place(x = 100, y = 50)
        
        add_but = tk.Button(self, text = "Add", font = 'Arial 12', command = self.put)
        add_but.place(relx = 0.5, rely = 0.83, anchor = tk.CENTER)
        
        
        
        self.grab_set()
        self.focus_set()  
        
    
class Daily_window(Windowa):
    def __init__(self, mw):
        global root
        self.workingtable = 'tasks'
        root.quit()
        self.tasks = DataBase()
        
        self.mainwindow = mw
        self.mainwindow.title('Daily Manager')
        self.mainwindow.geometry('600x500')
        
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
        self.show_daily()
        
        self.add_but = tk.Button(self.toolbar, text = 'Add', font = 'Arial 14', command = self.do_add)###
        self.delete_but = tk.Button(self.toolbar, text = 'Delete', font = 'Arial 14', command = self.delete)
        self.to_daily_but = tk.Button(self.toolbar, text = 'Flag as did', font = 'Arial 14', command = self.done)#add_to_daily
        self.read_but = tk.Button(self.toolbar, text = 'Read', font = 'Arial 14', command = self.read)
        self.add_but.place(rely = 0.5, relx = 0.1, anchor = tk.CENTER, width = 110)
        self.delete_but.place(rely = 0.5, relx = 0.3, anchor = tk.CENTER, width = 110)
        self.to_daily_but.place(rely = 0.5, relx = 0.5, anchor = tk.CENTER, width = 110)
        self.read_but.place(rely = 0.5, relx = 0.7, anchor = tk.CENTER, width = 110)
        
    def show_daily(self):
        array = self.tasks.get_daily()
        self.maintree.delete(*self.maintree.get_children())
        for everylist in array:
            self.maintree.insert('','end',values = everylist)
        self.maintree.after(5000, self.show_daily)
            
    def do_add(self):
        self.add('daily')  
            
    def done(self):
        '''adds to daily-list'''
        idis = self.return_id()
        if idis == False:
            return False
        string = 'UPDATE {0} SET status="done!" WHERE id in ('.format(self.workingtable)
        pos = 0
        if isinstance(idis, str):
            string = 'UPDATE {0} SET status="done!" WHERE id = "{1}"'.format(self.workingtable, idis)
        else:
            for i in idis:
                pos+=1
                string += '\"{0}\"'.format(i)
                if pos!=len(idis):
                    string += ', '
                else:
                    string += ')'
        self.tasks.send(string)       
    
        

if __name__ == '__main__':

    root = tk.Tk()    
    q = Windowa(root)
    root.mainloop()
    