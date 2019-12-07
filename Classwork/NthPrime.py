n = (int)(input())

def is_prime(num):
    factor = 3
    while (factor <= num**0.5):
        if num%factor == 0:
             return False
        factor +=2
    return True

if n==1:
    print (2)
count = 1
num = 3
while(True):
    if is_prime(num):
        count +=1
        if count == n:
            print('The prime number is:',num)
            break
    num +=2 
    
