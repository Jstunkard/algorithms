import math

def test(n):
  x = 4.0 * math.pow(float(n),2)
  y = 32.0 * float(n) * math.log(float(n))
  if x < y:
    print x
    print y

man = False
if man == True:
  n = raw_input("Enter a value for n")
  test(n)
else:
  n = range(100)
  i = 1
  j = 0
  for j in range(100): 
    print " "
    print i
    test(i)
    i = i + 1
