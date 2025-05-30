import numpy
import math

def rotate_x(point, angle):
  rot_matrix =  [
          [1,0,0],
          [0, math.cos(angle), -math.sin(angle)],
          [0, math.sin(angle), math.cos(angle)]
        ]
  return numpy.dot(rot_matrix,point)

def rotate_y(point, angle):
  rot_matrix =  [
          [math.cos(angle),0,math.sin(angle)],
          [0, 1, 0],
          [-math.sin(angle), 0, math.cos(angle)]
        ]
  return numpy.dot(rot_matrix,point)

def rotate_z(point,angle):
  rot_matrix =  [
          [math.cos(angle),-math.sin(angle),0],
          [math.sin(angle), math.cos(angle), 0],
          [0, 0, 1]
        ]
  return numpy.dot(rot_matrix,point)