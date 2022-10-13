#check for prime
ch='y'
while (ch=='y') or (ch=='Y'):
    a=int(input("enter no. you want to check:"))
    b=int(a/2)+1
    #print("b =",b)
    for i in range(2,b+1):
        c=a%i
        #print(c)
        if c==0:
            break
    if c!=0:
        print("entered no. is a prime no.")
    else:
        print("entered no. is not a prime no.")
    ch=input("do you want to check more numbers y/n:")
print("Good bye")
print("Hope i helped!!")
