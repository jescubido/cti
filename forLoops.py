# Problem 1
"""
Given a positive integer N, print the numbers from 1 to N.
But for multiples of 3 print “Fizz” instead of the number.
For the multiples of 5, print “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, print 
“FizzBuzz” instead of the number.
"""
def FizzBuzz():
   # Take input of first number
   n = int(input())
      # Use for loop to take one number from 1 to n
   for i in range(1, n+1):
   # Check if divisible by 3 and 5
   # If yes, print "FizzBuzz"
      if(i%3 == 0) and (i%5 == 0):
         print("FizzBuzz")
   # Check if divisible by 3
   # If yes, print "Fizz"
      elif(i%3 == 0):
         print("Fizz")
   # Check if divisible by 5
   # If yes, print "Buzz"
      elif(i%5 == 0):
         print("Buzz")
      else:
         print(i)

# Problem 2
""" 
Given an integer array nums, move all the even integers 
at the beginning of the array followed by all the odd integers.
"""
def sortArrayByParity(A):
   B = []
# Take one number
# Check if divisible by 2
# If yes, put into a separate array
   for num in A:
      if(num%2 == 0):
         B.append(num)
      
# Take one number
# Check if NOT divisible by 2
# If yes, put into a separate array
   for num in A:
      if(num%2 != 0):
         B.append(num)
# Return new array
   return B

# Problem 3
""" 
Given a string columnTitle that represents the column 
title as appears in an Excel sheet, return its corresponding 
column number.
"""
def excel_column_to_number(column):
   lengthOfColumn = len(column)
   answer = 0
   i = 0
  
  # Range(start, end, increment/decrement) 
   for index in range(lengthOfColumn - 1, -1, -1):
      # ord converts characters to decimal value - 64
      n = ord(column[index]) - 64
      answer = answer + n * (26 ** i)
      i = i + 1
      
   return answer

# Problem 4
"""
You are given a large integer represented as an integer array 
digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any 
leading 0's.
Increment the large integer by one and return the resulting array
of digits
"""
def plusOne(digits):
   # Determine length of array
   length = len(digits)
   # Range(start, end, decrement)
   for i in range (length - 1, -1, -1):
      # function/operation of adding 1 to num
      num = digits[i] + 1
      # If num is greater than 9, make digit == 0 and 
      # add another digit + current digits
      if num > 9:
         digits[i] = 0
         if i == 0:
            digits = [1] + digits
         # Else, add 1 to current digit
         else:
            digits[i] += 1
            break
   # Return digits
   return digits

# Problem 5
"""
Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""
def twoSum(nums, target):
   # Initialize out list
   out = []
   # Loop through the input to pick first_num
   for i in range(len(nums)):
      first_num = nums[i]
      # Loop through the remaining input to pick sec_num
      for j in range(i + 1, len(nums)):
         sec_num = nums[j]
         # If (first_num + sec_num == target)
         if (first_num + sec_num == target):
            # Add index of first_num, sec_num to out
            out.append(i)
            out.append(j)
   # Return out
   return out