a = int(input("FIRST NUMBER:"))
b = int(input("SECOND NUMBER:"))

if a % b == 0:
    print("Your HCF is:",b)
elif b % a == 0:
    print("Your HCF is:",a)
elif b % a != 0 and a % b != 0 :
    print("Your HCF is:",1)
