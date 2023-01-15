#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

def number_check(number):
    if number>0:
        print("number is positive")

    elif number<0:
        print("number is negative")

    else:
        print("number is zero")

number=int(input("enter number: "))
number_check(number)


#2. Write a Python Program to Check if a Number is Odd or Even?

def odd_even(number):
    if number%2==0:
        print("number is even")
    else:
        print("number is odd")

number=int(input('enter number: '))
odd_even(number)

#3. Write a Python Program to Check Leap Year?

def leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print("year is leap year")
    else:
        print("year is not leap year")

year=int(input("enter year: "))
leap_year(year)


#4. Write a Python Program to Check Prime Number?
def prime_num_check(number):
    if number <= 1:
        print('Given Number is either less than 1 or 1 which is not a Prime Number')
    if number > 1:
        for i in range(2, number):
            if number % 2 == 0:
                print("the number is not prime")
                break
        else:
            print("the number is prime")


number = int(input("enter the number: "))
prime_num_check(number)




#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
def prime_rang(number):

    a = []
    for num in range(number):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                a.append(num)
    print('prime number beteween 0 and {0} are :{1}'.format(number, a))

number = int(input('Enter the number '))
prime_rang(number)