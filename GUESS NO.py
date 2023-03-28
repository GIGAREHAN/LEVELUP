import random
num = random.randint(1,10)
print(num)

if num % 2 == 0:
    print("It is a even no.")
else:
    print("It is a odd no.")
a = (input("Guess no. : "))

if a == "no":
    print("next hint:")
if a == num:
    print("you got it")
else:
    print("nooo")
if num >= 5:
    print("Greater than or equal to 5")
else:
    print("It is smaller than 5")
b = int(input("Guess no. :"))
if b == num:
    print("YOU GOT IT")
else:
    print("SRY FOR  THIS TIME >3")
print(num)