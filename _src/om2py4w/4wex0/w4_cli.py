# -*- coding: utf-8 -*-
#!/usr/bin/env python

_author_ = 'Wills Wong'

'''
----------Version 1.0-------------------
极简交互式笔记（web版）的命令行界面进行交互
'''

import os,requests

def main():
     
    print '\nNow you can start writing:\n'
    print 'PS: When you complete writing, please hit "Q" or "q" ! Hit "R" or "r" can print your history diary.\n'

    line = 0
    saveurl = 'http://localhost:8080/save'
    readurl = 'http://localhost:8080/readcli'

    while True:
        try:        
            line_num = 'Line %d :' % line
            a = raw_input(line_num)
            if a == 'Q' or a == 'q':		
                print '\n\nThanks for using. Goodbye! ^_^\n'
                break
            if a == 'R' or a == 'r': 
                s = requests.get(readurl)
                print '\n' + s.text +'\n'
                line -= 1
            else: 
                requests.post(saveurl, data = {'newline':a})
             
            line += 1
        except KeyboardInterrupt:
            print '\n\nError! You can not hit "Ctrl-C" when you writing, it will interupt input and the current line will lose!\n'
            break

#自检区，判断脚本直接被运行 or 作为模块调用
if __name__ == '__main__':
    main()

