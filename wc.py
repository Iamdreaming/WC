import os
import re 

class world_count():
    
    def __init__(self,order,path):
        self.order = order
        self.path = path
    
    def char_count(self):
        #读取字符数
        file_object = open(self.path,'r')
        context = file_object.read()
        context = context.replace(' ','')
        context = context.replace('\n','')
        print("字符数为"+str(len(words)))


    def words_count(self):
        file_onject = open(self.path,'r')
        context = file_onject.read()
        words = context.split()
        print('单词个数为'+ str(len(words)))

    def lines_count(self):
        file_object = open(self.path,'r')
        count = 0
        for line in file_object.readlines():
            count += 1
        print('行数为'+ str(count))
        




