from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi

from Problem import Problem

class Booth(Problem):
  
  def __init__(self):
    pass

  def direction(self):
    return 'minimize'

  def name(self):
    return 'booth'
  
  def xmax(self):
      return 10
  
  def xmin(self):
    return -10
  
  def ymax(self):
    return 10
  
  def ymin(self):
    return -10

  def eval(self,x, y):
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2
