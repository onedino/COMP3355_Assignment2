#Q2 part 1

import time
import math

#bigint = "71755440315342536873"
bigint = "60884036363636410669"
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
    for j in range(6, int(math.sqrt(tmp)), 6):
      i = j - 1
      k = j + 1
#      print(i)
      sec = time.time() - start
      if ((tmp % i) or (tmp % k)) == 0:
        print (j)  #show the number of loops it computes
        return False
      if (sec) >= 600:
        print(i)
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
#60884036363636410669 is the largest prime number that my PC can find within 10 minutes
