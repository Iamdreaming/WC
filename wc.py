import os
import tkinter
import re 

class text_count():

    def __init__(self, path):
        self.path = path

    def char_count(self):
        # 统计字符数 -c
        context = ''
        file_object = open(self.path, 'r', encoding='UTF-8')
        context = file_object.read()
        context = context.replace(' ', '')
        context = context.replace('\n', '')
        print("字符数为"+str(len(context)))

    def words_count(self):
        # 统计单词数 -w
        file_object = open(self.path, 'r', encoding='UTF-8')
        context = file_object.read()
        words = context.split()
        print('单词个数为' + str(len(words)))

    def lines_count(self):
        # 统计行数 -l
        file_object = open(self.path, 'r', encoding='UTF-8')
        count = 0
        for line in file_object.readlines():
            count += 1
        print('行数为' + str(count))

    def more_information(self):
        # 返回更复杂的数据（代码行 / 空行 / 注释行） -a
        file_object = open(self.path, 'r', encoding='UTF-8')
        count = [0, 0, 0]
        flag = False  # 用于判断/*
        for line in file_object.readlines():
            if len(line) <= 1:
                count[0] += 1
            elif r'//' in line:
                count[1] += 1
            elif r'/*' in line:
                flag = True
                count[1] += 1
            elif flag :
                count[1] += 1
                if r'*/' in line:
                    flag = False
            else:
                count[2] += 1
        print('空行数为' + str(count[0]))
        print('注释行数为' + str(count[1]))
        print('代码行数为' + str(count[2]))
        


def handle_files(father_path, all_files, all_path,word):
    # 递归返回目录下符合条件的文件路径。-s
    
    reg = re.compile(word)
    file_list = os.listdir(father_path)
    for file in file_list:
        cur_path = os.path.join(father_path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            handle_files(cur_path, all_files, all_path,word)
        elif os.path.isfile(cur_path):
            if reg.search(file) != None :
                all_path.append(cur_path)
                all_files.append(file)


def base_orders(w_c, words):
    # 处理命令
    if '-c' in words:
        w_c.char_count()
    if '-w' in words:
        w_c.words_count()
    if '-l' in words:
        w_c.lines_count()
    if '-a' in words:
        w_c.more_information()


def more_orders(words):
    # 处理-s,-x命令
    if '-x' in words:
        pass
    elif '-s' in words:
        i = 0
        all_files = []
        all_path = []
        word = words[-1]
        word = word.replace('*','.*')
        word = word.replace('?','.?')
        father_path = os.path.split(os.path.abspath('wc.py'))[0]
        handle_files(father_path, all_files, all_path,word)
        for file in all_files:
            if os.path.splitext(file)[-1] == os.path.splitext(words[-1])[-1]:
                print(file + ':')
                w_c = text_count(all_path[i])
                base_orders(w_c, words)
                print()
            i += 1
    else:
        w_c = text_count(words[-1])
        base_orders(w_c, words)
        print()


def main():
    """主函数"""
    # 存储参数
    words = input("请输入命令和文件路径:").split()
    
    more_orders(words)


if __name__ == "__main__":
    main()
