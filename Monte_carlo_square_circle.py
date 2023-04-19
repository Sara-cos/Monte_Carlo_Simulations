# Square and Circle area and pi founding using random sampling and evaluations
# Zero be the mid(origin) of whole setup
# Let R be the Radius, thus extereme points lies between -Radius and Radius

# We calculate the ratio of area of circle to area of square, the result would be equal to pi/4

import numpy as np # import numpy for getting random integers

def MC_Simualtion():
    Radius = 0.5 # Sample radius of 0.5
    Circle = 0 # Counter for the points that lie inside the circle
    Big_Square = 0 # Counter for the total points inside the square
    Total_points = 10000000 # 10000000 points in total for testing

    # Generate random points and check if they lie inside the circle
    for i in range(Total_points): 
        x = np.random.uniform(-Radius,Radius) # Random points from -radius to radius to include all 4 quadrants of x and y
        y = np.random.uniform(-Radius,Radius) 

        # Distance between the coordinate and origin should be <= 0.5
        Distance = (np.sqrt(y**2 + x**2)) # Calculate the distance of all the points from the origin

        if(Distance <= Radius): # Check if point lies inside or outside the circle
            Circle = Circle + 1

        Big_Square = Big_Square + 1 # Increment the counter for the total points inside the square

    # Take the ratio of circle with the points that lie outside the circle ie total number of points
    Ratio_Big_Square = Circle/Big_Square
    print("Circle : {}".format(Circle))
    print("Square : {}".format(Big_Square))

    ## We get the Ratio_Big_Square as pi/4 so we multiply it by 4, to get the pi value
    Ratio =  4*Ratio_Big_Square

    return Ratio

Result = MC_Simualtion()
print(Result)
