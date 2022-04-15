from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi

from Problem import Problem

class Ackley(Problem):
  
  def __init__(self):
    pass

  def name(self):
    return 'ackley'

  def eval(self,x, y):
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * 
    pi * x)+cos(2 * pi * y))) + e + 20
