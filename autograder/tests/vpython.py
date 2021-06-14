# Github repository for vPython code is at
# https://github.com/vpython/vpython-jupyter

# Import functions from math

from math import cos, sin, sqrt

#-----------------------------------------------------------------------------#

# Math functions

pi = 3.141592653589793

#-----------------------------------------------------------------------------#

# Vectors are important

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
        return vector(self.x / v, self.y / v, self.z / v)

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

#-----------------------------------------------------------------------------#

# Add color to your life

class color:
    def __init__(self, *args):
        pass

#-----------------------------------------------------------------------------#

# Default values for most vPython objects are same
# as that of a cylinder

class cylinder:
    def __init__(self,
                 pos = vector(0, 0, 0),
                 axis = vector(1, 0, 0),
                 up = vector(0, 1, 0),
                 length = 1,
                 radius = 1,
                 #size = vector(length, 2 * radius, 2 * radius),
                 color = vector(1, 1, 1),
                 red = 1,
                 green = 1,
                 blue = 1,
                 opacity = 1,
                 shininess = 0.6,
                 emissive = False,
                 make_trail = False):
        
        self.pos = pos
        self.axis = axis
        self.up = up
        self.length = length
        self.radius = radius
        #self.size = size
        self.color = color
        self.red = red
        self.green = green
        self.blue = blue
        self.opacity = opacity
        self.shininess = shininess
        self.emissive = emissive
        self.make_trail = make_trail
        
        # Potential problem with length, radius not matching
        # defined values for size

#-----------------------------------------------------------------------------#
        
class arrow:
    def __init__(self,
                 pos = vector(0, 0, 0),
                 axis = vector(1, 0, 0),
                 up = vector(0, 1, 0),
                 length = 1,
                 radius = 1,
                 #size = vector(length, 2 * radius, 2 * radius),
                 color = vector(1, 1, 1),
                 red = 1,
                 green = 1,
                 blue = 1,
                 opacity = 1,
                 shininess = 0.6,
                 emissive = False,
                 make_trail = False,
                 round = False,
                 shaftwidth = 0.1,
                 headwidth = 0.2,
                 headlength = 0.3):
        
        self.pos = pos
        self.axis = axis
        self.up = up
        self.length = length
        self.radius = radius
        #self.size = size
        self.color = color
        self.red = red
        self.green = green
        self.blue = blue
        self.opacity = opacity
        self.shininess = shininess
        self.emissive = emissive
        self.make_trail = make_trail
        self.round = round
        self.shaftwidth = shaftwidth
        self.headwidth = headwidth
        self.headlength = headlength
        
        # Setting shaftwidth to zero sets it
        # to the default
        
#        if shaftwidth == 0:
#            self.shaftwidth = 0.1 * self.length

#-----------------------------------------------------------------------------#

class box:
    def __init__(self, pos = (0, 0, 0), color = (1, 1, 1)):
        self.pos = pos
        self.color = color
