import random
import math
TEST = False
question1 = False

# Recursive function to sum numbers
# This does NOT use the divide and conquer method
def recursionsum(numbers,count,summ,location):
  size = len(numbers)
  i = count

  if i >= (len(numbers)-4):
    while i < size:
      summ += numbers[i]
      i += 1
      print "Sum at",location, "is: ",summ
      location += 1

    print summ
  else:
    summ += numbers[i]
    print "Sum at", location, "is: ",summ
    recursionsum(numbers,i+1,summ,location+1)

# Routine to find the sum of the members of a given array
def divideConquerSum(numbers):
  i = 0
  summ = 0
  while i < len(numbers):
    summ += numbers[i]
    i += 1
  return summ

#Now need to finish the level identification #'s

# Divide-and-Conquer method to find the sum of an array of numbers
# Must be passed and array of numbers and the default starting recursion level (0)
def divideAndConquer(numbers,level):
  print "level", level
  level += 1
  if len(numbers) <= 4:
    summ = divideConquerSum(numbers)
    return summ
    #total += summ
  else:
    middle = len(numbers) / 2
    firstHalf = numbers[:middle]  # Split the origional array into
    lastHalf = numbers[middle:]   #  a first and last half

    first = divideAndConquer(firstHalf,level)
    print "first half", first
    second = divideAndConquer(lastHalf,level)
    print "second half", second
    total = first + second
    print "total:",total
    return total


if TEST == False:
  foo = open("input.txt", "r")
  bar = foo.read()
  numbers = map(int, bar.split(', '))
  
else: 
  numbers = range(1,513) #A small array I used for testing

location = 0
print numbers
print divideAndConquer(numbers,location)
# Recursion function I used to compare the Divide and Conguer function with
#print recursionsum(numbers,0,0,0)
