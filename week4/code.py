def gen(n):
  a = 1
  for i in range(n):
    yield a 
    a += 1
gen(10)
