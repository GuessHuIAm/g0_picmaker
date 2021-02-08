import random

def main():
	pixels = ''

	r1 = random.randint(0, 255)
	r2 = random.randint(0, 255)
	g1 = random.randint(0, 255)
	g2 = random.randint(0, 255)
	b1 = random.randint(0, 255)
	b2 = random.randint(0, 255)

	for i in range(250000):
		if (i % 50) < 25:
			pixels += str((r1 + i) % 256) + ' ' + str((g1 + i) % 256) + ' ' + str((b1 + i) % 256) + '\n'
		else:
			pixels += str((r2 + i) % 256) + ' ' + str((g2 + i) % 256) + ' ' + str((b2 + i) % 256) + '\n'

	pic = open('picture.ppm', 'w+')
	pic.write('P3\n500 500\n255\n')
	pic.write(pixels)
	pic.close()


main()
