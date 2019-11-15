# PROBLEM3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def Largest(n):
    prime = 1
    x = 2

    while x <= n / x:
        if n % x == 0:
            prime = x
            n /= x
        else:
            x += 1

    if prime < n:
        prime = n

    return prime

print("The Largest Prime factor of  13195  is",Largest(13195))
print("The Largest Prime factor of  600851475143 is",Largest(600851475143))
