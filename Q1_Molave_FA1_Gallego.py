import math

#Ask users the coordinates they want to use for the formula.

x1 = int(input("Enter your first x-coordinate:"))
y1 = int(input("Enter your first y-coordinate:"))
x2 = int(input("Enter your second x-coordinate:"))
y2 = int(input("Enter your second y-coordinate:"))

#Computes the distance using the distance formula.
distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)) 

#Rounds the distance to two decimal places.
rounded_distance = round( distance, 2)

#Prints the result rounded to to decimal places.
print( "The distance between (", x1,",", y1, ") and (", x2,",", y2, ") is ", rounded_distance )

"""Reflection:The math library helped me to simplify my  program because it takes less time to code, i think. functions like sqrt and pow were easier to use because you dont need more symbols. """