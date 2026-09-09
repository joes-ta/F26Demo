file = open("data", "r")
content = file.read()
file.close()
print(f'"{content}" was read from a file named "data" in the current directory.')