import random
num = random.randint(1,10)
print("Hi welcome to guessing a number game")
print("CHOOSE NUMBER BETWEEN 1 to 10")
'''print(num)'''

if num % 2 == 0:
    print("It is a even no.")
else:
    print("It is a odd no.")

a = int(input("Guess no. :"))
if a == num :
    print("you got it")
    exit()
else:
    print("nooo")
if num >= 5:
    print("Greater than or equal to 5")
else:
    print("It is smaller than 5")
b = int(input("Guess no. :"))
if b == num:
    print()
    print("YOU GOT IT")
else:
    print("SRY FOR  THIS TIME >3")
print("THE NUMBER IS:",num)
print()
print("THANKS FOR PLAYING XD")
print("BY GIGAREHAN")
