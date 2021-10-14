from functools import wraps
def counter(func):
	@wraps(func)
	def wrapper(name):
		wrapper.runs += 1
		func(name)
		print('Successful runs: {}'.format(wrapper.runs))
		wrapper.runs = 0
		return wrapper

	def log(func):
		def wrapper(*args):
			func(*args)
			print()
		return wrapper