import os
import re
import tkinter
from tkinter import ttk
from tkinter import filedialog

class text_count():

    def __init__(self, path):
        self.path = path

    def char_count(self):
        # 统计字符数 -c
        file_object = open(self.path, 'r',encoding= 'utf-8')
        context = file_object.read()
        context = context.replace(' ', '')
        context = context.replace('\n', '')
        string = "字符数为"+str(len(context))
        print(string)
        return string

    def words_count(self):
        # 统计单词数 -w
        file_object = open(self.path, 'r', encoding='UTF-8')
        context = file_object.read()
        words = context.split()
        string = '单词个数为' + str(len(words))
        print(string)
        return string

    def lines_count(self):
        # 统计行数 -l
        file_object = open(self.path, 'r', encoding='UTF-8')
        count = 0
        for line in file_object.readlines():
            count += 1
        string = '行数为' + str(count)
        print(string)
        return string
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
            elif flag:
                count[1] += 1
                if r'*/' in line:
                    flag = False
            else:
                count[2] += 1
        string1 = '空行数为' + str(count[0])
        string2 = '注释行数为' + str(count[1])
        string3 = '代码行数为' + str(count[2])
        string_all = [string1,string2,string3]
        
        print(string1)
        print(string2)
        print(string3)
        return string_all


class infor_windows(tkinter.Frame):
    def __init__(self, master):
        frame1 = tkinter.Frame(master)
        frame2 = tkinter.Frame(master)
        order_frame = tkinter.Frame(master)
        frame1.grid(row = 0, column = 5)
        frame2.grid(row = 4, column = 5)
        order_frame.grid(row = 4, column = 12)
        self.name = tkinter.Variable()
        self.entry = tkinter.Entry(frame1,textvariable = self.name)
        self.entry.pack(side = 'left')
        self.text = tkinter.Text(frame2, width = 40 ,height = 20)        
        self.button1 = tkinter.Button(frame1,text = '选择',command = self.open_file)       
        self.button1.pack(side = 'right')       
        self.text.pack()

        self.c_button = tkinter.Button(order_frame,text = 'c命令',command = self.order_c)
        self.get_c = tkinter.Variable()
        self.show_c = tkinter.Entry(order_frame,textvariable = self.get_c)
        self.c_button.pack()
        self.show_c.pack()

        self.w_button = tkinter.Button(order_frame,text = 'w命令',command = self.order_w)
        self.get_w = tkinter.Variable()
        self.show_w = tkinter.Entry(order_frame,textvariable = self.get_w)
        self.w_button.pack()
        self.show_w.pack()

        self.l_button = tkinter.Button(order_frame,text = 'l命令',command = self.order_l)
        self.get_l = tkinter.Variable()
        self.show_l = tkinter.Entry(order_frame,textvariable = self.get_l)
        self.l_button.pack()
        self.show_l.pack()

        self.a_button = tkinter.Button(order_frame,text = 'a命令',command = self.order_a)
        self.show_a = tkinter.Text(order_frame,width = 20,height = 3)
        self.a_button.pack()
        self.show_a.pack()

    def order_c(self):
        count_c = text_count(self.file_name)
        self.get_c.set(count_c.char_count())

    def order_w(self):
        count_w = text_count(self.file_name)
        self.get_w.set(count_w.words_count())

    def order_l(self):
        count_l = text_count(self.file_name)
        count_l.char_count()
        self.get_l.set(count_l.lines_count())

    def order_a(self):
        count_a = text_count(self.file_name)
        strings = count_a.more_information()
        for string in strings:
            self.show_a.insert('insert',string + '\n')
        



    def open_file(self):
        self.name.set('')
        self.get_c.set('')
        self.get_w.set('')
        self.get_l.set('')
        self.show_a.delete('1.0','end')
        self.text.delete('1.0','end')
        self.file_name = filedialog.askopenfilename()
        self.name.set(self.file_name.split(r'/')[-1])  
        file = open(self.file_name,'r',encoding= 'utf-8')
        for line in file.readlines():
            self.text.insert('insert',line)


def handle_files(father_path, all_files, all_path, word):
    # 递归返回目录下符合条件的文件路径。-s

    reg = re.compile(word)
    file_list = os.listdir(father_path)
    for file in file_list:
        cur_path = os.path.join(father_path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            handle_files(cur_path, all_files, all_path, word)
        elif os.path.isfile(cur_path):
            if reg.search(file) != None:
                all_path.append(cur_path)
                all_files.append(file)




class Order():

    
    def base_orders(self,w_c,words):
        # 处理命令
        if '-c' in words:
            w_c.char_count()
        if '-w' in words:
            w_c.words_count()
        if '-l' in words:
            w_c.lines_count()
        if '-a' in words:
            w_c.more_information()
        
    def senior_orders(self,words):
        # 处理-s命令
        
        if '-s' in words:
            i = 0
            all_files = []
            all_path = []
            word = words[-1]
            word = word.replace('*', '.*')
            word = word.replace('?', '.?')
            father_path = os.path.split(os.path.abspath('wc.py'))[0]
            handle_files(father_path, all_files, all_path, word)
            for file in all_files:
                print(file + ':')
                w_c = text_count(all_path[i])
                self.base_orders(w_c,words)
                print()
                i += 1
        else:
            self.w_c = text_count(words[-1])
            self.base_orders(self.w_c, words)
            print()

    def gui_order(self,words):
        if '-x' in words:
            win = tkinter.Tk()
            win.title('可视化文件夹遍历')
            win.geometry('600x400')
            inwindow = infor_windows(win)
            win.mainloop()
        else :
            self.senior_orders(words)


def main():
    """主函数"""
    # 存储参数
    words = input("请输入命令和文件路径:").split()
    order = Order()
    order.gui_order(words)


if __name__ == "__main__":
    main()
