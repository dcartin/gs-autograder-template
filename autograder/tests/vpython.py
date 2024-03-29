# Github repository for vPython code is at
# https://github.com/vpython/vpython-jupyter

# Last updated: 30 Jul 2021

# Import functions from math

from math import acos, asin, atan, cos, radians, sin, sqrt, tan

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
    
    # Negation of a vector
    
    def __neg__(self):
        return vector(-self.x, -self.y, -self.z)

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
    def __init__(self):
        
        self.red = vector(1, 0, 0)
        self.green = vector(0, 1, 0)
        self.blue = vector(0, 0, 1)
        self.purple = vector(0.4, 0.2, 0.6)
        self.yellow = vector(1, 1, 0)
        self.orange = vector(1, 0.6, 0)
        self.cyan = vector(0, 1, 1)
        self.magenta = vector(1, 0, 1)
        self.black = vector(0, 0, 0)
        self.white = vector(1, 1, 1)
        
# Create a color() object called color

color = color()

#-----------------------------------------------------------------------------#

# There is no need to define anything related to rate, so I don't, but
# it does need to be present, just in case it is used

class rate:
    def __init__(self, value):
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
                 make_trail = False,
                 **kwargs):
        
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
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
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
    def __init__(self,
                 pos = (0, 0, 0),
                 color = (1, 1, 1),
                 **kwargs):
        
        self.pos = pos
        self.color = color
        
        for key, value in kwargs.items():
            setattr(self, key, value)

#-----------------------------------------------------------------------------#

class sphere:
    def __init__(self,
                 pos = vector(0, 0, 0),
                 axis = vector(1, 0, 0),
                 up = vector(0, 1, 0),
                 color = vector(1, 1, 1),
                 red = 1,
                 green = 1,
                 blue = 1,
                 opacity = 1,
                 shininess = 0.6,
                 emissive = False,
                 #texture = textures.something
                 radius = 1,
                 #size = vector(length, 2 * radius, 2 * radius),
                 make_trail = False,
                 **kwargs):
        
        self.pos = pos
        self.axis = axis
        self.up = up
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
        
        for key, value in kwargs.items():
            setattr(self, key, value)

#-----------------------------------------------------------------------------#

class graph:
    def __init__(self,
                 width = 640,
                 height = 400,
                 align = 'none',
                 title = '',
                 xtitle = '',
                 ytitle = '',
                 xmin = None,
                 xmax = None,
                 ymin = None,
                 ymax = None,
                 foreground = color.black,
                 background = color.white):
        
        self.width = width
        self.height = height
        self.title = title
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.foreground = foreground
        self.background = background

#-----------------------------------------------------------------------------#

class gcurve:
    def __init__(self,
                 graph = graph(),
                 data = [],
                 width = 2,
                 color = color.black,
                 markers = False,
                 dot = False,
                 visible = True):
        
        self.graph = graph
        self.data = []
        
    # Create data structure to hold plotted data
        
    def plot(self, *args):
        
        self.data += [[data_pt for data_pt in args]]
