
import math
import sys

def main():
	for line in sys.stdin:
		words = line.split(" ")
		r = float(words[0])
		x = float(words[1])
		y = float(words[2])

		distance_squared = x**2 + y**2
		if distance_squared >= r**2:
			print ("miss")
		else: 
			dist = math.sqrt(distance_squared)
			h = r - dist 
			l = r-h

			chord_a = r**2 * math.acos(l/r)-l*math.sqrt(2*r*h-h**2)
			print (str((math.pi * r**2) - chord_a ) + " " + str(chord_a))
if __name__ == '__main__':
	main()