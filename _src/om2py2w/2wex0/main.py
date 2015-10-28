# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
------------------------Version 2.0-------------------------
该版本在1.0的基础上，增加了功能按键，通过不同的功能按键实现相应
的功能
"""

#全局引用
from Tkinter import *
import os,sys,time,tkMessageBox

def main():
    
    #全局变量
    local = ''
    filePath = '/home/wong/test.txt'

    #加载sys后，setdefaultencoding方法会被删除，所以需要重新加载
    #（reload）sys才能调用setdefaultencoding方法，重新设置系统编码
    reload(sys)
    sys.setdefaultencoding( "utf-8" )

    #初始化Tk，并设置窗口标题为“我的日记本”
    root = Tk()
    root.title('我的日记本')

    #创建Text控件
    test = Text(root)
    
    #创建两个关于颜色的文本属性tag，红色用于系统提示语，蓝色用于历史日志输出
    test.tag_config('red',foreground = 'red')
    test.tag_config('blue',foreground = 'blue')

    #定义按键“退出”的事件处理函数
    def quit():
        with open(filePath,'a') as f:
            f.write('\n' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n' + test.get(local,END))
        root.destroy()

    #定义按键“日记历史”的时间处理函数
    def history():
        if os.path.exists(filePath) == True:
            with open(filePath,'r') as f:
                testshow = '*** Hi 这是您以前的日记 ***\n' + f.read()
            tl = Toplevel()
            tl.title('您的日记历史')
            test_tl = Text(tl)
            test_tl.insert(1.0,testshow)
            test_tl.pack()
        else:
            tkMessageBox.showinfo('Error','Sorry，您还没有写过日记呢！赶紧行动起来吧！')

    #定义按键“新日记”的事件处理函数
    def new():
        test.delete(1.0,END)
        test.insert(CURRENT, '现在您可以开始写新日记啦', 'red')
    
    #定义按键“关于”的事件处理函数
    def about():
        tkMessageBox.showinfo('关于该软件的信息','Author: Wills Wong\nVersion: 2.0')
    
    #创建Button控件
    Button(root, text = '退出', relief = GROOVE, fg = 'red', command = quit).pack(fill=X)
    Button(root, text = '日记历史', relief = GROOVE, fg = 'red', command = history).pack(fill=X)
    Button(root, text = '新日记', relief = GROOVE, fg = 'red', command = new).pack(fill=X)
    Button(root, text = '关于', relief = GROOVE, fg = 'red', command = about).pack(fill=X)

    #获取新内容的起始光标位置
    local = test.index(CURRENT)

    #将test加入到布局，最后进入消息循环
    test.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
