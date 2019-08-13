#Task Manager backend
#coding: utf-8

class Task:
    def __init__(self, header, body, status):
        self.header, self.body, self.status = header, body, status
    
    def add(self):
        pass
    #add it into 
    def switch_status(self, end_status):
        self.status = end_status
        #update sql
