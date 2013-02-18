#!/usr/bin/env python2
TEST = True

def InsertionSort(array):
  i = 0
  j = 0
  n = len(array)

  for j in range(n):
    key = array[j]
    i = j - 1
    while (i >= 0 and array[i] > key):
      array[i + 1] = array[i]
      i = i -1
    array[i + 1] = key

def permutations(array,B):
  i = 0
  j = 0
  n = len(array)
  key = array[len(array)-1] # The key is the last element in array A
  B = range(n)
  print B
  print key
  for j in range(n):
    if (key > array[i] and i >= 0):
      B[i] = (array[i])
    i = i+1


def MergeSort(array):
  i = 0
  j = 0
 # n = 
  

if TEST == False:
  x = raw_input("Enter a list of characters seperated by spaces: ")
  numbers = map(int, x.split())
else: 
  numbers = [5,2,3,7,6,8,1,4]
B = []
print numbers
#InsertionSort(numbers)
permutations(numbers,B)
print numbers
