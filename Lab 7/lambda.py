def x(a): return a + 10
print(x(5))



def x(a, b): return a * b
print(x(5, 6))



def myfunc(n):
  return lambda a: a * n

double = myfunc(2)
print(double(11))
