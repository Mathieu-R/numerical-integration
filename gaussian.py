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
  f = math.exp(-(x**2)/2)
  return f

def gaussian_theo(N):
  return math.sqrt((2*math.pi)**N)

def evaluate_gaussian_integral():
  for dimension in DIMENSIONS:

    print(f"Valeur théorique approximative: {gaussian_theo(dimension)}")

    # trapèzes
    gaussian_trapezes = Trapezes(gaussian, X_0, X_N)
    gaussian_trapezes_value = gaussian_trapezes.integrate(dimension = dimension, iterations = 20, precision = TRESHOLD_PRECISION)
    print(f"Valeur de la gaussienne à {dimension} dimension (trapèzes): {gaussian_trapezes_value}")

    # romberg
    gaussian_romberg = Romberg(gaussian, X_0, X_N)
    gaussian_romberg_value = gaussian_romberg.integrate(dimension = dimension, iterations = 20, precision = TRESHOLD_PRECISION)
    print(f"Valeur de la gaussienne à {dimension} dimension (romberg): {gaussian_romberg_value}")

    # # monte-carlo
    # gaussian_monte_carlo = Monte_Carlo(gaussian, X_0, X_N)
    # gaussian_monte_carlo_value = gaussian_monte_carlo.integrate(iterations = 10000)
    # print(f"Valeur de la gaussienne à {dimension} dimension (monte-carlo): {gaussian_monte_carlo_value}")

evaluate_gaussian_integral()