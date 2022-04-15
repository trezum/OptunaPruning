from numpy import fabs
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi

from Problem import Problem

class Beale(Problem):
  
  def __init__(self):
    pass

  def direction(self):
    return 'minimize'

  def name(self):
    return 'Beale'
  
  def xmax(self):
      return -4.5
  
  def xmin(self):
    return -4.5
  
  def ymax(self):
    return 4.5
  
  def ymin(self):
    return -4.5

  def eval(self, x, y):
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
