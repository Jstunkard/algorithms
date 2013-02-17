import random
import math
TEST = True
question1 = False


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
    arraysum(numbers,i+1,summ,location+1)









def divideConquerSum(numbers):
  i = 0
  summ = 0
  while i < len(numbers):
    summ += numbers[i]
    i += 1
  return summ

#Now need to finish the level identification #'s

def divide(numbers,level):
  level += 1
  print "level", level
  if len(numbers) <= 4:
    summ = divideConquerSum(numbers)
    return summ
    #total += summ
  else:
    middle = len(numbers) / 2
    firstHalf = numbers[:middle]
    lastHalf = numbers[middle:]
    
    first = divide(firstHalf,level)
    print "first", first
    second = divide(lastHalf,level)
    print "second", second
    total = first + second
    
    return total









if TEST == False:
  foo = open("input.txt", "r")
  bar = foo.read()
  numbers = map(int, bar.split(', '))
  
else: 
  numbers = range(1,17) #A small array I used for testing

output = 0
summ = 0
location = 0
print numbers
#arraysum(numbers,output,summ,location)
print divide(numbers,0)
