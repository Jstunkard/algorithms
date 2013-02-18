def mergeSort(A,p,r):
  if p<r
    q = (p+r)/2
    mergeSort(A,p,q)
    mergeSort(A,q+1,r)
    merge(A,p,q,r)

def merge(A,p,q,r):
  n1 = q-p+1
  n2 = r-q
  L = A[:n1+1]
  R = A[:n2+1]
  for i=1 to n1
    L[i] = A[p+i-1]
  for j=1 to n2
    R[j] = A[q+j]
  L[
