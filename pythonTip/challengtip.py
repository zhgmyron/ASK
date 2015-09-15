#-*-coding:utf-8-*-
__author__ = 'ron'
import math

def test_5():
    a=2
    b=3

def test_6():
    return filter(is_prime, range(2, 100))
def is_prime():
    for i in range(2,101):
        flage= True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                flage =False
                break
        if flage:
            print i,
def test_51():
    res=list()
    for x in xrange(3,100,2):
        flag = 1
        # print "x",x
        for j in range(2,x):
            # print j
            if x%j == 0:
                # print x,j
                flag=0
                break
        if flag:
            res.append(str(x))
    print "2"," ".join(res)

def test_7():
    L=[0,1,2,3,4,5]
    print sorted(L)
    s=len(L)
    if s%2==0:
        return float((float(L[s/2-1])+float(L[s/2]))/2)
    else:
        return L[s/2]
def test_9(a,b):
    l=[]

    for i in range(1,b+1):
        if a%i==0 and b%i==0:
            l.append(i)

    print max(l)

def test_10(a,b):
    l=[]

    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            l.append(i)
    print a*b/max(l)
L=[3,4,2,10,5,5]
def test_11_0():
    cout=0
    m=reduce(lambda x,y:x*y,L)

    while m%10==0:
        cout=cout+1
        m=m/10

    print cout
def test_11_1():
    t=0
    f=0
    for i in range(len(L)):
        temp=L[i]
        while temp % 2==0:
            temp = temp/2
            t+=1
        temp=L[i]

        while temp%5==0:
            temp = temp/5
            f+=1
    if t*f !=0:
        print min(t,f)
    else:
        print 0
def test_12():

    m=int(reduce(lambda x,y:x*y,L))
    while m%10==0:
        m=m/10
    if m%2==0:
        print "0"
    else:
        print "1"

def test_13(a):
    count = 0
    str1= bin(int(a))
    for i in str1:
        if i=='1':
            count+=1
    print count
def test_15(str1):
    l=[]
    for x in str1:
        if x =="A":
            x="a"
        l.append(x)
    return "".join(l)
def test_17(a):
    if 'lover' in a.lower():
        print 'LOVE'
    else:
        print 'SINGLE'
def test_subtract(st,et):
    str1 =st.split(":")
    et1 =et.split(":")
    s=0
    m=3600
    for i in range(3):
        s=s+int((int(et1[i])-int(str1[i])))*m

        m=m/60
    print s

def test_subtract1(st,et):
    et = map(int, et.split(":"))
    st = map(int, st.split(":"))
    print et
    dif = 0
    for e, s in zip(et, st):
        dif = dif * 60 + (e - s)
    print dif

st="00:00:00"
et="01:01:10"
#test_subtract1(st,et)
def test_leap(year):
    year=int(year)
    if year%4==0 and year%100!=0 or year%400==0:
        print '366'
    else:
        print '365'
#test_leap(2013)
def test_sort():
    L=[0,1,6,3,4,5]
    m=sorted(L)
    n= sorted(L,reverse=True)
    if L==m:
        print "UP"
    elif L==n:
        print "DOWN"
    else:
        print "WRONG"
#test_sort()
def test_equal():
    L=[0,1,6,3,2,5]
    if len(L)==len(set(L)):
        print "YES"
    else:
        print "NO"
def test_equal1():
    L=[0,1,6,3,1,5]
    sign = False
    for i in L:
        if L.count(i) >= 2:
            sign = True

    if sign == True:
        print "YES"
    else:
        print "NO"
#test_equal1()
def test_circler():
    a="abcba"
    n=2
    j = 'NO'
    for i in range(len(a)):
        a1 = a[i:n+i][::-1]
        if a1 == a[i:n+i] and len(a1) == n:
            j = 'YES'
    print j
#test_circler()
t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
print t["year"]