import random

def machine():
	measurement = random.random()
	if measurement > 0.6: raise Exception("Out of bounds")
	return measurement

goodParts = 0
badParts = 0
yieldHigh = 0
yieldLow = 1
for n in range(100):
	try:
		measurement = machine()
		if measurement < yieldLow: yieldLow = measurement
		if measurement > yieldHigh: yieldHigh = measurement
		goodParts += 1
	except:
		badParts += 1

print(f"goodParts: {goodParts}, badParts: {badParts}")
print(f"yieldLow: {yieldLow}, yieldHigh: {yieldHigh}")
