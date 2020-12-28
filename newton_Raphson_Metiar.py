


import random
import math
from sympy import *

def f(x):
    return x**2+1

def derivative_func(expr,x):
    """[This function will find the derivative expr]

    Args:
        expr ([sympy.core.add]): [The orginal expr]
        x ([type]): [X symbol in expr]

    Returns:
        [sympy.core.add]: [The derivative_expr ]
    """
    
    expr_diff = diff(expr, x)
    return expr_diff

def Expr_to_numrical_value(expr,num):
    """[This function will set a value in x in the Original expression ]

    Args:
        expr ([sympy.core.add]): [The orginal expr]
        num ([float]): [set value]

    Returns:
        [float]: [The value of the expr after setting the num in]
    """
    return expr.subs({x:num})

def derivative_Expr_to_numrical_value(derivative_expr,num):
    """[This function will set a value in x in the Original expression ]

    Args:
        expr ([sympy.core.add]): [The derivative_expr]
        num ([float]): [set value]

    Returns:
        [float]: [The value of the expr after setting the num in]
    """
    return derivative_expr.subs({x:num})

def tangent_Formula(num,expr,derivative_expr): #Xr+1=Xr-(f(Xr)/f'(Xr))
    """[summary]

    Args:
        Xr ([int]): [The last value]
        expr ([sympy.core.add]): [The main expression]
        derivative_expr ([sympy.core.add]): [The derivative_expr]

    Returns:
        [int]: [The next X value]
    """
    numerator = Expr_to_numrical_value(expr,num)

    denominator = derivative_Expr_to_numrical_value(derivative_expr,num)
 
    new_Xr = num-(numerator/denominator)
    
    return new_Xr  

def newton_Raphson(expr,derivative_expr,start_point,end_point,eps):
    value = start_point
    
    while start_point<end_point:
        
        new_value = value+eps
        if Expr_to_numrical_value(expr,value)>0:
            if Expr_to_numrical_value(new_value)>0:
                print("No roots in section")
                value = new_value
            if Expr_to_numrical_value(new_value)<0:
                first_Xr = start_point+eps
                next_Xr = tangent_Formula(first_Xr,expr,derivative_expr)
                while (next_Xr-first_Xr>eps):
                    first_Xr = next_Xr
                    next_Xr = tangent_Formula(first_Xr,expr,derivative_expr) 
                    
                print("Root:{} ".format(next_Xr))
                                    
        if Expr_to_numrical_value(expr,value)<0:
            if Expr_to_numrical_value(expr,new_value)<0:
                print("No roots in section")
                value = new_value
            if Expr_to_numrical_value(expr,new_value)>0:
                first_Xr = start_point+eps
                next_Xr = tangent_Formula(first_Xr,expr,derivative_expr)
                while next_Xr-first_Xr>eps:
                    first_Xr = next_Xr
                    next_Xr = tangent_Formula(first_Xr,expr,derivative_expr) 
                    
                print("Root:{} ".format(next_Xr))
                
        start_point+=eps

def MeitarMethod(f, xn_1, xn, eps=0.001):

    d=2*eps #first guess
    count=0
    while abs(d) >eps:
        count=count+1
        d = (xn - xn_1) / (f(xn) - f(xn_1)) * f(xn)
        xn_1 = xn
        xn = xn - d

    print(count, "iteration to find root (", xn, ", 0 )")
    return

print("~ MEITAR METHOD ~")
print("function: x**3 -math.cos(x)")
MeitarMethod(lambda x: x**3 -math.cos(x), 1, 2)
    
print("~ newton_Raphson Method ~")
x = Symbol('x')
expr = x**3+x**2-4*x
start_point = -3
end_point = 2
derivative_expr = derivative_func(expr,x)
newton_Raphson(expr,derivative_expr,-3,2,0.5)








	

