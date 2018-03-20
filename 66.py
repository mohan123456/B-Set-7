num = int(input("Enter a no: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("is not a prime")
           break
   else:
       print("Prime number")
else:
   print("Not a prime")
