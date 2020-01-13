import math
from integration_methods.romberg import Romberg

a = 0
b = 5
TRESHOLD_PRECISION = 1e-09

def f(x):
  return math.exp(x)

rom = Romberg(f, a, b)
value = rom.integrate(dimension = 1, iterations = 5, precision = TRESHOLD_PRECISION)
print(f"Valeur de la fonction (romberg): {value}")