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
  
def main(): 
	v = Vector([1,2], [1,2])
	print (v.vector_add(v.x, v.y))
	print (v.vector_subtract(v.x,v.y))
	print v.vector_sum(v.x)
	print v.scalar_multiply(2,v.x)
	
if __name__=="__main__": main()
