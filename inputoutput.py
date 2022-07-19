# Problem 1.1
"""
Write a program that takes three numbers and prints their sum.
Every number is given on a separate line.
"""
def consoleInputOutput():
    input1= int(input())
    input2 = int(input())
    input3 = int(input())
    result = input1 + input2 + input3
    print(result)

# Problem 1.2
"""
Purpose: Practice handling multiple console inputs and outputting
a decimal.
Write a program that reads the length of the basr and the height
of a right-angled triangle and prints the area. Every number
is given on a separate line.
"""
def areaOfATriangle():
    b = int(input())
    h = int(input())
    area = 0.5*b*h
    print(area)

# Problem 1.3
"""
Practice concatenation
Write a program that greets the user by printing the word "Hello",
a comma, the name of the user and an exclamation mark after it.
"""
def helloPotter():
    name = input()
    print("Hello" + ", " + name + "!")

# Problem 1.4
"""
Practice printing input to the console
Write a program that reads an integer number and prints its previous
and next numbers.
"""
def previousAndNext():
    #input
    num = int(input())
    #formula for previous num
    prev = num - 1
    #formula for next num
    next = num + 1
    #print nums
    print("The next number for the number " + str(num) + " is " + str(next))
    print("The previous number for the number " + str(num) + " is " + str(prev))

# Problem 1.5
"""
Practice printing mathematical operations to the console
N students take K apples and distribute them among each other evenly.
The remaining (the indivisible) part remains in the basjet. How many
apples will each single student get? How many apples will remain in the basket?
"""
def dividingApples():
    # N number of students
    N = int(input())
    # K number of apples
    K = int(input())
    # formula for apples per student
    student = K//N
    # formula for remaining apples in basket
    remaining = K%N
    # print apples per student
    print(student)
    # print remainder
    print(remaining)

# Problem 1.6
"""
Practice printing two mathematical operations to the console.
Given the integer N - the number of seconds that is passed since
midnight - how many full hours and fill minutes are passed since midnight?
The program shouhld print two number: the number of hours (between 0 and 23)
and the number of minutes (between 0 and 1339).
"""
def timePastMidnight():
    #N number of seconds
    N = int(input())
    #seconds to minutes
    fullMinutes = int(N//60)
    #minutes to hours
    fullHours = fullMinutes//60
    #print hours
    #print minutes
    print(fullHours, fullMinutes)

# Problem 1.7
"""
Practice printing multiple mathematical expressions to the console
Given two timestamps of the dame day: a number of hours, minutes, and
seconds for both of the timestamps. The moment of the first timestamp happened
before the moment of the second one. Calculate how many seconds passed betweem
them.
"""
def secondsPassed():
    #hours in first timestamp
    #minutes in first timestamp
    #seconds in first timestamp
    firsthours = int(input())
    firstminutes = int(input())
    firstseconds = int(input())
    
    #convert time to seconds
    firstHoursToSeconds = firsthours*3600
    firstMinutesToSeconds = firstminutes*60

    #number of seconds in first timestamp
    firstTimestamp = firstHoursToSeconds + firstMinutesToSeconds + firstseconds
    
    #hours in second timstamp
    #minutes in second timestamp
    #seconds in second timestamp
    secondhours = int(input())
    secondminutes = int(input())
    secondseconds = int(input())
    
    #convert time to seconds
    secondHoursToSeconds = secondhours*3600
    secondMinutesToSeconds = secondminutes*60

    #number of seconds in second timestamp
    secondTimestamp = secondHoursToSeconds + secondMinutesToSeconds + secondseconds
    
    #print difference of seconds
    print(secondTimestamp - firstTimestamp)