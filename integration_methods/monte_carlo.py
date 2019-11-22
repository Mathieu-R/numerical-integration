import matplotlib.pyplot as plt
import numpy as np 
import random 
import math 

from IPython.display import clear_output

class Monte_Carlo():
  def __init__(self, f, x_0, x_n):
    self.f = f
    self.x_0 = x_0
    self.x_n = x_n
    self.iterations = iterations
    
  def random_number(self, min, max):
      range = max - min
      choice = random.uniform(0,1)
      return min + (range * choice)

  def integrate(self, iterations):
    sum = 0
    for i in range(iterations):
      # on tire un nombre
      # présent dans l'intervalle d'intégration
      a = self.random_number(self.x_0, self.x_n)
      # on évalue l'intégrale en ce point
      f_value = self.f(a)
      sum += f_value

    # théorème de la moyenne : f_avg = 1/(b-a) * int(f) <=> int(f) = (b-a)*f_avg
    f_avg = sum / iterations
    estimated_integral = (self.x_n - self.x_0) * f_avg
    return estimated_integral

  def variance(self, iterations):
    # moyenne des carrés
    tot_f_square = 0
    for k in range(iterations):
      # on évalue à nouveau la fonction
      # à un point random dans l'intervalle d'intégration
      x_k = self.random_number(0, self.x_n)
      tot_f_square += math.pow(self.f(x_k), 2)
    avg_square = ((self.x_n - self.x_0) / iterations) * tot_f_square

    # carré des moyennes
    tot_f = 0
    for k in range(iterations):
      # on évalue à nouveau la fonction
      # à un point random dans l'intervalle d'intégration
      x_k = self.random_number(0, self.x_n)
      tot_f += self.f(x_k)
    square_avg = math.pow((((self.x_n - self.x_0) / iterations) * tot_f), 2)

    sigma_square = avg_square - square_avg
    return sigma_square