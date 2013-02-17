#!/usr/bin/env python2
import random
import math
TEST = False
question1 = False

if question1 == True: #A simple method to answer question 1 in the homework
  def q1(n):
    x = 4.0 * math.pow(float(n),2)
    y = 32.0 * float(n) * math.log(float(n))
    if x < y:
      print x
      print y
  n = range(100)
  i = 1
  j = 0
  for j in range(100): 
    print " "
    print i
    q1(i)
    i = i + 1


def permutations(numbers,output):
  leftarray = []
  rightarray = []
  i = 0
  j = 0
  key = numbers[len(numbers)-1] # The key is the last element in the array "numbers"
  numbers.pop(len(numbers)-1)
  n = len(numbers)
  
  for j in range(n):
    if numbers[j] < key:
      leftarray.append(numbers[j])
    else:
      rightarray.append(numbers[j])
  output = leftarray 
  output.append(key)
  output += rightarray
  return output


if TEST == False:
  foo = open("input.txt", "r")
  bar = foo.read()
  numbers = map(int, bar.split(', '))
  
else: 
  numbers = [5,2,3,7,6,8,1,4] #A small array I used for testing

output = []
print numbers
#InsertionSort(numbers)
print permutations(numbers,output)

