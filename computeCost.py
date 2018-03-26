import numpy as np

def computeCost(X, y, theta):
    """
       computes the cost of using theta as the parameter for linear 
       regression to fit the data points in X and 
    """
    
    m = y.size
    J = 0
    s = 0
    X = np.ones((m, 1))
    theta = np.zeros(2, 1)
    s = np.power(( X.dot(theta)) - np.transpose(([y]), 2))
    J = (1.0/(2 * m)) * np.sum(s, axis=0)
    iterations = 10
    alpha = 0.01

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
#               You should set J to the cost.


# ========================================================================
    return J




#'''X = [ones(m, 1), data(:,1)]; ''' % Add a column of ones to x'''
#theta = zeros(2, 1); '''% initialize fitting parameters'''
#iterations = 1500;
##alpha = 0.01;
