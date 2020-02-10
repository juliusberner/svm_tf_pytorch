__all__ = ['get_line', 'plot']

def get_line(W, b, x):
    return (-W[0]*x+b)/W[1]

def plot(X, Y, W=None, b=None):
    x1_min, x1_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    x2_min, x2_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    x1 = np.arange(x1_min, x1_max, .02)
    xx1, xx2 = np.meshgrid(x1, np.arange(x2_min, x2_max, .02))
    if W is not None and b is not None:
        decision = np.c_[xx1.ravel(), xx2.ravel()] @ W + b
        plt.contourf(xx1, xx2, decision.reshape(xx1.shape), cmap=plt.cm.RdBu, alpha=.8)
        plt.colorbar()
        for intercept in [-1,0,1]:
            plt.plot(x1, get_line(W, b + intercept, x1), c='black')
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    plt.scatter(X[:,0],X[:,1], c=Y.ravel(), cmap=cm_bright)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.show()
