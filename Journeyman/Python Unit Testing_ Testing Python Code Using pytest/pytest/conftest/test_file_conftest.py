def test_write_ten_lines(write_file):

	print('\nWriting ten lines')

	num_lines_before = sum(1 for line in open(write_file.name))

	for i in range(10):
		write_file.write('\nX Y Z %d' % (i+1))

	write_file.flush()

	num_lines_after = sum(1 for line in open(write_file.name))

	assert (num_lines_after - num_lines_before) == 10


def test_field_count(readonly_file):

	print('\nReading one line')

	readonly_file.readline()
	field_count = len(readonly_file.readline().split())

	assert field_count == 4






















	