class Geometry(object):
	def __init__(self):
		pass
	def area(self):
		pass
	def perimeter(self):
		pass
class Cylinder(Geometry):
	def __init__(self, radius=1, height=1):
		self.radius = radius
		self.height = height
	def volume(self):
		volume = self.height * (3.14) * (self.radius)**2
		return volume
	def surface_area(self):
		top = (3.14)* (self.radius)**2
		surface_area = 2*top + 2*3.142*self.radius*self.height
		return surface_area
class Cube(Geometry):
	def __init__(self, length = 1):
		self.length = length
	def volume(self):
		volume = self.length**3
		return volume
	def surface_area(self):
		surface_area = 6*(length**2)
		return surface_area
c = Cylinder(2,3)
print (c.volume())