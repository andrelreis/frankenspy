"""
Definition of geometries like spheres, prisms, polygons, etc.

"""

from __future__ import division, absolute_import
from future.builtins import object, super
import numpy as np
import copy as cp

class GeometricElement(object):
    """
    Common class for geometric elements.
    """

    def __init__(self,props):
        self.props = {}
        if props is not None:
            for p in props:
                self.props[p] = props[p]

    def addprop(self,prop,value):
        """
        Define the physical property of a geometric element

        Parameters :

        * prop - string
        Physical property such as density or magnetization

        * value - float
        Value of the physical property
        """

        self.props[prop] = value

    def copy(self):
        """
        A deep copy of this instance
        """
        return cp.deepcopy(self)


class Sphere(GeometricElement):
    """
    Define a sphere

    Parameters :

    * x,y,z - float
    Cartesian coordinate of the center

    * radius - float
    Radius of the sphere

    """

    def __init__(self,x,y,z,radius,props=None):
        super().__init__(props)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.center = np.array([x,y,z])
