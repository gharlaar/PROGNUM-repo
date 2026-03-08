#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import sin, cos, pi, exp
import scipy
from scipy.integrate import quad

#defining the function

function= input("Enter a function: ") 
def f(x):
    try: 
        return eval(function) 
    except NameError:
        print(f"Unknown function or variable used.")
    except SyntaxError:
        print (f"Invalid syntax used.")
    except IndexError:
        print(f"The sequence subscript is out of range.")
    except TypeError:
        print(f"An operation or function is applied to an object of inappropriate type.")
    except ValueError:
        print(f"An operation or function recieved an argument of the right type but it has an inappropriate value.")
    except Exception as exc:
        print(f"Error in evaluating the expression: {exc}.")
    
#Defining the bounds of the integrals
x_low = 0
x_up = pi

#Calculating the integral using quad
area = scipy.integrate.quad(f, x_low, x_up)
print(f"So the area and its error calculated using the quad function is {area}.")

#Calculating the error using Monte Carlo
#Creating the Gaussian distributions
#From PLS, I assume these errors hava a Gaussian distribution
N = 10000
def MonteCarlo(f, x_low, x_up, N):
    try:
        x = np.random.uniform(0, pi, N)
        y = np.array([f(xi) for xi in x])
        integral = (x_up - x_low) * np.mean(y)
        error = ((x_up - x_low) * np.std(y)) / np.sqrt(N)
    
        return integral, error
    except NameError:
        print(f"Unknown function or variable used.")
    except SyntaxError:
        print (f"Invalid syntax used.")
    except IndexError:
        print(f"The sequence subscript is out of range.")
    except TypeError:
        print(f"An operation or function is applied to an object of inappropriate type.")
    except ValueError:
        print(f"An operation or function recieved an argument of the right type but it has an inappropriate value.")
    except Exception as exc:
        print(f"Error in evaluating the expression: {exc}.")
    
area_MonteCarlo = MonteCarlo(f, x_low, x_up, N)
print(f"The area and its error determined by using Monte Carlo is {area_MonteCarlo}.")



# In[2]:


import sympy as sp

x = sp.Symbol('x')  #defining x

f = x**4 + sp.exp(sp.sin(x) + sp.cos(x))  #defining the formula
integral = sp.integrate(f, (x, 0, sp.pi))  #calculating the integral
integral_value = integral.evalf()  #Evaluating the value of the integral

print(f"So the value of the integral is {integral_value}.")



# In[ ]:




