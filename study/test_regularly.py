#-*-coding:utf-8-*-
import re
"""
.    ƥ������з�����������ַ�
^    ƥ���ַ����Ŀ�ʼ
$    ƥ���ַ����Ľ���
[]   ����ƥ��һ��ָ�����ַ����
��   ����ǰһ���ַ��ַ��ظ�0�ε�1��
*    ����ǰһ���ַ��ظ�0�ε������
{}   ����ǰһ���ַ��ظ�m��
{m��n} ��ǰһ���ַ��ظ�Ϊm��n��
\d   ƥ�����֣��൱��[0-9]
\D   ƥ���κη������ַ����൱��[^0-9]
\s   ƥ������Ŀհ׷����൱��[ fv]
\S   ƥ���κηǿհ��ַ����൱��[^ fv]
\w   ƥ���κ���ĸ�����ַ����൱��[a-zA-Z0-9_]
\W   ƥ���κη���ĸ�����ַ����൱��[^a-zA-Z0-9_]
\b   ƥ�䵥�ʵĿ�ʼ�����
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