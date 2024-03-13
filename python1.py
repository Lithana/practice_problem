def fibonacci():
    n=int(input("enter the value"))
    a,b=0,1
    s=str(a)+' ' +str(b)
    print(a,b, end=" ")
    for i in range(n-2):
        a,b=b,a+b
        c=str(a+b)
        print(c, end=" ")
fibonacci()