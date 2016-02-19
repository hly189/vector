import math

class Vector(object): 
	
	def __init__(self, x, y): 
		self.x = x
		self.y = y
	
	# adding vector 
	def vector_add(self, x, y): 
		return [x_i + y_i for x_i, y_i in zip(x, y)]
	
	
	# subtracting vector
	def vector_subtract(sef,x,y):
		return [x_i - y_i for x_i, y_i in zip(x, y)]

	# sum of a vector
	def vector_sum(self, vectors): 
		return sum(vectors)
	
	# scalar multiplication
	def scalar_multiply(self, c, v): 
		return [c*v_i for v_i in v]
 	
	# dot product
	def dot(self, x, y):
		return sum(x_i * y_i for x_i, y_i in zip(x,y))

	# mean of the vector
	def vector_mean(self, vectors): 
		n = len(vectors)
		v_sum = self.vector_sum(vectors)
		return self.scalar_multiply(1./n, [v_sum]) 

	#dot product of 2 vectors 
	def dot(self, x, y): 
		return sum(x_i*y_i for x_i, y_i in zip(x,y))

	# sum of square
	def sum_of_squares(self, x):
		return self.dot(x, x)
	
	# magnitude of length (length)
	def magnitude(self, x): 
		return math.sqrt(self.sum_of_squares(x))
	
	# distance of square of two vectors
	def square_distance(self, x, y): 
		return self.sum_of_squares(self.vector_subtract(x,y))

	# distance of two vectors
	def distance(self, x, y): 
		return math.sqrt(self.square_distance(x,y))
def main(): 
	v = Vector([1,2], [1,2])
	print v.vector_add(v.x, v.y)
	print v.vector_subtract(v.x,v.y)
	print v.vector_sum(v.x)
	print v.scalar_multiply(2,v.x)
	print v.dot(v.x, v.y)
	print v.vector_mean(v.x)
	print v.dot(v.x, v.y)
	print v.sum_of_squares(v.x)	
	print v.magnitude(v.x)	
	print v.square_distance(v.x,v.y)
	print v.distance(v.x,v.y)
	
if __name__=="__main__": main()
