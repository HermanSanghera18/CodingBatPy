# -*- coding: utf-8 -*-
"""
Herman Sanghera
October 26, 2019
CodingBat Solutions (Python)

This is a python file containing my own solutions to the
different Python Warmup-2 exercises on codingbat.com
"""

""" 
Warmup-2 > string_times:
Given a string and a non-negative int n, return a larger string 
that is n copies of the original string.
"""
def string_times(str, n):
  answ = ""
  for x in range(n):
    answ += str
  return answ;

"""
Warmup-2 > front_times:
Given a string and a non-negative int n, we'll say that the front 
of the string is the first 3 chars, or whatever is there if the 
string is less than length 3. Return n copies of the front.
"""
def front_times(str, n):
  answ = ""
  for x in range(n):
    answ += str[:3]
  return answ;

"""
Warmup-2 > string_bits:
Given a string, return a new string made of every other char 
starting with the first, so "Hello" yields "Hlo".
"""
def string_bits(str):
  return(str[::2])

"""
Warmup-2 > string_explosion:
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
  answ = ""
  for i in range(len(str)+1):
    answ += str[0:i]
  return answ

"""
Warmup-2 > last2:
Given a string, return the count of the number of times that a substring
length 2 appears in the string and also as the last 2 chars of the 
string, so "hixxxhi" yields 1 (we won't count the end substring).
"""
def last2(str):
  num = 0
  if(len(str) <= 2):
    return num
  else:
    last2 = str[-2:]
    for i in range(len(str)-2):
      if(last2 == str[i:i+2]):
        num+=1
  return num

"""
Warmup-2 > array_count9
Given an array of ints, return the number of 9's in the array.
"""
def array_count9(nums):
  count = 0
  for element in nums:
    if element == 9:
      count+=1
  return count

"""
Warmup-2 > array_front9
Given an array of ints, return True if one of the first 4 elements
in the array is a 9. The array length may be less than 4.
"""
def array_front9(nums):
  stop = len(nums)
  if(len(nums) > 4):
    stop = 4
  
  for i in range(stop):
    if nums[i] == 9:
      return True;
  return False;

"""
Warmup-2 > array123
Given an array of ints, return True if the sequence of numbers 1, 2,
3 appears in the array somewhere.
"""
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1:
      if nums[i+1] == 2:
        if nums[i+2] == 3:
          return True;
  return False;

"""
Warmup-2 > string_match
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" 
yields 3, since the "xx", "aa", and "az" substrings appear in the same 
place in both strings.
"""
def string_match(a, b):
  count = 0
  if len(a) >= len(b):
    min = len(b)
  else:
    min = len(a)
  
  for i in range(min-1):
    target1 = a[i:i+2]
    target2 = b[i:i+2]
    if(target1 == target2):
      count+=1;
  return count




 