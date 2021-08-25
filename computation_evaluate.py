class Number:
	
	def __init__(self,value = 0):
		if not isinstance(value,(int,float)):
			raise Exception("ERROR -> Number : {} is not (int or float).".format(value))
		self.value = value
		
	def __str__(self):
		return "{}".format(self.value)
		
	def __repr__(self):
		return str(self)
	
	def evaluate(self,env = {}):
		return self

class Boolean:
	
	def __init__(self,value = False):
		if not isinstance(value,bool):
			raise Exception("ERROR -> Boolean : {} is not bool.".format(value))
		self.value = value
		
	def __str__(self):
		return "{}".format(self.value)
		
	def __repr__(self):
		return str(self)
	
	def evaluate(self,env = {}):
		return self.value
		
	@staticmethod
	def to_false():
		return Boolean(False)
	
	@staticmethod
	def to_true():
		return Boolean(True)		


class Variable:
	
	def __init__(self,value = 0):
		if not isinstance(value,str):
			raise Exception("ERROR -> Variable : {} is not str.".format(value))
		self.value = value
		
	def __str__(self):
		return "{}".format(self.value)
		
	def __repr__(self):
		return str(self)
			
	def evaluate(self,env = {}):
		if self.value not in env:
			raise Exception("Variable : {} is not defined.".format(self.value))
		return env[self.value]

class BinaryNode:
	
	def __init__(self,left,right):
		self.left = left
		self.right = right
	
		
class DoNothingNode():

	def evaluate(self,env = {}):
		return env

class AddNode(BinaryNode):

	def evaluate(self,env = {}):
		return Number(self.left.evaluate(env).value + self.right.evaluate(env).value)

class MulNode(BinaryNode):

	def evaluate(self,env = {}):
		return Number(self.left.evaluate(env).value * self.right.evaluate(env).value)

class LessThanNode(BinaryNode):

	def evaluate(self,env = {}):
		return Boolean(self.left.evaluate(env).value < self.right.evaluate(env).value)

		
class AssignNode(BinaryNode):

	def evaluate(self,env = {}):
		env.update({self.left.value : self.right.evaluate(env)})
		return env

class IfNode:
	
	def __init__(self,condition,consequence,alternative):
		self.condition = condition
		self.consequence = consequence
		self.alternative = alternative
		
	def evaluate(self,env = {}):		
		if self.condition.evaluate(env).value:
			return self.consequence.evaluate(env)
		else:	
			return self.alternative.evaluate(env)
			
class SequenceNode(BinaryNode):

	def evaluate(self,env = {}):
		self.right.evaluate(self.left.evaluate(env))
		return env

class WhileNode:
	
	def __init__(self,condition,body):
		self.condition = condition
		self.body = body
		
	def evaluate(self,env = {}):		
		if self.condition.evaluate(env).value:
			return self.evaluate(self.body.evaluate(env))
		else:	
			return env

statement = WhileNode(
	LessThanNode(Variable("x"),Number(5)),
	AssignNode(Variable("x"),MulNode(Variable("x"),Number(3)))
)		
print(statement.evaluate({"x" : Number(1)})) ## {"x" : 9}		

'''		
statement = SequenceNode(
	AssignNode(Variable("x"),AddNode(Number(1),Number(1))),
	AssignNode(Variable("y"),AddNode(Variable("x"),Number(3)))
)		

print(statement.evaluate({}))			
'''
			
##print(IfNode(LessThanNode(Number(6),Number(9)),Variable("a"),Number(2)).evaluate({"a" : Number(6)}))
		
##print(LessThanNode(Variable("a"),Number(9)).evaluate({"a" : Number(6)}))

##print(AssignNode(Variable("a"),Number(9)).evaluate({"a" : Number(6)}))

