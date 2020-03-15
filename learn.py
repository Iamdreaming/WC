"""学习测试"""

import re 

#检查readlines()函数用法
def test1():
    file_path = 'test3.c'
    fb = open(file_path,'r')
    words = fb.read()
        
    words = words.replace(' ','')
    words = words.replace('\n','')
    print("字符数为"+str(len(words)))

test1()