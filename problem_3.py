#1
a = 24
b = 36
c = 16

divisor = min(a,b,c)
while divisor > 0:
    if a % divisor == 0 and b % divisor == 0 and c % divisor == 0:
        print("The GCD is ", divisor)
        break
    divisor -= 1

#2
a = 24    
b = 36

divisor = min(a,b)
while divisor > 0:
    if a % divisor == 0 and b % divisor == 0:
        print("The GCD is ", divisor)
        break
    divisor -= 1

#3
a = 24

divisor = min(a)
while divisor > 0:
    if a % divisor == 0:
        print("The GCD is ", divisor)
        break
    divisor -= 1
    

#4
a = ''

divisor = min(a)
while divisor > 0:
    if a % divisor == 0:
        print("The GCD is ", divisor)
        break
    divisor -= 0