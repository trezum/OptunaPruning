from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import meshgrid
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os

graph_name = 'ackley'

save_results_to = os.path.dirname(os.path.abspath(__file__)) + '/plots/' + graph_name + '/'
if not os.path.exists(save_results_to):
    os.makedirs(save_results_to)

def objective(x, y):
 return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * 
  pi * x)+cos(2 * pi * y))) + e + 20


r_min, r_max = -32.768, 32.768
xaxis = arange(r_min, r_max, 2)
yaxis = arange(r_min, r_max, 2)
x, y = meshgrid(xaxis, yaxis)
results = objective(x, y)
figure = plt.figure()
axis = plt.axes( projection='3d')

axis.plot_surface(x, y, results, cmap='jet', shade= "false")
plt.savefig(save_results_to + graph_name + '_surface.png', dpi = 300)
plt.close()

#plt.contour(x,y,results)
fig,ax=plt.subplots(1,1)
cp = ax.contourf(x,y,results)
fig.colorbar(cp) # Add a colorbar to a plot
plt.savefig(save_results_to + graph_name + '_contour.png', dpi = 300)
plt.close()

# plt.scatter(x, y, results)
# plt.savefig(save_results_to + graph_name + '_scatter.png', dpi = 300)
# plt.close()
print('Done')