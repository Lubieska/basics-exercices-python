#Series de Fibonacci:
# La suma de 2 elementos, define el siguiente elemento

#Esto
a,b = 0,1
#es lo mismo que esto
#a 0 0
#b = 1

while b < 10:
  print(b)
  a, b = b, a+b