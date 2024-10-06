#1
a = int(input("Enter a starting number : "))
b = int(input("Enter an ending number : "))

for i in range(a,b+1):
    if i>1:
        for m in range(2,i):
            if i%m == 0:
                break
        else:
            print(i)