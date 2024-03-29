
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
        from matplotlib import ticker
        from matplotlib.colors import LogNorm
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
        plt.savefig(save_results_to + self.name() + '_surface.png', dpi = 500)
        plt.close()

        fig,ax=plt.subplots(1,1)
        #lvls = np.logspace(0,4,20)
        #cp = ax.contourf(x,y,results,20, cmap=plt.cm.coolwarm,extend='both')
        
        #cp = ax.contourf(x,y,results, locator=ticker.LogLocator(base=10))
        cp = ax.contourf(x,y,results, locator=ticker.MaxNLocator(nbins=20))
        #cp = ax.contourf(x,y,results, levels=20)
        #cp = ax.contourf(x,y,results, levels=[0,0.01,0.1,1,2,4,8,16,32,64,128,256]) #, levels=20
        fig.colorbar(cp)
        plt.savefig(save_results_to + self.name() + '_contour.png', dpi = 500)
        plt.close()
        print(self.name() + ' drawn')