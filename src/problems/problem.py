from numpy import arange
from numpy import meshgrid
import matplotlib.pyplot as plt
import os


class problem:

    def name(self):
        return 'problem'

    def objective(self, x, y):
        pass

    def draw(self):
        
        save_results_to = os.path.dirname(os.path.abspath(__file__)) + '/plots/' + self.name() + '/'
        if not os.path.exists(save_results_to):
            os.makedirs(save_results_to)
        
        r_min, r_max = -32.768, 32.768
        xaxis = arange(r_min, r_max, 0.25)
        yaxis = arange(r_min, r_max, 0.25)
        x, y = meshgrid(xaxis, yaxis)
        results = self.objective(x, y)
        figure = plt.figure()
        axis = plt.axes( projection='3d')

        axis.plot_surface(x, y, results, cmap='jet', shade= "false")
        plt.savefig(save_results_to + self.name() + '_surface.png', dpi = 300)
        plt.close()

        fig,ax=plt.subplots(1,1)
        cp = ax.contourf(x,y,results)
        fig.colorbar(cp)
        plt.savefig(save_results_to + self.name() + '_contour.png', dpi = 300)
        plt.close()