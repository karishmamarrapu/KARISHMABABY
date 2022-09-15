x=input("enter the first number :")
y=input("enter the second number :")
if x.isnumeric() and  y.isnumeric():
    print("it is a neumeric")  
    a=int(x)
    b=int(y)
    c=input("enter any operator:")
    if c=='+':
     print(a+b)
    elif c=='-':
     print(a-b)
    elif c=='*':
     print(a*b)
    elif c=='/':
     print(a/b)
    elif c=='()':
     print(a,b)
elif x.isalpha() and y.isalpha():
    print("both are same")      

elif x.isalpha() or y.isnumeric():
    print("both are different") 
else:
    print("both are different")

          
