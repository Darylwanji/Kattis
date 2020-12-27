import sys 

def main():
	""" Gets number of sentences """
	num_of_lines = int(sys.stdin.readline().strip())

	if num_of_lines == 0:
		""" Stops if 0 lines """
		return
	else:
		for i in range(num_of_lines):
			sentence = sys.stdin.readline()
			find_P(sentence)


def find_P(sentence):
	for n in range(1, len(sentence)):
		if sentence == ((sentence[0:n] * len(sentence))[:len(sentence)]):
			print(n)
		
if __name__ == "__main__":
	main()