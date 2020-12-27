import math, sys 

def main():
	while True: 
		num_of_names  = int(sys.stdin.readline().strip())
		names = []
		dict = {} 
		if num_of_names == 0: 
			break 
		else: 
			for i in range(num_of_names):
				name = sys.stdin.readline().strip()
				names.append(name)
				dict[name[0:2]] = name 
			#for i in sorted (dict): 
				#print((i,dict[i]))
		print(dict)
		print(names)



if __name__ == "__main__":
	main()