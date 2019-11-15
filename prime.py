#PRIME NUMBER CHECKER

num = int(input("Enter a number: "))

if num > 1:

   for x in range(2, num):
       if (num % x) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")

elif num == 1:
    print(num, "is a prime number")
else:
   print(num, "is not a prime number")