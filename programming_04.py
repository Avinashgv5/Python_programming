#1. Write a Python Program to Find the Factorial of a Number?

n=int(input("enter number for factorial: "))

def factorial(n):
    if n<0:
        print("number shoudnt less than zero")
        return None
    if n==1 or n==0:
        return 1
    else:
        return n* factorial(n-1)
result= factorial(n)
print("factorial of {0} is: {1}".format(n,result))

#2. Write a Python Program to Display the multiplication Table?
x=int(input("enter number for table: "))
y=int(input("enter lenght of table: "))

for i in range(1,y+1):
    print('{0} * {1}= {2}'.format(x,i,x*i))

#3. Write a Python Program to Print the Fibonacci sequence?
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input('Enter the value: '))
if n <= 0:
    print('Please enter positive number')
for i in range(n):
    print(fibonacci(i))

#4. Write a Python Program to Check Armstrong Number?
num = int(input("Enter a number: "))

sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#5. Write a Python Program to Find Armstrong Number in an Interval?
l = int(input('Enter the lower bound value: '))
u = int(input('Enter the upper bound value: '))

for num in range(l, u + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

#6. Write a Python Program to Find the Sum of Natural Numbers?
n = int(input('Enter the number to find sum of natuaral number: '))

def sum_n(x):
    sum = 0
    sum = sum + (x*(x+1))//2
    return sum
res = sum_n(n)
print('sum of {0} numbers is: {1}'.format(n,res))


