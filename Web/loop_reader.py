#-*-coding=utf-8
__author__ = 'zhaor'
import useinfo

info = useinfo.zidian()

for us,pw in info.items():
    print us
    print pw