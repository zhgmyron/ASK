
#-*-coding=utf-8
__author__ = 'zhaor'
f = open("F://test.txt")
line = f.readline()
while line:
    print line,
    # print(line, end = '')
    line = f.readline()

f.close()