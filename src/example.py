try:
    file = open("datax", "r")
    content = file.read()
    file.close()
    print(f'"{content}" was read from a file named "data" in the current directory.')

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("You don't have permission to write to this file.")

except IsADirectoryError:
    print("Filename is a folder.")

except OSError as ex:
    # Catches FileExistsError, disk failures, or other system limits
    print(f"An OS error occurred: {ex}")