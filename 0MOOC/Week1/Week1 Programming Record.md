#极简交互式本地日记系统编程记录
##需求
+ 一次接收输入一行日记
+ 保存为本地文件
+ 再次运行系统时,能打印出过往的所有日记

##关键点
+ python脚本的调用，外部数据输入（包括中文数据），持续交互与终止，文件操作

##整体流程框图
 ![W1 liuchengtu](W1 liuchengtu.png)

##代码

        # -*- coding: utf-8 -*-
        #!/usr/bin/env python

        _author_ = 'Wills Wong'

        import os

        if os.path.exists('/home/wong/test.txt') == True:
            print '\n*** Here is your writting record ***\n\n'
            with open('/home/wong/test.txt','r') as f:
                print f.read()
                
        print '\nNow you can start writing:\n'
        print 'PS: When you complete writing, please hit "Q" or "q" !\n'

        line = 0

        while True:
            try:
                line_num = 'Line %d :' % line
                a = raw_input(line_num) + '\n'
                if a == 'Q\n' or a == 'q\n':		
                    print '\n\nThanks for using. Goodbye! ^_^\n'
                    break
                with open('/home/wong/test.txt','a') as f:
                    f.write(a)
                line += 1
            except KeyboardInterrupt:
                print '\n\nError! You can not hit "Ctrl-C" when you writing, it will interupt input and the current line will lose!\n'
                break


##相关流程的代码实现
* 首次输入检测
 + 系统需求中提到，当系统再次运行时，需要打印出过往的所有日记。由此引发了一个问题：对于首次使用系统的用户来说，本地并无日志记录，这种情况下应该不执行历史日志的输出。因此需要甄别用户是否首次使用该系统。
 + 要解决首次输入检测问题，可以通过检测日志文件是否存在来实现，os模块中的exists方法正好能实现这一功能，相关代码如下:
```
        if os.path.exists('/home/wong/test.txt') == True:
            print '\n*** Here is your writting record ***\n\n'
            with open('/home/wong/test.txt','r') as f:
                print f.read()
 ```
* 外部数据输入 & 持续交互与终止
 + 本系统需要从外部输入数据，并且是一行一行地接收，同时考虑到中文数据的输入和输出，用*raw_input()*函数比较合适（PS：*raw_input()*和*input()*的区别）。另外，为了实现持续交互，*raw_input()*函数应当在停止交互信号出现前，不断循环调用
 + 通过调用*raw_input()*函数实现数据输入，同时在写入日志记录文件之前，对所输入的数据进行判断，若发现输入结束信号，交互立刻终止，相关的循环体如下：
```
        line_num = 'Line %d :' % line
        a = raw_input(line_num) + '\n'
        if a == 'Q\n' or a == 'q\n':		
            print '\n\nThanks for using. Goodbye! ^_^\n'
            break
        with open('/home/wong/test.txt','a') as f:
            f.write(a)
        line += 1
```
* 异常处理
 + 在系统的使用过程中，应该考虑两个可能会出现的异常情况：文件操作过程中出现异常，导致文件数据丢失；误触发键盘中断信号（PS:同时按下Ctrl-C）而退出系统。
 + 对于文件操作方面的异常，在打开文件时可以使用__'with fileFunction() as fileName:'__语句，该语句在异常产生时也可以关闭文件，从而减少文件数据内容丢失的风险。
 + 对于误触发键盘中断信号的情况，可以在交互循环体中加入__try...except...__语句块，在except后加入键盘中断的异常处理代码。

##待完善地方
* 系统暂时不能显示时间，因为代码中没添加时间处理方面的模块。（PS：开智罪）这点将在week 2中完善。
* 系统在开始运行时需要显示历史输入（首次使用系统除外），若历史数据比较庞大（1G？），全部一次性读取这一操作并不恰当。因此历史回放功能应该让用户具有可选性（比如按日期选择要显示的历史日志）。

##所用到的主要知识点
* os模块检测文件存在的方法：os.path.exists（'filePath'）
* 文件的操作：open()、close()、read()、wrtie(content)；文件的操作模式：'r'写模式、'w'写模式、'a'追加模式、'b'二进制模式、'+'读/写模式
* 带异常处理机制的文件操作方式：with fileFunction() as fileName:；异常处理语句try...except，本次任务设计到KeyboardInterrupt异常处理
* 从外部获取输入的方法：raw_input()，该函数若在括号内添加内容，则还可带提示语


