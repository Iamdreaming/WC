import os
import re 

class world_count():
    
    def __init__(self,order,path):
        self.order = order
        self.path = path
    
    def char_count(self):
        #读取字符数
        file_object = open(self.path,'r')
        words = ''
        for line in file_object.readlines():
            words += line
        words = words.replace(' ','')
        words = words.replace('\n','')
        print("字符数为"+str(len(words)))


    def words_count(self):
        file_onject = open(self.path,'r')
        




