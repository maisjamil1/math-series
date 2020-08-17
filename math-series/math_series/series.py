def sum_series(nth,f=0,s=1):
  if f < 0 or nth < 0 or s< 0:
    print("wronge input ,enter a positive num please")
  elif f==0:
    return fibonacci(nth)
  
  elif f==2:
    return lucas(nth)
  else:
    # pass
    return fibonacci(nth)



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


# print(sum_series(7,2,1))