def print_items(items_list):
	"""
	>>> print_items(['Ecuador', 'Egypt', 'Estonia']) #doctest: +NORMALIZE_WHITESPACE
	<BLANKLINE>
	  Ecuador
	<BLANKLINE>
	 	Egypt
	<BLANKLINE>
	 Estonia
	"""
	for item in items_list:
		print('\n', item)