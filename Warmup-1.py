# -*- coding: utf-8 -*-
"""
Herman Sanghera
October 25, 2019
CodingBat Solutions (Python)

This is a python file containing my own solutions to the
different Python Warmup-1 exercises on codingbat.com
"""


""" 
Warmup-1 > sleep_in:
The parameter weekday is True if it is a weekday, 
and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. 
Return True if we sleep in.
"""
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

"""
Warmup-1 > monkey_trouble:
We have two monkeys, a and b, and the parameters a_smile 
and b_smile indicate if each is smiling. We are in trouble 
if they are both smiling or if neither of them is smiling. 
Return True if we are in trouble.
"""
def monkey_trouble(a_smile, b_smile):
  return (((a_smile and b_smile) or (not a_smile and not b_smile)))

"""
Warmup-1 > sum_double:
Given two int values, return their sum. Unless the two values 
are the same, then return double their sum.
"""
def sum_double(a, b):
  c = a + b
  if (a == b):
    c= 2 * c
  return c
    
"""
Warmup-1 > diff21:
Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.
"""
def diff21(n):
  c = abs(21 - n)
  if n > 21:
    c = 2 * c
  return c
  
"""
Warmup-1 > parrot_trouble:
We have a loud talking parrot. The "hour" parameter is the current 
hour time in the range 0..23. We are in trouble if the parrot is 
talking and the hour is before 7 or after 20. Return True if we 
are in trouble.
"""
def parrot_trouble(talking, hour):
  if not talking:
    return False
  elif hour < 7 or hour > 20:
    return True
  return False

"""
Warmup-1 > makes10:
Given 2 ints, a and b, return True if one if them is 10 or if 
their sum is 10.
"""
def makes10(a, b):
  c = a + b
  if(c == 10 or a == 10 or b == 10):
    return True 
  else:
    return False

"""
Warmup-1 > near_hundred:
Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
"""
def near_hundred(n):
  a = abs(200 - n);
  b = abs(100 - n);

  if(a <= 10 or b <= 10):
    return True
  return False

"""
Warmup-1 > pos_neg:
Given 2 int values, return True if one is negative and one is 
positive. Except if the parameter "negative" is True, then return 
True only if both are negative.
"""
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

"""
Warmup-1 > not_string:
Given a string, return a new string where "not " has been added to
the front. However, if the string already begins with "not", return 
the string unchanged.
"""
def not_string(str):
  if(len(str) <= 2 or str[0:3] != "not"):
    return("not " + str)
  return str;

"""
Warmup-1 > missing_char:
Given a non-empty string and an int n, return a new string where the 
char at index n has been removed. The value of n will be a valid index
of a char in the original string (i.e. n will be in the range 
0..len(str)-1 inclusive).
"""
def missing_char(str, n):
  return(str[0:n] + str[n+1:])
  
"""
Warmup-1 > front_back:
Given a string, return a new string where the first and 
last chars have been exchanged.
"""
def front_back(str):
  if len(str) >= 2:
    return(str[-1] + str[1:len(str)-1] + str[0])
  return str;


"""
Warmup-1 > front3:
Given a string, we'll say that the front is the first 3 chars of the 
string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
"""
def front3(str):
  if(len(str) >= 3):
    return(str[0:3]+str[0:3]+str[0:3])
  return(str + str + str)







