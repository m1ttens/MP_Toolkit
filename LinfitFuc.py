import numpy as np 

def Linfit(x,y):

    #Calculating the gradient and y intercept
    x = np.asarray(x)
    y = np.asarray(y)
    
    m, c = np.polyfit(x, y, 1)
    print("Gradient =", m)
    print("Y-Intercept =", c)

    #Calculating the gradient and y intercept error 
    n = len(x)
    D = sum(x**2) - 1./n * sum(x)**2
    x_bar = np.mean(x)
    p_coeff, residuals, _, _, _ = np.polyfit(x, y, 1, full=True)
    dm_squared = 1./(n-2)*residuals/D 
    dc_squared = 1./(n-2)*(D/n + x_bar**2)*residuals/D
    print("Gradient Erorr =" , np.sqrt(dm_squared))
    print("Y-Intercept" , np.sqrt(dc_squared))

