def quicksortTest(A,p,r):
  print A
  if (p<r):
    q = hoare(A,p,r)
    quicksortTest(A,p,q-1)
    quicksortTest(A,q+1,r)
  print A
 

def partition(A, p, r):
  x = A[p]
  print "Pivot: ", x
  i = p-1
  j = r+1
  while True:
    while True:
      j=j-1
      if not (A[j]<=x):
        break
    while True:
      i=i+1
      if not (A[i]>=x):
        break
    if (i<j):
      A[i], A[j] = A[j], A[i]
    else: return j
  #for j in range(0,r,1):
    #print "J: ", j
    #print "i: ", i
    #if (A[j]<=x):
      #i+=1
  #    A[i], A[j] = A[j], A[i]
  #temp = A[i+1]
  #A[i+1] = A[r]
  #A[r] = temp
  #return i+1


def hoare(a, p, r):
  x = a[p]
  i, j = p-1, r+1
  while True:
    while True:
      j -= 1
      if a[j] <= x:
        break
    while True:
      i += 1
      if a[i] >= x:
        break
    if i < j:
      a[i], a[j] = a[j], a[i]
    else:
      return j

Array = [2,8,7,1,3,5,6,4]
p = 0
r = len(Array)-1
quicksortTest(Array,p,r)

