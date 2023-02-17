#incluir la serie fibonacci en un array
#las funciones se definen así:
def fib2(n): # devuelve la serie fibonacci hasta n
    """Devuelve una lista conteniendo la serie de Fibonacci"""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)#append agrega un valor al final del arreglo
        a, b = b, a+b
    return result

# crear una variable y asignarle el valor de la función 
f100 = fib2(100)
print(f100)
