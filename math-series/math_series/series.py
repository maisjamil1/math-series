def sum_series(nth,f=0,s=1):
  if f < 0 or nth < 0 or s< 0:
    print("wronge input ,enter a positive num please")
  elif f==0:
    return fibonacci(nth)
  
  elif f==2:
    return lucas(nth)
  else:
    # pass
    return other_series(nth,f,s)






def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
  if (n == 0) :
        return 2 
  if (n == 1) :
        return 1
  return lucas(n - 1) +lucas(n - 2) 
  
def other_series(nth,f,s):
  if (nth == s) :
        return s 
  if (nth == f) :
        return f
  else:
       return(other_series(nth-1,f,s) + other_series(nth-2,f,s))

# print(sum_series(7,2,1))