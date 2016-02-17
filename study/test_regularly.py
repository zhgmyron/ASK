#-*-coding:utf-8-*-
import re
"""
.    匹配除换行符以外的任意字符
^    匹配字符串的开始
$    匹配字符串的结束
[]   用来匹配一个指定的字符类别
？   对于前一个字符字符重复0次到1次
*    对于前一个字符重复0次到无穷次
{}   对于前一个字符重复m次
{m，n} 对前一个字符重复为m到n次
\d   匹配数字，相当于[0-9]
\D   匹配任何非数字字符，相当于[^0-9]
\s   匹配任意的空白符，相当于[ fv]
\S   匹配任何非空白字符，相当于[^ fv]
\w   匹配任何字母数字字符，相当于[a-zA-Z0-9_]
\W   匹配任何非字母数字字符，相当于[^a-zA-Z0-9_]
\b   匹配单词的开始或结束
"""
name="Hello,My name is kuangl,nice to meet you..."
k=re.search(r'kuangl',name)

print k.group(0)
p = re.compile(r'\d+')
print p.findall('one1two24three3four4')

test="Hi, nice to meet you where are you from?"
k=re.compile(r'\w*o\w*')
print k.findall(test)
n='0102-12345678'
k=re.compile(r'0\d+-\d+')
g='hi a lucy,h i whi him'
g1=re.compile(r'\bhi\b.*\blucy\b')

ho='go  go'
h=re.compile(r'\b\(?<Word>\w+\)\b\s+\\1\b')
t='aabab'
t1=re.compile(r'a.*?b')
print h.findall(ho)
print t1.findall(t)