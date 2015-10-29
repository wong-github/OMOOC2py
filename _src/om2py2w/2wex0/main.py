# -*- coding: utf-8 -*-
#!/usr/bin/env python

_author_ = 'Wills Wong'

"""
----------------------------------------Version 3.0--------------------------- --------------
极简交互式日记系统（桌面版） V3.0
该版本在2.0的基础上进行修改,将2.0版本中的按键控制改为下拉菜单控制,同时加入垂直滚动条,并优化了界面
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

    #创建Text控件，Scrollbar控件以及带下拉菜单的Menu控件
    test = Text(root)

    menubar = Menu(root)
    fmenu = Menu(menubar,tearoff = 0)
    amenu = Menu(menubar,tearoff = 0)

    slr = Scrollbar(root)

    #将Text与Scrollbar的位置变化关联起来
    test.config(yscrollcommand = slr.set)
    slr.config(command = test.yview)

    #定义按键“新日记”的事件处理函数
    def new():
        root.title('正在编辑新日记')
        test.delete(1.0,END)

    #定义按键“退出”的事件处理函数
    def quit():
        #“退出”按键按下时，自动保存输入内容，同时添加文本保存时间
        with open(filePath,'a') as f:
            f.write('\n' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n' + test.get(local,END))
        root.destroy()

    #定义按键“日记历史”的时间处理函数
    def history():
        #首次输入检测
        if os.path.exists(filePath) == True:
            with open(filePath,'r') as f:
                testshow = f.read()
            #在新窗口中显示日记历史内容，Text和Scrollbar控件的实例化与配置跟主窗口的类似
            tl = Toplevel()
            tl.title('我的日记历史')
            Label(tl, text = '*** Hi 这是您以前的日记 ***', fg = 'red').pack(side = TOP, fill = X)
            test_tl = Text(tl)
            slr_tl = Scrollbar(tl)
            test_tl.config(yscrollcommand = slr_tl.set)
            slr_tl.config(command = test_tl.yview)
            test_tl.insert(1.0,testshow)
            test_tl.pack(side = LEFT, fill = Y)
            slr_tl.pack(side = LEFT, fill = Y)
        else:
            #首次使用软件的用户没有日记历史文件，按下该按键会弹出提示窗口
            tkMessageBox.showinfo('Error','Sorry，您还没有写过日记呢！赶紧行动起来吧！')
    
    #定义按键“关于”的事件处理函数
    def about():
        #显示软件信息
        tkMessageBox.showinfo('关于该软件的信息','Author: Wills Wong\nVersion: 2.0')

    #定义菜单栏的主菜单及相应的下拉菜单   
    menubar.add_cascade(label = '文件', menu = fmenu)
    menubar.add_cascade(label = '关于', menu = amenu)
    fmenu.add_command(label = '新日记', command = new)
    fmenu.add_command(label = '日记历史', command = history)
    fmenu.add_command(label = '退出', command = quit)
    amenu.add_command(label = '软件信息', command = about)
       
    #获取新内容的起始光标位置
    local = test.index(CURRENT)

    #将Text，Scrollbar和Menu加入到布局，最后进入消息循环
    test.pack(side = LEFT, fill = Y)
    slr.pack(side = RIGHT, fill = Y)
    root['menu'] = menubar
    root.mainloop()

#自检区，判断脚本直接被运行 or 作为模块调用
if __name__ == '__main__':
    main()
