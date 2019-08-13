#Task Manager backend
#coding: utf-8
import sqlite3


class Task:
    def __init__(self, header, body, status):
        self.header, self.body, self.status = header, body, status
    
    def add(self):
        pass
    #add it into 
    def switch_status(self, end_status):
        self.status = end_status
        #update sql

class DataBase:
    
    
    def __init__(self, name = 'mydb.db'):
        
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        
    def createtable(self, name = 'tasks'):
        try:
            self.cursor.execute('''CREATE TABLE {0} (id int primary key, header varchar, body text, status varchar)'''.format(name))
        except sqlite3.OperationalError:
            pass
    
    def add(self, header, body, status, table = 'tasks',):
        self.cursor.execute('''SELECT * FROM {0} ORDER BY id DESC'''.format(table))
        self.cursor.execute('''INSERT INTO {0} (id, header, body, status) VALUES (?, ?, ?, ?)'''.format(table), (self.cursor.fetchone()[0]+1, header, body, status))
        self.conn.commit() 
    
    def get(self, id_, table = 'tasks'):
        strs = '''SELECT * FROM {0} WHERE id = {1} '''.format(table, id_)
        print(strs)
        listt = self.cursor.execute(strs)
        for i in listt:
            quit = i
        return quit
    
        
    def dbclose(self):
        self.cursor.close()        
        self.conn.close()


q = DataBase('olddb.db')
q.createtable()
q.add(1, 'of', 'aq')
q.add(2, 'of', 'aq')
q.get(1)
q.dbclose()