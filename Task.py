#Task Manager backend
#coding: utf-8
import sqlite3


class Task:
    def __init__(self, header, body, status):
        self.header, self.body, self.status = header, body, status
    
    def add(self):
        pass
   

class DataBase:
    
    
    def __init__(self, table = 'tasks', name = 'mydb.db'):
        self.name = name
        self.table = table
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        
    def change_table(self, new_name):
        self.table = new_name
        try:
            self.cursor.execute('''CREATE TABLE {0} (id int primary key, header varchar, body text, status varchar)'''.format(self.table))
        except sqlite3.OperationalError:
            pass        
        
    def createtable(self):
        try:
            self.cursor.execute('''CREATE TABLE {0} (id int primary key, header varchar, body text, status varchar)'''.format(self.table))
        except sqlite3.OperationalError:
            pass
    
    def add(self, header, body, status):
        self.cursor.execute('''SELECT id FROM {0} ORDER BY id DESC'''.format(self.table))
        #print('q')
        #print(self.cursor.fetchone())
        try:
            quit = self.cursor.fetchone()[0]
        except TypeError:
            quit = -1
            
        self.cursor.execute('''INSERT INTO {0} (id, header, body, status) VALUES (?, ?, ?, ?)'''.format(self.table), (quit+1, header, body, status))
        self.conn.commit()
        
    def switch_status(self, id_, end_status):
        self.status = end_status
        sqlrequest = '''UPDATE {0} SET status = '{1}' WHERE id = {2}'''.format(self.table, end_status, id_)
        #print(sqlrequest)
        self.cursor.execute(sqlrequest)
        self.conn.commit()
    
    def get(self, id_):
        strs = '''SELECT * FROM {0} WHERE id = {1} '''.format(self.table, id_)
        listt = self.cursor.execute(strs)
        for i in listt:
            quit = i
        return quit
    
    def get_all(self):
        strs = '''SELECT * FROM {0} ORDER BY id'''.format(self.table)
        return self.cursor.execute(strs)
    
    def get_daily(self):
        strs = '''SELECT * FROM {0} WHERE status = "daily" ORDER BY id'''.format(self.table)
        return self.cursor.execute(strs)    
    
    def send(self, string):
        self.cursor.execute(string)
        self.conn.commit()
    
        #UPDATE tablename SET pole1="message" WHERE id="1" and id="15";    
        
    
        
    def dbclose(self):
        self.cursor.close()        
        self.conn.close()


#q = DataBase('olddb.db')
#q.createtable()
#q.add(1, 'of', 'aq')
#q.add(2, 'of', 'aq')
#q.switch_status(2,'switched')
#q.dbclose()