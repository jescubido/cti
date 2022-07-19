# Problem 2.1
"""
Given a 2 bit integer, print its left bit (a 2's bit)
and then its right bit (a ones bit). Use the operator of integer
division for obtaining the 2's bit and the operator of taking
remainder for obtaining the ones bit.
"""
def twoBits():
    # plan
    num = int(input())
    # calculate right bit (num % 2)
    right = num % 2
    # calculate left bit (num // 2)
    left = num // 2
    # print left bit and right bit
    print(left, right)

# Problem 2.2
"""
Given a two-digit integer, print its left digit (a tens digit)
and then its right digit (a ones digit). Use the operator of
integer division for obtaining the tens digit and the operator
of taking remainder for obtaining the ones digit.
"""
def twoDigits():
    #plan
    num = int(input())
    # calculate rightmost value (num % 10)
    right = num % 10
    # calculate leftmost value (num // 10)
    left = num // 10
    # print leftmost value and rightmost value
    print(left, right)

# Swap Last Two Digits
"""
To learn number input, mod and integer division operators.
Given an integer greater than 9, print its last two digits in
the reverse order, 1's value first, and then 10's value with a
space in between.
"""
def swapLastTwoDigits():
    #take in input
    num = int(input())
    i = 1
    #identify digit in 1's place
    onesPlace = num%10**1//10**0
    onesToTens = onesPlace*10
    #identify digit in 10's place
    tensPlace = num%10**2//10**1
    #print in reverse order
    print(onesToTens + tensPlace)

# Reverse the Digits
"""
To learn number input, mod, integer division operators and
simple while loops.
Given an integer greater than 9, print all the digits in the
reverse order, 1's value first, and then 10's value and then the
100's value, and so on, with a space in between.
"""
def reverseTheDigits():
    # take the input
    num = int(input())
    reverseNum = ""
    while num > 0:
        temp = num % 10
        reverseNum = reverseNum + str(temp) + " "
        num = int(num/10)
    print(reverseNum)

# Tens Digit
"""
Numbers, modulus, and remainder operators
Given an integer, print its tens digit
"""
def tensDigit():
    #take in input
    n = int(input())
    #identify tens digit
    tens = int(n//10)
    #find remainder
    remainder = int(tens%10)
    #print tens digit
    print(remainder)

# Sum of Digits
"""
Numbers, modulus, and remainder operation
Given a three-digit number, find the sum of its digits without
using string operations.
"""
def sumOfDigits():
    #take input
    n = int(input())
    #find value in one's place
    ones = int(n%10)
    #find value in ten's palce
    numA = int(n//10)
    tens = int(numA%10)
    #find value in hundred's place
    numB = int(numA//10)
    hundreds = int(numB%10)
    #add values together
    print(ones + tens + hundreds)

# Digit After Decimal Point
"""
Numbers, modulus and remainder operations
Given a positive real number, print its first digit to the
right of the decimal point without using string operations.
"""
def digitAfterDecimal():
    #take input
    userInput = float(input())
    #multiply 10 to get first digit right of decimal
    numA = userInput * 10
    #turn into int data type to get rid of remaining decimal
    #mod 10 to get digit
    numB = int(numA % 10)
    #print value
    print(numB)

# Total Cost
"""
To learn input, modulus operator and output formatting
A cupcake costs A dollars and B cents. Determine how many
dollars and cents should one pay for N cupcakes. A program
gets three numbers: A, B, N. It should print two numbers:
total cost in dollars and cents.
"""
def totalCost():
    #take user input
    A = int(input())
    B = float(input())
    N = int(input())
    #turn B into cents (decimal)
    numB = B/100
    #add A and B for total cost of one cupcake
    #multiply to N number of cupcakes
    #print dollars and cents
    oneCupcake = A + numB
    totalCost = oneCupcake * N
    dollars = int(totalCost)
    cents = int((totalCost*100)%100)
    print(dollars, cents)

# Day of Week
"""
To practice remainder operation
Days of week are numbered as : 0 = Sunday, 1 - Monday,
2 - Tuesday, ..., 6 - Saturday. An integer K in the range
1 to 365 is given. Find the number of day of week for K-th
day of year provided that in this year January 1 was Thursday.
"""
def dayOfWeek():
    #take user input
    K = int(input())
    #mod 7 for days of week
    #add 3 to K for shift
    dayOfWeek = (K + 3) % 7
    #print value
    print(dayOfWeek)

# Digital Clock
"""
To practice remainder and integer divison operations
Given the integer N - the number of minutes that is passed
since minutes are displayed on the 24h digital clock?
The program should print two number: the number of hours
(between 0 and 23) and the number of minutes (between 0 and 59).
For example, if N = 150, then 150 minutes have passed since
midnight - i.e. now is 2:30 am. So the program should pritn 2 30.
"""
def digitalClock():
    #take in user input
    N = int(input())
    #calculate hours passed
    hours = N//60
    #calculate minutes passed
    minutes = N%60
    #print time passed
    print(hours, minutes)

# Clock Face
"""
To practice remainder and integer divison
The hour hand of an analog clock turned α degrees since the midnight.
Determine and print the angle by which the minute hand turned since
the start of the current hour. Input and output in this problem
are integers.
"""
def clockFace():
    #take user input
    α = int(input())
   # Check if divisible by 30
   # If yes, print 0
    if(α%30 == 0):
        print(0)
    else:
        print((α * 12)%360)

# School Desks
"""
A school decided to replace the desks in three classrooms. Each desk
sits two students. Given the number of students in each class, print
the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each
of the three classes, a, b, and c, respectively.
"""