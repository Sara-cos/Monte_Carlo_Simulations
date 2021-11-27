# Square and Circle area and pi founding using random sampling and evaluations
# Zero be the mid(origin) of whole setup
# Let R be the Radius, thus extereme points lies between -Radius and Radius

import numpy as np

def MC_Simualtion():
    Radius = 0.5
    Circle = 0
    Big_Square = 0
   
    for i in range(1000000):
        x = np.random.uniform(-Radius,Radius)
        y = np.random.uniform(-Radius,Radius)

        #Distance between the coodinate and origin should be <=5
        Distance = (np.sqrt(y**2 + x**2))

        if(Distance <= Radius):
            Circle = Circle + 1
        else:
            Big_Square = Big_Square + 1

    Big_Square = Circle + Big_Square

    Ratio_Big_Square = Circle/Big_Square
    print("Circle : {}".format(Circle))
    print("Square : {}".format(Big_Square))

    ## As the Big_Square is Basically 4 times the Small Square area

    Ratio =  4*Ratio_Big_Square

    return Ratio

Result = MC_Simualtion()
print(Result)




