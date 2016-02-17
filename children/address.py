__author__ = 'zhaor'
def calculateTax(price, tax_rate):
    total = price +(price * tax_rate)

    my_price = 10
    print my_price
    return total
price =1
my_price = float(raw_input("enter a price:"))

totalPrice = calculateTax(my_price,0.06)
print totalPrice

print my_price