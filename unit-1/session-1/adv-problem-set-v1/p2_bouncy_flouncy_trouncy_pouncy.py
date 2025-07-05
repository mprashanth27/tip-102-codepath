'''
U-nderstand:
Initially, the value of tigger is 1
bouncy and flouncy ~ tigger + 1 # ASSUMING CASE INSENSITIVE
trouncy and pouncy ~ tigger - 1

i/p = operations: list[str]
o/p = tigger: int

#Constraints

#Edge cases
[]
Non operations in i/p? skip them?

P-lan:
iterate thru operations list if not empty
inc/dec var tigger
return tigger

I-mplement:
'''
# 
def final_value_after_operations(operations):
	# Initialize tigger to 1
	tigger = 1
	
	if operations: # check if not empty
		for operation in operations:
			if operation == "bouncy" or operation == "flouncy":
				tigger += 1
			elif operation == "trouncy" or operation == "pouncy":
				tigger -= 1
	return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))


