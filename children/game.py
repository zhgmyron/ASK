class Ball:
    # def __str__(self):
    #     return  "zhao"
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()

print myBall

print "Number\t\tSquare\t\tlbe"
for i in range (1 , 11):
    print i , "\t\t" ,i**2 , "\t\t" , i**3
