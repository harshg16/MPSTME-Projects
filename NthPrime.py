n = (int) (input())

def is_prime(num):
    factor = 2
    while (factor < num):
        if num%factor == 0:
             return False
        factor +=1
    return True

if n==1:
    print (2)
count = 1
num = 3
while(count <= n):
    if is_prime(num):
        count +=1
        if count == n:
            print(num)
            break
    num +=2 
    
