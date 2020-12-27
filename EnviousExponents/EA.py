import math
import sys

def countOnes(number):
	count = 0
	for i in number:
		if i == 1:
			count += 1
	return count
def main():
	current = sys.stdin.readline().split(" ")
	mynumber = int(current[0])
	if (mynumber >= 1) and (mynumber <= 10 ** 18) and (int(current[1]) <= 60) and (int(current[1]) >= 1 ):
		while True:
			mynumber +=1
			number_bin = format(mynumber,"08b")
			bits = list(map(int, number_bin))
			if (countOnes(bits) == int(current[1]) and (mynumber > int(current[0]))):
				print(mynumber)
				break
if __name__ == "__main__":
	main()