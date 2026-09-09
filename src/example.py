import random

"""
There are a number of factors that can cause bad parts. In this model,
so far, they are lumped into a single measurement.
"""
def machine():
	measurement = random.random()
	if measurement > 0.8: raise Exception("Out of bounds")
	return measurement

"""
The Production Department is responsible for running machines to 
make parts. There's a QC Dept for determining process problems and
a Maintenance Dept for fixing machines. So, the machine exception 
bubbles up through Production to the Factory.
"""
def production():
	part = machine()
	return part

"""
The QC Departent should really do something to improve the process.
"""
class QualityControl():
	failures = 0
	
	def track():
		QualityControl.failures += 1

"""
In this model, a factory attempts to fulfill orders.
"""
def factory():
	order = 1000000
	parts = 0
	while parts < order:
		try:
			production()
			parts += 1
		except Exception as e:
			QualityControl.track()
	print(f"ship: {order}")
	print(f"scrap: {QualityControl.failures}")

factory()
