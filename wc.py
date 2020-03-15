import os

class world_count():
    
    def __init__(self,path):
        self.path = path
    
    def char_count(self):
        #读取字符数
        file_object = open(self.path,'r')
        context = file_object.read()
        context = context.replace(' ','')
        context = context.replace('\n','')
        print("字符数为"+str(len(context)))


    def words_count(self):
        file_object = open(self.path,'r')
        context = file_object.read()
        words = context.split()
        print('单词个数为'+ str(len(words)))

    def lines_count(self):
        file_object = open(self.path,'r')
        count = 0
        for line in file_object.readlines():
            count += 1
        print('行数为'+ str(count))


def main():
    words = input("请输入命令和文件路径:").split()
    w_c = world_count(words[1])
    if words[0] == '-c':
        w_c.char_count()
    elif words[0] == '-w':
        w_c.words_count()
    elif words[0] == '-l':
        w_c.lines_count()
    else :
        print("输入有误")

if __name__ == "__main__":
    main()




