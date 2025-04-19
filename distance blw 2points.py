def calculate_distance(x1,y1,x2,y2):
    """
    calculate the distance between two points (X1,Y1)and(x2,y2).
    :param x1:X-coordinate of the first point(float or int).
    :param y1:y-coordinate of the first point(float or int).
    :param x2:x-coordinate of the secound point(float or int).
    :param y2:y-coordinate of the secound point(float or int).
    :return:The distance between the two points(float).
    """
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance
#input coordinate
x1=float(input("enter x-coordinate of the first point:"))
y1=float(input ("enter y-coordinate of the first point:"))
x2=float(input("enter X-coordinate of the secound point:"))
y2=float(input("enter Y-coordnate of the secound point:"))
#calculate the result
diatance=calculate_distance(x1,y1,x2,y2)
#output the result
print(f"The distance between the points({x1},{y1})and ({x2},{y2}) is {distance:.2f}")

    
