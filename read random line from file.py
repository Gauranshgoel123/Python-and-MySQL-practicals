
import random
def randnum(fname):
	lines=open(fname).read().splitlines()
	print(lines)
	return random.choice(lines)
print(randnum('file1.txt'))
