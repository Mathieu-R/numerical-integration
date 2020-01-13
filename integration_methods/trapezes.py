import matplotlib.pyplot as plt
import numpy as np
import math

# méthode des trapèzes
# on note l'aire d'une petite surface approximée : W_i
# on approxime la fonction par une somme de trapèzes.
# Aire d'un trapèze : A = [(B+b)*h]/2 ; W_i = [(f(x_i) + f(x_{i+1}))*h]/2
# I = sum_{i=0}^{n-1} W_i
#   = h/2 * sum_{i=0}^{n-1} (f(x_i) + f(x_{i+1}))
#   = h/2 * f(x_0) + 2 * sum_{i=1}^{n-1} f(x_{i}) + f(x_n)
# I_n = I_{n-1} / 2 + h/2 * sum{i=0}^{n} f(x_i)

class Trapezes():
  def __init__(self, f, x_0, x_n):
    self.f = f
    self.x_0 = x_0
    self.x_n = x_n
  
  # borne inférieure : x_0
  # borne supérieure : x_n
  # en pratique on itère sur la méthode 
  # et on diminue le pas h progressivement (de 1/2 à chaque itération)
  # k : itération en cours
  def trapezes(self, old_integral, k):
    # si k = 1, le nombre de trapèzes serait de 1 (en effet, 2^0 = 1)
    if k == 1: 
      # Aire d'un trapèze
      h = (self.x_n - self.x_0)
      return (self.f(self.x_0) + self.f(self.x_n)) * h / 2

    # nombre de trapèzes
    n = int(math.pow(2, k-1))
    # intervalle h
    h = (self.x_n - self.x_0) / n

    sum = 1/2 * (self.f(self.x_0) + self.f(self.x_n))
    for i in range(1, n):
      x_i = self.x_0 + (i * h)
      sum += self.f(x_i)

    return h * sum 
  
  # N : nombre de dimensions
  def integrate(self, N, iterations, precision):
    new_integral = 0
    for k in range(1, iterations):
      old_integral = new_integral
      new_integral = self.trapezes(old_integral, k)
      if abs(old_integral - new_integral) < precision and k > 1:
        return new_integral, k
        break