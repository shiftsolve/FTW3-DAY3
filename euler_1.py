# Proble 15: Power Digit Sum
#2** = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?

prod = 2**1000
print("The answer to 2**1000 is",prod)

sum = 0
while prod > 0:
    d = prod%10
    prod = prod//10
    sum += d

print("The sum of digits of 2**1000 is",sum)