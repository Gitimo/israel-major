import numpy
V_water = 5*pow(10,-3)
n_water = V_water * 55.6
n_zinc = 400*pow(10,-9)* n_water
print n_zinc/n_water * 100

A_sample = 0.035 * 0.011
A_cell = 3.25 * pow(10,-20)* 5.2
n_cell = A_sample / A_cell
print n_cell
