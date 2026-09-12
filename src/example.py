def doNothing():
	pass

print(f"dir(doNothing): {dir(doNothing)}\n")
print(f"type(doNothing): {type(doNothing)}\n")
print(f"id(doNothing): {id(doNothing)}\n")
print(f"call of doNothing(): {doNothing()}\n")

def doNothing():
	return None
print(f"call of doNothing()): {doNothing()}\n")

def douglasAdams():
	return 42
print(f"call of douglasAdams()): {douglasAdams()}\n")

def doNothing(milk):
	if milk == "fresh": return "spoiled"
	else: return milk
print(f"doNothing(\"fresh\")): {doNothing("fresh")}\n")

def doNothing(milk, flour):
	if milk == "fresh": 
		if flour != None: return "matzah"
		else: return milk
	else: return "spoiled"
print(f"doNothing(\"fresh\", \"white\"): {doNothing("fresh", "white")}\n")

def doNothing(milk, flour=None):
	if milk == "fresh": 
		if flour != None: return "matzah"
		else: return "spoiled"
	else: return "spoiled"
print(f"doNothing(\"fresh\", \"white\"): {doNothing("fresh")}\n")
