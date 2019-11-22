import math

class Romberg():
  def __init__(self, f, x_0, x_n):
    self.f = f
    self.x_0 = x_0
    self.x_n = x_n
  
  def integrate(self, precision):
    r = [trapezes(0, 1)]
    for k in range(2, 20):
      r_new = [trapezes(r[0], k)]
      for i in range(1, k):
        r_new.append(richardson_extrapolation(r[i-1], r_new[i-1], 2*i))
      
      if abs(r[-1] - r_new[-1] < precision):
        return r[-1], k
      
      r = r_new

  def richardson_extrapolation(self):
    pass

  def trapezes(self, old_integral, k):
    # si k = 1, le nombre de trapèzes serait de 1 (en effet, 2^0 = 1)
    if k == 1: 
      return ((self.f(self.x_0) + self.f(self.x_n)) * ((x_n - x_0)) / 2)

    # nombre de trapèzes
    n = int(math.pow(2, k-1))
    # intervalle h
    h = (x_n - x_0) / n

    sum = 0
    # on démarre à x_1
    x = x_0 + h
    for i in range(n):
      sum += f(x)
      x += h
    return old_integral/2 + (h/2) * sum