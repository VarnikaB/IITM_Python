'''
Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.

Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive). The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.
'''
def prime(n):
  if n < 2:
    return False
  for i in range(2,n//2+1):
    if n%i==0:
      return False
  return True
    
def Twin_Primes(n, m):
  Res=[]
  for i in range(n,m-1):
    if prime(i)==True:
      if prime(i+2)==True:
        Res.append((i,i+2))
  return(Res)
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
