try:
    file = open("datax", "r")
    content = file.read()
    file.close()
    print(f'"{content}" was read from a file named "data" in the current directory.')
except:
    print("Something unexpected happened.")
