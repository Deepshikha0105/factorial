n=int(input("enter a number: "))
fact=1
for i in range(1, n+1):
    if n<=0:
        print("factorial is 1")
    else:
        fact = fact*i
print(f"factorial of {n} is " + str(fact))
