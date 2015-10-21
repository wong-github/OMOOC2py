#!/usr/bin/env python

#OMOOC2py, week one programming, 2015-10-20
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

