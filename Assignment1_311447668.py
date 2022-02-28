###############################
## Assignment 1 
## Dvir David Iluz
## 311447668
###############################

import math

# A. 

def my_func(x1,x2,x3):
    try:
        if not isinstance(x1,float) or not isinstance(x2,float) or not isinstance(x3,float):
            raise TypeError
        counter = (x1+x2+x3)*(x1+x2)*x3        
        denominator = x1+x2+x3
        answer = counter/denominator
        return answer
    except ZeroDivisionError:
        return "Not a number - denominator equals zero"
    except TypeError:
        return "Error: parameters should be double"

# B. 

def convert(hours, minutes=0):
    s = 60 
    if hours < 0 or minutes < 0:
        return "Input error!"
    else: 
        seconds = hours*s*s + minutes*s
    return seconds
