#Q2 part 1

import time
import math

bigint = "5555555555555555533"

start = time.time()

def isPrime(num):
  start = time.time()
  tmp = 0
  for i in range(0,len(num)):
    tmp = tmp + int(num[i])*(10**(len(num)-1-i))
  
#  print(tmp)
    
  if tmp == 1:
    return False
  if tmp % 2 == 0:
    return False
  else:
    for i in range(3, int(math.sqrt(tmp)), 2):
#      print(i)
      sec = time.time() - start
      if (tmp % i) == 0:
        print (i)
        return False
      if (sec) >= 660:
#        print(i)
        print("run out of time")
        break
    else:
      sec = time.time() - start
      print("Time: ")
      print(sec)
      print(num)
      return True


#change the value here to check if it is a prime number
print(isPrime(bigint))
#print(isPrime(str(5555555555555555533)))
#5555555555555555533 is the largest prime number that my PC can find within 10 minutes
#3874204890000000001)))
