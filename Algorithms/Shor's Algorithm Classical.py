import math
import sys
import array as arr
from random import randrange

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

print('Shor\'s Algorithm - The classical approach')

while True: 
  N = int(input('Enter N to factorize: '))
  if (N % 2 == 0 or is_prime(N)):
    print('Must not be even or a prime.')
  else: 
    break;
  
print('N = ' + str(N))

while True:
  k = randrange(1, N-1)
  print('k = ' + str(k))

  gcd = math.gcd(N, k)
  print('GCD(N, k) = ' + str(gcd))

  if (gcd != 1):
    a = int(gcd)
    b = int(N / gcd)
    print('')
    print('Congratulations! Factors of N = ' + str(N) + ' are (' + str(a) + ', ' + str(b) + ')')
    sys.exit()
    
  print('Doing transformations:')  

  q = 1
  tn = 0
  t_array = arr.array('i')
  while True:
    product = int(q*k)
    remainder = int(product % N)
    t_array.append(remainder)
    tn += 1
    print(str(q) + ' x ' + str(k) + ' mod ' + str(N) + ' = ' + str(remainder))
    
    if (remainder == 1):
      break
    else:
      q = remainder
      
  if (tn % 2 == 0):
    r_2 = int((tn / 2) - 1)
    p = t_array[r_2]
    if (p + 1 != N):
      break
    
  t_array = []
  print('')
  print('Choosing diffent random k')
      
print('p = ' + str(p))

f1 = math.gcd(p + 1, N)
f2 = math.gcd(p - 1, N)

print('The factors of N = ' + str(N) + ' are: (' + str(f1) + ', ' + str(f2) + ')')
