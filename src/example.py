import sys

print(f"dir(sys): {dir(sys)}\n")
print(f"type(sys): {type(sys)}\n")
print(f"id(sys): {id(sys)}\n")

print(f"dir(sys.argv): {dir(sys.argv)}\n")
print(f"type(sys.argv): {type(sys.argv)}\n")
print(f"id(sys.argv): {id(sys.argv)}\n")

print(f"len(sys.argv): {len(sys.argv)}")
print(f"type(len(sys.argv)): {type(len(sys.argv))}\n")

print(f"sys.argv[0]: {sys.argv[0]}")
print(f"type(sys.argv[0]): {type(sys.argv[0])}\n")

if len(sys.argv) > 1:
	print(f"sys.argv[1]: {sys.argv[1]}\n")

print("Arguments by index")

for index in range(len(sys.argv)):
	print(f"sys.argv[{index}]: {sys.argv[index]}")

print("\nArguments by iteration")

for arg in sys.argv:
	print(f"{arg}: {sys.argv.index(arg)}")
