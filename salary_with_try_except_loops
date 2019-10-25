#asking for input
h=input("hours: ")
r=input("rate: ")
#nutrilizing input errors
try:
    ih=float(h)
    ir=float(r)
except:
    ih=-1
    ir=-1
#re-asking for input if there are some errors 
while ih==-1 or ir==-1:
    print("Please enter a numerical value")
    h=input("hours: ")
    r=input("rate: ")
    try:
        ih=float(h)
        ir=float(r)
    except:
        ih=-1
        ir=-1
#result        
salary=ih*ir
isalary=int(salary)
print("Thanks, the salary is", isalary, "MAD")
