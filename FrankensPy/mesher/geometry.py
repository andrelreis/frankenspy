"""
Defining geometries like spheres, prisms, polygons, etc.

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

    Parameters
    ------------

    * center: tuple - Cartesian coordinate of the center

    * radius: float - Radius of the sphere

    """

    def __init__(self,center,radius,props=None):
        super().__init__(props)
        self.center = tuple(x,y,z)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)

class RecPrism(GeometricElement):
    """
    Define a rectangular prism

    Parameters
    ------------

    * bounds: tuple - Horizontal bounds of the prism

    * top: float - Position of the top of the prism

    * bottom: float - Position of the bottom of the prism

    """
    def __int__(self,bounds,top,bottom,props=None):
        super().__init__(props)
        self.bounds = tuple(westing,easting,southing,northing)
        self.westing = float(westing)
        self.easting = float(easting)
        self.southing = float(southing)
        self.top = float(top)
        self.bottom = float(bottom)

class PolyPrism(GeometricElement):
    """
    Define a polygonal prism

    Parameters
    -----------

    * coordinates_ns : tuple - N-S vertices of the polygonal prisms

    * coordinates_ew : tuple - E-W vertices of the polygonal prisms

    * top: float - Position of the top of the prism

    * bottom: float - Position of the bottom of the prism

    """
    def __init__(self,coordinates_ns,coordinates_ew,top,bottom,props=None):
    super().__init__(props)
    self.coordinates_ns = tuple(coordinates_ns)
    self.coordinates_ew = tuple(coordinates_ew)
    self.top = float(top)
    self.bottom = float(bottom)
