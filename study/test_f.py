def fibonacci():
     a = b = 1
     yield a
     yield b
     while True:
        a, b = b, a+b
        yield b

for num in fibonacci():
    if num > 100: break
    print num,
print

def counter(start=1):
    while True:
        yield start
        start +=1

for num in counter():
    if num >10 :break
    print num,
