# -*- coding: utf-8 -*-
#!/usr/bin/env python

_author_ = 'Wills Wong'

"""
----------------Version 1.0--------------------
极简交互式笔记（网络版）服务器端
"""

#全局引用
import os,sys,time,threading,socket

def main():

    def choose(data, addr):
        if data == '-*-saveContent-*-':
            uname, addr = s.recvfrom(2048)
            newContent, addr = s.recvfrom(2048)
            savepath = '/home/wong/slog/' + uname + '/server_diary.txt'
            with open(savepath, 'a') as f:
                f.write('\n' + newContent)
            print 'File was saved successfully @ %s,%s' %(addr)

        if data == '-*-historyContent-*-':
            usr_name, addr = s.recvfrom(2048)
            findpath = '/home/wong/slog/' + usr_name + '/server_diary.txt'
            if os.path.exists(findpath) == True:
                s.sendto('T', addr)
                with open(findpath, 'r') as f:
                    s.sendto(f.read(), addr)
                print 'History was sent successfully @ %s,%s' %(addr)
            else:
                s.sendto('F', addr)
        
        if data == '-*-signup-*-':
            sinup_username, addr = s.recvfrom(2048)
            signup_dirs = '/home/wong/slog/' + sinup_username
            if os.path.exists(signup_dirs) == True:
                s.sendto('F', addr)
                print 'Signup failed! @ %s,%s' %(addr)
            else:
                s.sendto('T', addr)
                signup_passwd, addr = s.recvfrom(2048)
                os.makedirs(signup_dirs)
                signup_filePath = signup_dirs + '/Password.txt'
                with open(signup_filePath, 'w') as f:
                    f.write(signup_passwd)
                print 'Signup successfully! @ %s,%s' %(addr)

        if data == '-*-login-*-':
            login_username, addr = s.recvfrom(2048)
            login_passwd, addr = s.recvfrom(2048)
            login_dirs = '/home/wong/slog/' + login_username
            login_filePath = login_dirs + '/Password.txt'
            if os.path.exists(login_dirs) == False:
                s.sendto('N', addr)
                print 'User does not exists! @ %s,%s' %(addr)
            else:
                with open(login_filePath, 'r') as f:
                    passwd_test = f.read()
                if login_passwd != passwd_test:
                    s.sendto('F', addr)
                    print 'Password error! @ %s,%s' %(addr)
                else:
                    s.sendto('T', addr)
                    print 'Login successfully! @ %s,%s' %(addr)
            

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',9999))
    print 'Bind UDP on 9999 ...\n'

    while True:
        data, addr = s.recvfrom(2048)

        t = threading.Thread(target = choose ,args = (data, addr))
        t.start()
        t.join()

#自检区，判断脚本直接被运行 or 作为模块调用
if __name__ == '__main__':
    main()

