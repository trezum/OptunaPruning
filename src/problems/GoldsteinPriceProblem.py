from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi

from Problem import Problem

class GoldsteinPrice(Problem):
  
  def __init__(self):
    pass

  def direction(self):
    return 'minimize'

  def name(self):
    return 'goldstein_price'
  
  def xmax(self):
    return 2
  
  def xmin(self):
    return -2
  
  def ymax(self):
    return 2
  
  def ymin(self):
    return -2

  def eval(self, x, y):
    return (1+(x+y+1)**2*(19 - 14*x +3*x**2-14*y+6*x*y+3*y**2))*(30+(2*x-3*y)**2*(18-32*x+12*x**2+48*y-36*x*y+27*y**2))
