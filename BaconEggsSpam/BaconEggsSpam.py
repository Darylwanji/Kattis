import math
import sys

list_of_Orders = {}
final = {}
def main():
	while True:
		""" Reading the first line """
		num_of_customers = int(sys.stdin.readline().strip())

		if num_of_customers == 0: 
			"""  As required, stops if number is zero """
			break
		else:
			""" Read next n(number of customers)lines """
			for _ in range(num_of_customers):
				order = sys.stdin.readline().split(" ")

				""" adding names and orders to dictionary """
				list_of_Orders[order[0]] = [ order[i].strip() for i  in range(1,len(order))] 

				""" getting all clients names """
			client_names = sorted(list_of_Orders.keys())
			pdts =get_list_of_products(list_of_Orders)

			""" Compares the list of products with list of orders """
			for product in pdts:
				final[product] = []
				for key in client_names: 
					if product in list_of_Orders.get(key):
						final[product].append(key)

			[print(key,*value) for key, value in final.items()]
			final.clear()
			list_of_Orders.clear()
			print()


def get_list_of_products(orders):
	""" gets sorted list of products in one order """
	product_list = list(orders.values())[0]

	for i in range(1,len(list_of_Orders)):
		product_list = product_list + list(set(list(orders.values())[i]) - set(product_list))
	return sorted(product_list)

if __name__ == "__main__":
	main()