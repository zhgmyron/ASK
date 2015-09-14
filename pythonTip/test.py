__author__ = 'ron'
import  math

list = []


for i in range(2, 100):
    prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        list.append(i)


print ' '.join(str(x) for x in list)