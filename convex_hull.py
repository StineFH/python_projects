#a
from random import random
 
def random_points(n):
    assert 1 <= n <=100, "n is not 1<= n <=100 as required"
    return([(round(random(), 3), round(random(), 3)) for i in range(n)])  

#b 
import matplotlib.pyplot as plt

def plot_hull(points, polygon):
    x_points, y_points = map(list, (zip(*points)))
    polygon.append(polygon[0])
    x_poly, y_poly = map(list, (zip(*polygon))) 
        
    plt.plot(x_points, y_points, "go") # plotting points 
    plt.plot(x_poly, y_poly, "r-") # plotting polygon
    plt.plot(x_poly, y_poly, "ro") # Making points on polygon red 
    plt.show()
    
#c
def left_turn(p, q, r):
    return (q[0]-p[0]) * (r[1]-p[1]) - (r[0]-p[0]) * (q[1]-p[1]) >= 0

example_1 = [(0.112, 0.113), (0.487, 0.435), (0.665, 0.2), (0.313, 0.346), (0.166, 0.886), (0.998, 0.623), (0.805, 0.296), (0.446, 0.783), (0.653, 0.774), (0.146, 0.033)]

def convex_hull(points): 
    """Convex Hull Constructor
    Examples:
    >>> sorted(convex_hull(example_1))
    [(0.112, 0.113), (0.146, 0.033), (0.166, 0.886), (0.653, 0.774), (0.665, 0.2), (0.805, 0.296), (0.998, 0.623)]
    """
    # Computing upper hull       
    start, towards, testing = 0, 1, 2
    s_points = sorted(points)
    sh = [s_points[0], s_points[1]]
    
    while testing <= len(s_points)-1:
        if left_turn(s_points[start], s_points[towards], s_points[testing]):
            sh.pop()   
            if start == 0: 
                towards += 1
                testing += 1
                sh.append(s_points[towards])
            else: 
                start = s_points.index(sh[-2])
                towards = s_points.index(sh[-1])
        else: 
            sh.append(s_points[testing])
            start = towards 
            towards = testing
            testing += 1                 
    
    #Computing lower hull 
    start, towards, testing = 0, 1, 2
    rev_points = s_points[::-1] # Doing the same on the reversed list of points
    sh.append(rev_points[1])
    
    while testing <= len(rev_points)-1:
        if left_turn(rev_points[start], rev_points[towards], rev_points[testing]):
            sh.pop()   
            if start == 0 and towards == 1: # Only difference between two loops 
                towards += 1
                testing += 1
                sh.append(rev_points[towards])
            else: 
                start = rev_points.index(sh[-2])
                towards = rev_points.index(sh[-1])
        else: 
            sh.append(rev_points[testing])
            start = towards 
            towards = testing
            testing += 1
         
    sh.pop() #removing the last point so it does not appear twice      
    return(sh)

    
# Testing 
points = random_points(48)        
polygon = convex_hull(points)  
plot_hull(points, polygon)                   
