with open("data", "r") as animal:
	first = "{"
	for kind in animal:
		if ord( kind[0] ) < ord(first[0]): first = kind

print(first)
