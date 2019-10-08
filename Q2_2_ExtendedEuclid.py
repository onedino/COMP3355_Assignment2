#Example from geek for geek
#def inverseMod(a, b, x, y): 
#    # Base Case 
#    if a == 0 :  
#        x = 0
#        y = 1
#        return b 
#          
#    x1 = 1
#    y1 = 1 # To store results of recursive call 
#    gcd = inverseMod(b%a, a, x1, y1) 
#  
#    # Update x and y using results of recursive 
#    # call 
#    x = y1 - (b/a) * x1 
#    y = x1 
#  
#    return gcd 
#  
#  
#x = 1
#y = 1
#a = 20999311111111111135
#b = 33332322667876
#g = inverseMod(a, b, x, y) 
#print("Data for testing, c = " , str(a) , ", n = ", str(b), " result = ", g) 


def inverseMod(C,N,ai,ai_1,bi,bi_1):
  if C == "1":
    return bi
  
  c = 0
  n = 0
  for i in range(0,len(N)):
    n = n + int(N[i])*(10**(len(N)-1-i))
  for i in range(0,len(C)):
    c = c + int(C[i])*(10**(len(C)-1-i))  
  
  q1 = int(n/c)
  c1 = n % c
  b1 = bi_1 - bi * q1
  a1 = ai_1 - ai * q1

#  print ("q :"+str(q1)+" a :"+str(a1)+" b :"+str(b1)+ " c :"+str(c1))
  
  return inverseMod(str(c1),str(c),a1,ai,b1,bi)

c = 20999311111111111135
n = 33332322667876
print("data for testing, c = " + str(c) +", n = "+str(n)+", result = " +str(inverseMod(str(c),str(n),0,1,1,0)))
