# -*- coding: utf-8 -*-
#!/usr/bin/env python

_author_ = 'Wills Wong'

'''
--------------------------------Version 1.0-------------------------------------
极简交互式笔记（web版），支持浏览器访问，同时兼容 3w 的 Net 版本的命令行界面进行交互
'''

from bottle import *
import os,time

def main():

    savePath = '/home/wong/slog/diary.txt'
    tempPath = '/home/wong/slog/temp.txt' 

    #用浏览器访问http://localhost:8080/read,在浏览器端输出历史日记内容
    @route('/read')
    def read():
        if os.path.exists(tempPath) == True:
            os.remove(r'/home/wong/slog/temp.txt')
        if os.path.exists(savePath) == True:      
            with open(savePath,'r') as f:
                return '''
                <html>
                <head>
                <title>您的日记历史</title>
                </head>
                <body>
                <a href = "http://localhost:8080/">新日记</a>
                <p> %s </p>
                </body>
                </html>
                ''' % (f.read()).replace('\n', '<br />')
        else:
            return '''<p>啊哈～您还没写过日记哦！赶紧动手把</p>'''

    #用浏览器访问http://localhost:8080，在浏览器端可进行新日记编辑和提交
    @route('/', method = 'GET')
    def input_one_line():
        return '''
        <html>
        <head>
        <title>您的新日记</title>
        </head>
        <body>
        <form method="POST" action="/">
        Current Line:
        <input name="content" type="text" />
        <input type="submit" />
        </form>
        <a href = "http://localhost:8080/read">日记历史</a>
        </body>
        </html>
        '''

    @route('/', method='POST')
    def submit_one_line():
        saveLine = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n' + request.forms.get('content') + '\n'
        with open(savePath, 'a') as f:
            f.write(saveLine)
        with open(tempPath, 'a') as f:
            f.write(saveLine)
        with open(tempPath, 'r') as f:
            return '''
            <html>
            <head>
            <title>您的新日记</title>
            </head>
            <body>
            <form method="POST" action="/">
            Current Line:
            <input name="content" type="text" />
            <input type="submit" />
            </form>
            <a href = "http://localhost:8080/read">日记历史</a>
            <p> %s </p>
            </body>
            </html>
            ''' % (f.read()).replace('\n', '<br />')

    #保存命令行界面提交的新日记信息
    @route('/save', method = 'POST')
    def save():
        saveLine = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n' + request.POST.get('newline') + '\n'
        with open(savePath, 'a') as f:
            f.write(saveLine)

    #向命令行界面打印历史日记信息
    @route('/readcli')
    def readcli():
        if os.path.exists(savePath) == True:      
            with open(savePath,'r') as f:
                return '%s' % f.read()
        else:
            return '啊哈～您还没写过日记哦！赶紧动手把'


    run(host='localhost',port=8080,debug=True)

#自检区，判断脚本直接被运行 or 作为模块调用
if __name__ == '__main__':
    main()

