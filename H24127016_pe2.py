#coding: utf-8

shoppingAmount = float(input("Enter the shopping amount : "))
membershipLevel = input("Enter the membership level (Regular or Gold) : ")

discount = 0.0

if membershipLevel == "Regular" :
    if shoppingAmount > 3000 :
        discount = 0.20
    elif shoppingAmount > 2000 :
        discount = 0.15
    elif shoppingAmount > 1000 :
        discount = 0.10

elif membershipLevel == "Gold" :
    if shoppingAmount > 3000 :
        discount = 0.25
    elif shoppingAmount > 2000 :
        discount = 0.20
    elif shoppingAmount > 1000 :
        discount = 0.15
else :
    print("Invalid member level")

finalAmount = shoppingAmount * (1 - discount)
print(f"{membershipLevel} Member, Final Amount Payable: ${finalAmount:.2f}")