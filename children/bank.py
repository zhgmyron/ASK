__author__ = 'zhaor'
class BankAccount():
    def __init__(self,name,account,blance):
        self.name= name
        self.accout=account
        self.blance=blance
    def mblance(self):
        return  self.blance
    def savemoney(self,money):
        self.blance = self.blance +money
        return  self.blance

    def pickmoney(self,money):
        if self.blance>=money:
            self.blance = self.blance - money
            return  self.blance
        else:
            print "withdraw money"
class InterestAccount(BankAccount):
    def addinterest(self):
        insert=self.blance*0.009
        return self.blance+insert
mb=BankAccount('ron','0001',0.01)

mb.savemoney(5)
print mb.blance