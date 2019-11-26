# -*- coding: utf-8 -*-
"""
Herman Sanghera
November 6, 2019
CodingBat Solutions (Python)

This is a python file containing my own solutions to the
different Python List-2 exercises on codingbat.com
"""


"""
List-2 > count_evens:
Return the number of even ints in the given array. Note: 
the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
"""
def count_evens(nums):
  count = 0
  for element in nums:
    if element%2 == 0:
      count+=1
  return count
    

"""
List-2 > big_diff:
Given an array length 1 or more of ints, return the difference 
between the largest and smallest values in the array. Note: the 
built-in min(v1, v2) and max(v1, v2) functions return the smaller 
or larger of two values.
"""
def big_diff(nums):
  i = 0
  big = max(nums[0], nums[0])
  small = min(nums[0], nums[0])
  
  while(i < len(nums)):
    big = max(big, nums[i])
    small = min(small, nums[i])
    i += 1
  
  return(big - small)
  
"""
List-2 > centered_average:
Return the "centered" average of an array of ints, which 
we'll say is the mean average of the values, except ignoring 
the largest and smallest values in the array. If there are 
multiple copies of the smallest value, ignore just one copy, 
and likewise for the largest value. Use int division to produce 
the final average. You may assume that the array is length 3 or 
more.
"""
def centered_average(nums):
  small = min(nums[1], nums[2])
  big = max(nums[1], nums[2])
  i = 0
  sum = 0
  
  for i in range(len(nums)):
    small = min(small, nums[i])
    big = max(big, nums[i])
    sum += nums[i]
  
  return((sum-small-big)/(len(nums)-2))

"""
List-2 > sum13:
Return the sum of the numbers in the array, returning 0 for an 
empty array. Except the number 13 is very unlucky, so it does 
not count and numbers that come immediately after a 13 also do 
not count.
"""
def sum13(nums):
  sum = 0
  i = 0
  while i < len(nums):
    if(nums[i] == 13):
      i+=1
    else:
      sum += nums[i]
    i += 1
  return sum

"""
List-2 > sum67:
Return the sum of the numbers in the array, except ignore 
sections of numbers starting with a 6 and extending to the
next 7 (every 6 will be followed by at least one 7). Return 
0 for no numbers.
"""
def sum67(nums):
  x = 0
  sum = 0
  
  while x < len(nums):
    if(nums[x] == 6):
      while(x < len(nums) and nums[x] != 7):
        x += 1
    else:
      sum += nums[x]
    x += 1
  return sum

"""
List-2 > has22:
Given an array of ints, return True if the array contains a 
2 next to a 2 somewhere.
"""
def has22(nums):
  if len(nums) == 1:
    return False
  for i in range(len(nums)-1):
    if(nums[i] == 2 and nums[i+1] == 2):
      return True
  return False
  
  
  
  
