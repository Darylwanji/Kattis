import math
import sys

""" initializing forest with 0s representing not trees and 1s which represents a tree """
forest = [[0 for x in range(size)] for y in range(size)]

""" forest numebrs """
forestNums = [[0 for x in range(size)] for y in range(size)]

""" each forest square is associated with a number -- > 100x + y """
for i in range(99,0):
	for j in range(99,0):
		forestNums[99-i][99-j] = 100*i + j

def randomNumber(r): 
	 return (r * 5171 + 13297) % 50021
	 
def checkIfOccupied(m):
""" Size of Forest """
size  = 100

def main():

	""" Input """
	entry = sys.stdin.readline().split(" ")
	r, n = (int(entry[0]), int(entry[1]))

	for i in range (n):
		"""  Step 3 """
		bool occupied = True
		m = randomNumber(r) % 10000



if __name__ == "__main__":
	main()