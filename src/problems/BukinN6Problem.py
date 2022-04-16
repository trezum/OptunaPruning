from numpy import fabs
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi

from Problem import Problem

class BukinN6(Problem):
  
  def __init__(self):
    pass

  def direction(self):
    return 'minimize'

  def name(self):
    return 'bukin_n6'
  
  def xmax(self):
    return -5
  
  def xmin(self):
    return -15
  
  def ymax(self):
    return 3
  
  def ymin(self):
    return -3

  def eval(self, x, y):
    return 100* sqrt(fabs(y - 0.01 * x**2)) + 0.01 * fabs( x+ 10)
