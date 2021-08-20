"""
Grammar:
0.E  ->  TE'
1.E' -> +TE' | .
2.T  ->  FT'
3.T' -> *FT' | .
4.F  ->  id  | (E)
"""

non_terminals = ["E","E'","T","T'","F"]

terminals = ["id","+","*","(",")","$"]

table = {
	"E" : {
		"id" : ["T","E'"],
		"("  : ["T","E'"]
	},
	"E'" : {
		"+"  : ["+","T","E'"],
		")"  : ["."],
		"$"  : ["."]
	},
	"T" : {
		"id" : ["F","T'"],
		"("  : ["F","T'"]
	},
	"T'" : {
		"+"  : ["."],
		"*"  : ["*","F","T'"],
		")"  : ["."],
		"$"  : ["."],
	},
	"F" : {
		"id" : ["id"],
		"("  : ["(","E",")"]
	}
}

actions = []
inputs = "( id + id ) * id".split(" ") + ["$"]
stack = ["$","E"]

def parse():
	while True:
		s = stack[-1]
		i = inputs[0]
		if s == "$" and i == "$":
			print()
			print("Accepted")
			print()
			break
		if len(inputs) == 0 or len(stack) == 0:
			print()
			print("Rejected")
			print()
			break
		if s == '.':
			stack.pop()
		else:
			if s in terminals:
					if i == s:
						stack.pop()
						inputs.pop(0)
			else:
				if i not in table[s]:
					raise Exception("ERROR: Undefined {} for {}".format(i,s))
				action = table[s][i]
				actions.append([s,action])
				print("On Seeing input {} and stack {} required action is {} -> {} ".format(i,s,s,"".join(action)))
				print()
				stack.pop()
				for element in action[::-1]:
					stack.append(element)		

parse()
for action in actions:
	print("{:3} -> {}".format(action[0],"".join(action[1])))


"""
Input : ( id + id ) * id
Output:
On Seeing input ( and stack E required action is E -> TE'

On Seeing input ( and stack T required action is T -> FT'

On Seeing input ( and stack F required action is F -> (E)

On Seeing input id and stack E required action is E -> TE'

On Seeing input id and stack T required action is T -> FT'

On Seeing input id and stack F required action is F -> id

On Seeing input + and stack T' required action is T' -> .

On Seeing input + and stack E' required action is E' -> +TE'

On Seeing input id and stack T required action is T -> FT'

On Seeing input id and stack F required action is F -> id

On Seeing input ) and stack T' required action is T' -> .

On Seeing input ) and stack E' required action is E' -> .

On Seeing input * and stack T' required action is T' -> *FT'

On Seeing input id and stack F required action is F -> id

On Seeing input $ and stack T' required action is T' -> .

On Seeing input $ and stack E' required action is E' -> .


Accepted

E   -> TE'
T   -> FT'
F   -> (E)
E   -> TE'
T   -> FT'
F   -> id
T'  -> .
E'  -> +TE'
T   -> FT'
F   -> id
T'  -> .
E'  -> .
T'  -> *FT'
F   -> id
T'  -> .
E'  -> .
"""
