def check_prime(num):
    if num > 1: 
        for i in range(2,num//2):
            if num % i == 0:
                return False
        return True
    else:
        return True

def check_pandigital(num,s):
    n=str(num) 
    len(n)==s 
    master_numbers = '1234567890'
    return not (master_numbers[:s]).strip(n)

n = 7654321
iteration = 0
while not (check_pandigital(n,7) and check_prime(n)):
    n -= 2
    iteration +=1 
print ('largest number = ',n,iteration)
