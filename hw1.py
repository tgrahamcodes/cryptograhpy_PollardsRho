# Tom Graham
# Homework 1
# CS-673 Advanced Cryptograhpy

import time as t

time = t.perf_counter()

def do_update(alpha, beta, p, x, a, b):
	n = int((p - 1) / 2)
	if (x % 3 == 1): 
		x = (x * x) % p
		a =  (a*2) % n
		b =  (b*2) % n
		return x, a, b

	if (x % 3 == 0):
		x = (x * alpha) % p
		a = (a+1) % n
		return x, a, b

	if (x % 3 == 2):
		x = (x * beta) % p
		b = (b+1) % n
		return x, a, b

def do_print(alpha, beta, p, i, x, a, b, A2, B2, z):
	print ("\n-----------------------------------------------")
	print ("Pollard's Rho")
	print ("-----------------------------------------------")
	print ("Input:")
	print ("Alpha:", alpha, end="")
	print ("  Beta:", beta, end="")
	print ("  P:", p)
	print ("-----------------------------------------------")
	print ("\nCollision found")
	print ("-----------------------------------------------")
	print ("x = X: \t\t\t ", x)
	print ("\na :\t\t\t ", a)
	print ("b :\t\t\t ", b)
	print ("\nA2 :\t\t\t ", A2)
	print ("B2 :\t\t\t ", B2)
	print ("Total Iterations:\t ", i - 1)
	print ("Runtime :\t\t ", time)
	print ("\n-----------------------------------------------")
	print ("System Specifications:")
	print ("-----------------------------------------------")
	print ("\nOperating System:\t macOS Monterey")
	print ("CPU:\t\t\t Apple M1")
	print ("RAM:\t\t\t 8GB")
	print ("IDE:\t\t\t Visual Studio Code")
	print ("----------------------------------------------\n")
	do_check(z)
	print ("----------------------------------------------\n")

def do_check(z):
	if (beta == pow(alpha, z, p)):
		print ("Beta:\t\t\t", beta)
		print ("Pow:\t\t\t", pow(alpha, z, p))
		print ("\nCheck succeeded!")
	else:
		print ("\nCheck failed.")

def main(alpha, beta, p):

	n = int((p - 1) / 2)
	a = 777357
	b = 552357
	i = 1
	x = pow(alpha, a, p) * pow(beta, b, p) % p

	X2 = pow(alpha, a, p) * pow(beta, b, p) % p
	A2 = 777357
	B2 = 552357
	
	while (i < n):
		x, a, b = do_update(alpha, beta, p, x, a, b)
		X2, A2, B2 = do_update(alpha, beta, p, X2, A2, B2)
		X2, A2, B2 = do_update(alpha, beta, p, X2, A2, B2)

		if (x == X2):
			bb = (b - B2) % n
			aa = A2 - a
		
			if bb == 0:
				return -1
			z = (pow(bb, -1, n) * (A2 - a)) % n
			do_print(alpha, beta, p, i, x, a, b, A2, B2, z)
			break
		else:
			i = i + 1

if __name__ == "__main__":

	# p = 2199023255867
	# n = int((p - 1) / 2)
	# alpha = 3
	# beta = 1228035139812	
	# main(alpha, beta, p)
	# print("Problem One Solved!\n")
	
	p = 2305843009213699919
	alpha = 3
	beta = 259893785866906004	
	main(alpha, beta, p)
	print("Problem Two Solved")

	# p = 2417851639229258349415043
	# n = int((p - 1) / 2)
	# alpha = 3
	# beta = 1007149824486452497234736	
	# main(alpha, beta, p)

