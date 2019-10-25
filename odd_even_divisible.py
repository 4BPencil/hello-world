num1=input("num1: ")
num2=input("num2: ")
#convert to int
inum1=int(num1)
inum2=int(num2)
#is num1 odd or even; can it be divided by num2? LET"S SEE!
if inum1%2==0 and inum1%inum2==0:
  print("num 1 is even and divideable by ", inum2)
elif inum1%2==0 and not inum1%inum2==0:
    print("num 1 is even but not divideable by ", inum2)
elif inum1%2!=0 and inum1%inum2==0:
    print("num 1 is odd and divisible by ", inum2)
elif inum1%2!=0 and not inum1%inum2==0:
    print("num 1 is odd and not divisible by ", inum2)
