import matplotlib.pyplot as plt
import numpy as np
import math

# precision de l'évaluation numérique de l'intégrale
TRESHOLD_PRECISION = 1e-6

# intégrer une gausssienne à N dimensions : I_N = int_[-3, 3]^N exp(-\vec{x}^2/2)dx

# méthode des trapèzes
# on note l'aire d'une petite surface approximée : W_i
# on approxime la fonction par une somme de trapèzes.
# Aire d'un trapèze : A = [(B+b)*h]/2 ; W_i = [(f(x_i) + f(x_{i+1}))*h]/2
# I = sum_{i=0}^{n-1} W_i
#   = h/2 * sum_{i=0}^{n-1} (f(x_i) + f(x_{i+1}))
#   = h/2 * f(x_0) + 2 * sum_{i=1}^{n-1} f(x_{i}) + f(x_n)
# I_n = I_{n-1} / 2 + h/2 * sum{i=0}^{n} f(x_i)

# borne inférieure : x_0
# borne supérieure : x_n
# en pratique on itère sur la méthode 
# et on diminue le pas h progressivement
def trapezes(f, x_0, x_n, old_integral, k):
  # si k = 1, le nombre de trapèzes serait de 1 (en effet, 2^0 = 1)
  if k == 1: 
    return ((f(x_0) + f(x_n))*(x_n - x_0)) / 2

  # nombre de trapèzes
  n = int(math.pow(2, k-1))
  # intervalle h
  h = (x_n - x_0) / n

  sum = 0
  # on démarre à x_1
  x = x_0 + h
  for i in range(0, n):
    sum += f(x)
    x += h
  return old_integral/2 + (h/2) * sum
  
# N : nombre de dimensions
def compute_trapezes(N, iterations):
  new_integral = 0
  for k in range(1, iterations):
    old_integral = new_integral
    new_integral = trapezes(gausssienne, -3, 3, old_integral, k)
    if abs(old_integral - new_integral) < TRESHOLD_PRECISION and k > 1:
      print(f"valeur de la gaussienne à une dimension entre -3 et 3: {new_integral} après {k} itérations")
      print(f"devrait +/- ètre égale à: {math.sqrt((2*math.pi)**N)}")
      break

def richardson_extrapolation():
  pass

def romberg(f, x_0, x_n):
  r = [trapezes(f, x_0, x_n, 0, 1)]
  for k in range(2, 20):
    r_new = [trapezes(f, x_0, x_n, r[0], k)]
    for i in range(1, k):
      r_new.append(richardson_extrapolation(r[i-1], r_new[i-1], 2*i))
    
    if abs(r[-1] - r_new[-1] < TRESHOLD_PRECISION):
      return r[-1], k
    
    r = r_new


def gausssienne(x):
  f = math.exp(-(x**2)/2)
  return f

compute_trapezes(N = 1, iterations = 10000)
