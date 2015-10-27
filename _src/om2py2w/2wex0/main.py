# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
------------------------Version 1.0-------------------------
此脚本是桌面版极简交互式日记系统的原始版本，能实现基本功能。用户
在运行该脚本后，能窗口中输入日记内容，并保存为本地文件。同时，对
于非首次使用用户，脚本运行后还能在窗口中输出所有历史日记内容。
"""

#全局引用
from Tkinter import *
import os,sys

def main():
    
    #全局变量
    local = ''

    #加载sys后，setdefaultencoding方法会被删除，所以需要重新加载
    #（reload）sys才能调用setdefaultencoding方法，重新设置系统编码
    reload(sys)
    sys.setdefaultencoding( "utf-8" )

    #初始化Tk，并设置窗口标题为“My Diary”
    root = Tk()
    root.title('My Diary')

    #定义按键“Save”的事件处理函数：点击按键后保存所输入的全部内容
    def saveText():
        with open('/home/wong/test.txt','a') as f:
            f.write(test.get(local,END))

    #创建一个Text控件和Button控件
    test = Text(root)
    buttons = Button(root, text = 'Save', command = saveText)

    #创建两个关于颜色的文本属性tag，红色用于系统提示语，蓝色用于历史日志输出
    test.tag_config('red',foreground = 'red')
    test.tag_config('blue',foreground = 'blue')

    #首次输入检测，否则打印历史日志
    if os.path.exists('/home/wong/test.txt') == True:
        test.insert(1.0,'*** Here is your writting record ***\n','red')
        with open('/home/wong/test.txt','r') as f:
            test.insert(CURRENT, f.read() + '\n', 'blue')

    test.insert(CURRENT, 'Now you can start writing:', 'red')

    #获取新内容的起始光标位置
    local = test.index(CURRENT)

    #将buttons和test加入到root并布局，最后进入消息循环
    buttons.pack()
    test.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
