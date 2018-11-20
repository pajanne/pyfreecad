#import freeCAD
#import Draft

coordinates = []
#freecad_coordinates = []

with open('airfoil_surface.csv') as input:
    for line in input:
        x, y = line.strip().split(',')
        coordinates.append([float(x), float(y)])
        #freecad_dot = freeCAD.Vector(float(x), float(y), 0)
        #freecad_coordinates.append(freecad_dot)

print(coordinates)
#Draft.makeBSpline(freecad_coordinates, closed=True)
