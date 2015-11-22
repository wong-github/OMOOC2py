# -*- coding: utf-8 -*-
#!/usr/bin/env python

_author_ = 'Wills Wong'

'''
------Version 1.0-------
极简交互式笔记（PaaS版）
'''

from bottle import *
from sae.storage import Bucket
import os, time, sae#,sae.kvdb

app = Bottle()

bucket = Bucket('t')
bucket.put()
bucket.post(acl = '.r:.sinaapp.com,.r:sae.sina.com.cn')

@app.route('/')
def init():
    return'''
    <title>欢迎</title>
    <style>
    h1 
    {
        color: #333333;
        font-size: 48px;
        text-shadow: 3px 3px 3px #666666;
    }
    </style>
    <h1>Welcome!</h1>
    <meta http-equiv="refresh" content="2;url=http://diaryweb.sinaapp.com/write">
    '''

#用浏览器访问http://diaryweb.sinaapp.com/read,在浏览器端输出历史日记内容
@app.route('/read')
def read():      
    return '''
    <html>
    <head>
    <title>您的日记历史</title>
    </head>
    <body>
    <a href = "http://diaryweb.sinaapp.com/write">新日记</a>
    <h1>您的日记历史：</h1>
    <p> %s </p>
    </body>
    </html>
    ''' % (bucket.get_object_contents('mydiary.txt')).replace('\n', '<br />')

#用浏览器访问http://diaryweb.sinaapp.com/write，在浏览器端可进行新日记编辑和提交
@app.route('/write', method = 'GET')
def input_one_line():
    return '''
    <html>
    <head>
    <title>您的新日记</title>
    </head>
    <body>
    <form method="POST" action="/write">
    <fieldset>
    <legend>慢慢来～一行一行地写 ^_^</legend>
    <input name="content" type="text" style="width:1200px;height:30px" />
    <input type="submit" value="上传" style="height:30px;position:absolute;+margin-top:2px" />
    </fieldset>
    </form>
    <a href = "http://diaryweb.sinaapp.com/read">日记历史</a>
    </body>
    </html>
    '''

@app.route('/write', method='POST')
def submit_one_line():
    saveLine = bucket.get_object_contents('mydiary.txt') + '\n' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n' + request.forms.get('content') + '\n'  
    bucket.put_object('mydiary.txt', saveLine)
    return '''
    <html>
    <head>
    <title>您的新日记</title>
    </head>
    <body>
    <form method="POST" action="/write">
    <fieldset>
    <legend>慢慢来～一行一行地写 ^_^</legend>
    <input name="content" type="text" style="width:1200px;height:30px" />
    <input type="submit" value="上传" style="height:30px;position:absolute;+margin-top:2px" />
    </fieldset>
    </form>
    <a href = "http://diaryweb.sinaapp.com/read">日记历史</a>
    <p> %s </p>
    </body>
    </html>
    ''' % saveLine.replace('\n', '<br />')

#保存命令行界面提交的新日记信息
@app.route('/save', method = 'POST')
def save():
    saveLine = bucket.get_object_contents('mydiary.txt') + '\n' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n' + request.POST.get('newline') + '\n'
    bucket.put_object('mydiary.txt', saveLine)

#向命令行界面打印历史日记信息
@app.route('/readcli')
def readcli():
    return '%s' % bucket.get_object_contents('mydiary.txt')
    
application = sae.create_wsgi_app(app)

