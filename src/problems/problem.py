
class Problem:

    def __init__(self):
        pass

    def name(self):
        raise NotImplementedError

    def eval(x, y):
        raise NotImplementedError

    def xmax(self):
        raise NotImplementedError
    
    def xmin(self):
        raise NotImplementedError
    
    def ymax(self):
        raise NotImplementedError
    
    def ymin(self):
        raise NotImplementedError

    def draw(self):
        import matplotlib
        matplotlib.use('agg')
        import matplotlib.pyplot as plt
        from numpy import arange
        from numpy import meshgrid
        import os

        save_results_to = os.path.dirname(os.path.abspath(__file__)) + '/plots/'
        if not os.path.exists(save_results_to):
            os.makedirs(save_results_to)
        
        xaxis = arange(self.xmin(), self.xmax(), 0.1)
        yaxis = arange(self.ymin(), self.ymax(), 0.1)
        x, y = meshgrid(xaxis, yaxis)
        results = self.eval(x, y)
        axis = plt.axes( projection='3d')

        axis.plot_surface(x, y, results, cmap='jet', shade= "false")
        plt.savefig(save_results_to + self.name() + '_surface.png', dpi = 300)
        plt.close()

        fig,ax=plt.subplots(1,1)
        #cp = ax.contourf(x,y,results,20, cmap=plt.cm.coolwarm,extend='both')
        cp = ax.contourf(x,y,results, 20)
        fig.colorbar(cp)
        plt.savefig(save_results_to + self.name() + '_contour.png', dpi = 300)
        plt.close()