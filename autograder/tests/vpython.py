# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:32:50 2021

@author: cartin
"""

# Create a class of mock objects

class Mock:
    def __init__(self, name, *args, **kwargs):
        self.name = name

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        for name in kwargs:
            setattr(self, name, kwargs[name])

        if self.name == "vector" and len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

        return self

# Create possible vPython objects

arrow = Mock("arrow")
box = Mock("box")
cone = Mock("cone")
curve = Mock("curve")
cylinder = Mock("cylinder")
ellipsoid = Mock("ellipsoid")
helix = Mock("helix")
label = Mock("label")
pyramid = Mock("pyramid")
ring = Mock("ring")
sphere = Mock("sphere")

# Auxiliary commands

canvas = Mock("canvas")
rate = Mock("rate")

# Create all possible vPython colors
# (list taken from https://www.glowscript.org/docs/VPythonDocs/color.html)

color = Mock("color")

color.red = "red"
color.green = "green"
color.blue = "blue"
color.purple = "purple"
color.yellow = "yellow"
color.orange = "orange"
color.cyan = "cyan"
color.magenta = "magenta"
color.black = "black"
color.white = "white"

# Vectors must be handled specially, since calculations must be carried out
# properly and reported at the end

class vector:

    def __init__(self, *args):
        if len(args) == 3:              # Vector defined in terms of components
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])
        elif len(args) == 1 and isinstance(args[0], vector):
            other = args[0]
            self.x = other.x
            self.y = other.y
            self.z = other.z
        else:
            raise TypeError('A vector needs 3 components.')

    # Return vPython-style vector, either as part of a print (or str())
    # statement, or when called directly

    def __str__(self):
        return '<{:.6g}, {:.6g}, {:.6g}>'.format(self.x, self.y, self.z)

    def __repr__(self):
        return '<{:.6g}, {:.6g}, {:.6g}>'.format(self.x, self.y, self.z)

    # Determines if two vectors are equal by verifying their components
    # are equal

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # Vector addition and subtraction

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # Define scalar multiplication: __mul__ for when the vector is
    # given first, and __rmul__ for when the vector is second

    def __mul__(self, other):
        return vector(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, other):
        return vector(other * self.x, other * self.y, other * self.z)

    # Only division using '/' appears to be defined in Glowscript; the
    # operations '//' and '%' give errors

    def __truediv__(self, other):
        return vector(self.x / other, self.y / other, self.z / other)

    # Magnitude

    def mag(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Magnitude squared

    def mag2(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    # Unit vector in same direction as given vector
    # (two possible commands)

    def norm(self):
        v = mag(self)
        return vector(self.x / mag, self.y / mag, self.z / mag)

    # Scalar product

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Vector product

    def cross(self, other):
        return vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

# Define shortcuts for certain vector operations

cross = vector.cross
dot = vector.dot
hat = vector.norm
mag = vector.mag
mag2 = vector.mag2
norm = vector.norm
