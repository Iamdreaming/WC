"""学习测试"""

import re 

path = 'test1.c'
#检查readlines()函数用法
def test1():
    
    fb = open(path,'r')
    words = fb.read()
        
    words = words.replace(' ','')
    words = words.replace('\n','')
    print("字符数为"+str(len(words)))

test1()
def words_count():
    file_onject = open(path,'r')
    context = file_onject.read()
    words = context.split()
    print('单词个数为'+ str(len(words)))
words_count()
def lines_count():
    file_object = open(path,'r')
    count = 0
    for line in file_object.readlines():
        count += 1
    print('行数为'+ str(count))
lines_count()