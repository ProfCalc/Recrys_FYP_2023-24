import numpy as np
import main
import random

n1 = 50  ### Number of X which should be used for avg 
n2 = 50 ### Number of Y which should be used for avg 



def average_grain_x(n1):
    random_y = random.sample(range(0,main.c),n1)
    subgrains =[]
    for y in random_y:
        i=0
        for x in range (0,main.r):
            if main.s[x,y,3] < 0.1 or main.s[x+1,y,3] < 0.1:
                pass
            elif 0< np.degrees(main.theta(np.matmul(main.G[x,y,0],main.G[x+1,y,1]))) < 15:
                i+=1
        subgrains.append(i)
        
    return sum(subgrains)/(n1*main.r*main.stepsize_x)
    
def average_grain_y(n2):
    random_x = random.sample(range(0,main.r),n2)
    subgrains =[]
    for x in random_x:
        i=0
        for y in range (0,main.c):
            if main.s[x,y,3] < 0.1 or main.s[x,y+1,3] < 0.1:
                pass
            elif 0 < np.degrees(main.theta(np.matmul(main.G[x,y,0],main.G[x,y+1,1]))) < 15:
                i+=1
        subgrains.append(i)
        
    return sum(subgrains)/(n2*main.c*main.stepsize_y)

if __name__ == "__main__":
    f = open("grain_size.txt", "w" )
    f.write("Avg Grain X = %s \n"%(average_grain_x(n1)))
    f.write("Avg Grain Y = %s \n"%(average_grain_y(n2)))