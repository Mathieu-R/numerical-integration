import numpy as np
import math

class Romberg():
  def __init__(self, f, x_0, x_n):
    self.f = f
    self.x_0 = x_0
    self.x_n = x_n

  def trapezes(self, k):
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

  def richardson_extrapolation(self, I_prev, I_current, k):
    return ((2**k * I_current) - I_prev) / (2**k - 1)

  def integrate(self, iterations, precision):
    # R(n, m)
    self.map = np.zeros((iterations, iterations))

    """
    iterations = 3
       j
       __________________
    i | trap   x    x    |
      | trap rich   x    |
      | trap rich approx |  
       ------------------
    """
    for i in range(1, iterations):
      i_prime = i - 1
      # Méthode des trapèzes
      self.map[i_prime, 0] = self.trapezes(i)
      for j in range(1, i):
        # Extrapolation de Richardson
        self.map[i_prime, j] = self.richardson_extrapolation(self.map[i_prime-1, j-1], self.map[i_prime, j-1], 2*j)
      
      if abs(self.map[i_prime - 1, i_prime - 1] - self.map[i_prime, i_prime]) < precision:
        return self.map[i_prime, i_prime], i
        break
    