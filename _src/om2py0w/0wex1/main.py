#!/usr/bin/env python

#OMOOC2py, week one programming, 2015-10-20
_author_ = 'Wills Wong'

import os

def input_one_line(count):
    line_num = 'Line %d :' % count
    a = raw_input(line_num) + '\n'
    with open('/home/wong/test.txt','a') as fileName:
        fileName.write(a)

if os.path.exists('/home/wong/test.txt') == True:
    print '\n*** Here is your writting record ***\n\n'
    with open('/home/wong/test.txt','r') as f:
        print f.read()
        
print '\nNow you can start writing:\n'

print'PS: When you complete writing, please hit Ctrl - C !\n'

line = 0

while True:
	try:
		input_one_line(line)
		line += 1
	except KeyboardInterrupt:
		print '\n\nThanks for using, goobye! ^_^\n'
		break
