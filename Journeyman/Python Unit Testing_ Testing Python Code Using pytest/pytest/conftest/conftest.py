import pytest
import os

@pytest.fixture
def write_file():
	print('\nCreating file')
	f = open('append_file.txt', 'w+')

	for i in range(10):
		f.write('\nX Y Z %d' % (i+1))

	f.flush()

	yield f

	print('\nClosing file')
	f.close()


@pytest.fixture
def readonly_file():
	print('\nCreating file')
	f = open('readonly_file.txt', 'w+')

	for i in range(10):
		f.write('\nX Y Z %d' % (i+1))

	f.close()

	f = open('readonly_file.txt', 'r')

	yield f

	print('\nClosing file')
	f.close()
















	