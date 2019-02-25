class Line:

  def __init__(self,coor1,coor2):
    self.coor1 = coor1
    self.coor2 = coor2

  def distance(self):
    return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5

  def slope(self):
    return float(self.coor2[1] - self.coor1[1]) / float(self.coor2[0] - self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

import math

class Cylinder:

  def __init__(self,height=1,radius=1):
    self.height = height
    self.radius = radius

  def volume(self):
    return math.pi * self.radius**2 * self.height

  def surface_area(self):
    return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius**2

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
