#rose keenan section 2 lab 4
#program containing functions involing trig

import math

#FUNCTION ONE: defining the vertices
#k: which vertex being analyzed
#n: number of vertices of a regular polygon
#RETURN: position of k
def vert(k, n):
  x = math.cos(2*(math.pi)*k/n)
  y = math.sin(2*(math.pi)*k/n)
  return (x,y)

#FUNCTION TWO:  finding the list of vertices
#n: number of vertices of a regular polygon
#RETURN: list of tuples containing location of vertices
def vertices(n):
  vertList = []
  for k in range(n):
    eachPosition = vert(k, n)
    vertList.append(eachPosition)
  return vertList

#FUNCTION THREE: finding the distance between a given amount of vertices
#p1: the first tuple in the list of vertex locations
#p2: the second tuple in the list of vertex locations
#RETURN: the distance between p1 and p2
def dist(p1, p2):
  distance = (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2))
  distance = math.sqrt(distance)
  return distance

#FUNCTION FOUR: finding the perimeter
#points: list of tuples containing location of vertices of a regular polygon
#RETURN: the sum of the distances between every vertex of a regular polygon
def perimeter(points):
  perim = 0
  totalPerim = 0
  amountTuples = len(points)
  for k in range(amountTuples - 1):
    perim = dist(points[k], points[k + 1])
    totalPerim = totalPerim + perim
  totalPerim += dist(points[amountTuples - 1], points[0])
  return totalPerim

#FUNCTION FIVE: finding area using heron
#p1: the first tuple in the list of vertex locations
#p2: the second tuple in the list of vertex locations
#p3: the third tuple in the list of vertex locations
#RETURN: the area of the triangle for the given vertices
def heron(p1, p2, p3):
  s1 = dist(p1, p2)
  s2 = dist(p2, p3)
  s3 = dist(p3, p1)
  p = (s1 + s2 + s3) / 2.0
  area = (p*(p-s1)*(p-s2)*(p-s3))**0.5
  return area

#FUNCTION SIX: finding area of a regular triangle given a list of its n vertices
#points: list of tuples containing location of vertices of a regular polygon
#RETURN: the area of the polygon with n amount of vertices
def area(points):
   calcArea = 0
   polygonArea = 0
   amountTuples = len(points)
   for k in range(amountTuples - 1):
     calcArea = heron((0,0), (points[k]), (points[k + 1]))
     polygonArea += calcArea
   polygonArea += heron((0,0), (points[amountTuples - 1]), (points[0]))
   return polygonArea

#main program
if __name__ == "__main__":
  polygonVertices = [3, 103, 203, 303, 403, 503, 603, 703, 803, 903, 1003]
  for n in polygonVertices:
    print("Vertices:", n)
    points = vertices(n)
    perimeter(points)
    print("Perimeter:", perimeter(points))
    area(points)
    print("Area:", area(points))
    expr = perimeter(points)**2/(4.0*area(points))
    print("Expression:", expr)


