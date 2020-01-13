from integration_methods.trapezes import Trapezes
from integration_methods.romberg import Romberg
from integration_methods.monte_carlo import Monte_Carlo

import math

# precision de l'évaluation numérique de l'intégrale (trapèzes)
TRESHOLD_PRECISION = 1e-9
DIMENSIONS = [1] #[1, 2, 10, 15]
X_0 = -3 
X_N = 3

# intégrer une gausssienne à N dimensions : I_N = int_[-3, 3]^N exp(-\vec{x}^2/2)dx

def gaussian(x):
  f = math.exp(-(x**2) / 2)
  return f

def gaussian_2_dim(x, y):
  return math.exp(-(x**2 + y**2) / 2)

def gaussian_theo(N):
  return math.sqrt((2*math.pi)**N)

def evaluate_gaussian_integral():

    print(f"dimension 1")
    print("-------------")
    print(f"Valeur théorique approximative: {gaussian_theo(N=1)}")

    # trapèzes
    gaussian_trapezes = Trapezes(gaussian, X_0, X_N)
    gaussian_trapezes_value = gaussian_trapezes.integrate(iterations = 20, precision = TRESHOLD_PRECISION)
    print(f"Valeur de la gaussienne à 1 dimension (trapèzes): {gaussian_trapezes_value}")

    # romberg
    gaussian_romberg = Romberg(gaussian, X_0, X_N)
    gaussian_romberg_value = gaussian_romberg.integrate(iterations = 20, precision = TRESHOLD_PRECISION)
    print(f"Valeur de la gaussienne à 1 dimension (romberg): {gaussian_romberg_value}")

    print(f"dimension 2")
    print("-------------")
    print(f"Valeur théorique approximative: {gaussian_theo(N=2)}")

    def Fx_trapeze(y):
      def f(x):
        return gaussian_2_dim(x, y)
      integral, _ = Trapezes(f, X_0, X_N).integrate(iterations=10, precision=TRESHOLD_PRECISION)
      return integral

    gaussian_trapezes = Trapezes(Fx_trapeze, X_0, X_N)
    gaussian_trapezes_value = gaussian_trapezes.integrate(iterations = 10, precision = TRESHOLD_PRECISION)
    print(f"Valeur de la gaussienne à 2 dimension (trapèzes): {gaussian_trapezes_value}")

    def Fx_romberg(y):
      def f(x):
        return gaussian_2_dim(x, y)
      integral, _ = Romberg(f, X_0, X_N).integrate(iterations=10, precision=TRESHOLD_PRECISION)
      return integral

    # romberg
    gaussian_romberg = Romberg(Fx_romberg, X_0, X_N)
    gaussian_romberg_value = gaussian_romberg.integrate(iterations = 10, precision = TRESHOLD_PRECISION)
    print(f"Valeur de la gaussienne à 2 dimension (romberg): {gaussian_romberg_value}")

    # en pratique, ces 2 méthodes deviennent moins efficace si la dimension devient plus grande que 2
    # car il faudrait embriquer un tas de fonctions.
    # Solution : La méthode de Monte Carlo, elle converge moins rapidement mais au moins 

    print("Monte Carlo (pratique pour des dimensions > 2)")
    print("-------------")

  #for dimension in DIMENSIONS:
    # # monte-carlo
    # gaussian_monte_carlo = Monte_Carlo(gaussian, X_0, X_N)
    # gaussian_monte_carlo_value = gaussian_monte_carlo.integrate(iterations = 10000)
    # print(f"Valeur de la gaussienne à {dimension} dimension (monte-carlo): {gaussian_monte_carlo_value}")

evaluate_gaussian_integral()