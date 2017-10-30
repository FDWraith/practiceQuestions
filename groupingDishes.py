def groupingDishes(dishes):
	"""
	:dishes type: List of Lists
	rtype: List of Lists
	"""

	d = {}
	# Dictonary of:
	# "Ingredient" : set( [DishName, DishName, ...])
	for dish in dishes:
		# Dish is composed of:
		# "Name of Dish", ... "Ingredients" ...
		name = dish[0]
		ingredients = dish[1:]

		for ingredient in ingredients: 
			# If there is an ingredient key in the dict,
			# Then jsut add the name of dish to that 
			# Else, create a new entry in the dict
			if ingredient in d:
				d[ingredient].add(name)
			else:
				d[ingredient] = set([name])

	l = []
	for ingredient in sorted(d.keys()):
		if len(d[ingredient]) >= 2:
			entry = [ingredient] + sorted(d[ingredient])
			l.append( entry )

	return l





