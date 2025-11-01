import bpy
import math
import numpy as np

def move_to(obj, location):
    """ Set the object location.
    """
    obj.location = location
    bpy.context.view_layer.update()
    return obj
    
def move_by(obj, vector):
    """ Shift the object location by a 3D vector
    """
    obj.location[0] += vector[0]
    obj.location[1] += vector[1]
    obj.location[2] += vector[2]
    bpy.context.view_layer.update()
    return obj

# These are movable objects. 
table = bpy.data.objects['Table']
chair1 = bpy.data.objects['Chair.001']
chair2 = bpy.data.objects['Chair.002']
chair3 = bpy.data.objects['Chair.003']
chair4 = bpy.data.objects['Chair.004']
basketball = bpy.data.objects['basketball']

table.location = (0.0, 0.0, 0.0)
chair1.location = (0.0009641684591770172, -0.2938234508037567, 0.0)
chair2.location = (-0.5036665797233582, -0.0009641647338867188, 0.0)
chair3.location = (-0.0009641647338867188, 0.30151283740997314, 0.0)
chair4.location = (0.5036665797233582, 0.0009641647338867188, 0.0)
basketball.location = (0.0, 0.0, 0.6)