def fib(n):
 if(n==0) or n==1:
     return n
 else:
     return fib(n-1)+fib(n-2)
n=int(input("Enter the range for fibonacci series:"))
print("Fibonacci Series")
for i in range(0,n):
 print(fib(i),end=' ')



