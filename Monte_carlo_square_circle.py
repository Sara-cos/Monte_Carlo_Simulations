# Square and Circle area and pi founding using random sampling and evaluations
# Zero be the mid(origin) of whole setup
# Let R be the Radius, thus extereme points lies between -Radius and Radius

# We calculate the ratio of area of circle to area of square, the result would be equal to pi/4

import numpy as np # import numpy for getting random integers

def MC_Simualtion():
    Radius = 0.5 # Sample radius of 0.5
    Circle = 0
    Big_Square = 0
   
    for i in range(10000000): # 10000000 points in total for testing
        x = np.random.uniform(-Radius,Radius) # Random points from -radius to radius to include all 4 quadrants
        y = np.random.uniform(-Radius,Radius) # of x and y

        #Distance between the coodinate and origin should be <= 0.5
        Distance = (np.sqrt(y**2 + x**2)) # Distance of all the points from the origin

        if(Distance <= Radius): # Check if point lies inside or outside the circle
            Circle = Circle + 1
        else:
            Big_Square = Big_Square + 1

    # Take the ratio of circle with the points that lie outside the circle ie total number of points
    Ratio_Big_Square = Circle/10000000
    print("Circle : {}".format(Circle))
    print("Square : {}".format(10000000))

    ## We get the Ratio_Big_Square as pi/4 so we multiply it by 4

    Ratio =  4*Ratio_Big_Square

    return Ratio

Result = MC_Simualtion()
print(Result)
