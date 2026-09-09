with open("data", "r") as file:
	content = file.read()

print(f'"{content}" was read from a file named "data" in the current directory.')