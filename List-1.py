# -*- coding: utf-8 -*-
"""
Herman Sanghera
November 2, 2019
CodingBat Solutions (Python)

This is a python file containing my own solutions to the
different Python List-1 exercises on codingbat.com
"""

""" 
List-1 > first_last6:
Given an array of ints, return True if 6 appears as 
either the first or last element in the array. The array 
will be length 1 or more.
"""
def first_last6(nums):
  if(nums[0] == 6 or nums[len(nums)-1] == 6):
    return True
  return False

"""
List-1 > same_first_last
Given an array of ints, return True if the array is length 
1 or more, and the first element and the last element are equal.
"""
def same_first_last(nums):
  if(len(nums) >= 1 and nums[0] == nums[len(nums)-1]):
    return True
  return False

"""
List-1 > make_pi
Return an int array length 3 containing the first 3
digits of pi, {3, 1, 4}.
"""
def make_pi():
  a = [3, 1, 4]
  return a

"""
List-1 > common_end
Given 2 arrays of ints, a and b, return True if they have the 
same first element or they have the same last element. Both 
arrays will be length 1 or more.
"""
def common_end(a, b):
  if(a[0] == b[0] or a[len(a)-1] == b[len(b)-1]):
    return True
  return False

"""
List-1 > Sum3
Given an array of ints length 3, return the sum of all the elements.
"""
def sum3(nums):
  sum = 0
  for element in nums:
    sum += element
  return sum

"""
List-1 > rotate_left3
Given an array of ints length 3, return an array with the 
elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
"""
def rotate_left3(nums):
  return([nums[1],nums[2],nums[0]])
  
"""
List-1 > reverse3
Given an array of ints length 3, return a new array with the 
elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
"""
def reverse3(nums):
  return(nums[len(nums)::-1])
  
"""
List-1 > max_end3
Given an array of ints length 3, figure out which is larger, 
the first or last element in the array, and set all the other 
elements to be that value. Return the changed array.
"""
def max_end3(nums):
  if(nums[0] > nums[len(nums)-1]):
    max = nums[0]
  else:
    max = nums[len(nums)-1]
  
  for i in range(len(nums)):
    nums[i] = max
  return nums

"""
List-1 > sum2
Given an array of ints, return the sum of the first 2 elements 
in the array. If the array length is less than 2, just sum up 
the elements that exist, returning 0 if the array is length 0.
"""
def sum2(nums):
  sum = 0
  i = 0
  while i < 2 and i < len(nums):
    sum += nums[i]
    i+=1
  return sum

"""
List-1 > middle_way
Given 2 int arrays, a and b, each length 3, return a new array 
length 2 containing their middle elements.
"""
def middle_way(a, b):
  c = [a[len(a)/2], b[len(b)/2]]
  return c

"""
List-1 > make_ends
Given an array of ints, return a new array length 2 containing 
the first and last elements from the original array. The original 
array will be length 1 or more.
"""
def make_ends(nums):
  return([nums[0], nums[len(nums)-1]])

"""
List-1 > has23
Given an int array length 2, return True if it contains a 2 or a 3.
"""
def has23(nums):
  for element in nums:
    if element == 2 or element == 3:
      return True
  return False






