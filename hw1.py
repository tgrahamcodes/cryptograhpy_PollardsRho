# Tom Graham
# Homework 1
# CS-673 Advanced Cryptograhpy

import time as t

time = t.perf_counter()

def do_update(alpha, beta, p, x, a, b, n):
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

# def do_print(alpha, beta, n, i, x, a, b, A2, B2, z, flag):
# 	print ("\n-----------------------------------------------")
# 	print ("Pollard's Rho")
# 	print ("-----------------------------------------------")
# 	print ("Input:")
# 	print ("Alpha:", alpha, end="")
# 	print ("  Beta:", beta, end="")
# 	print ("  P:", p)
# 	print ("-----------------------------------------------")
# 	print ("\nCollision found")
# 	print ("-----------------------------------------------")
# 	print ("x = X: \t\t\t ", x)
# 	print ("\na :\t\t\t ", a)
# 	print ("b :\t\t\t ", b)
# 	print ("\nA2 :\t\t\t ", A2)
# 	print ("B2 :\t\t\t ", B2)
# 	print ("Total Iterations:\t ", i - 1)
# 	print ("Runtime :\t\t ", time)
# 	print ("\n-----------------------------------------------")
# 	print ("System Specifications:")
# 	print ("-----------------------------------------------")
# 	print ("\nOperating System:\t macOS Monterey")
# 	print ("CPU:\t\t\t Apple M1")
# 	print ("RAM:\t\t\t 8GB")
# 	print ("IDE:\t\t\t Visual Studio Code")
# 	print ("----------------------------------------------\n")
# 	do_check(z, flag, n)
# 	print ("----------------------------------------------\n")

def do_check(z, flag, p):
	if (flag):
		if (beta == pow(alpha, z, p)):
			print ("Beta:\t\t\t", beta)
			print ("Pow:\t\t\t", pow(alpha, z, p))
			print ("\nCheck succeeded!")
		else:
			print ("\nCheck failed.")
	else:
		if (beta == pow(alpha, z, (p-1))):
			print ("Beta:\t\t\t", beta)
			print ("Pow:\t\t\t", pow(alpha, z, p))
			print ("\nCheck succeeded!")
		else:
			print ("\nCheck failed.")

def main(alpha, beta, p, flag):

	if (flag):
		n = int((p - 1) / 2)
	else:
		n = int(p)

	a = 777357
	b = 552357
	i = 1
	x = pow(alpha, a, p) * pow(beta, b, p) % p

	X2 = pow(alpha, a, p) * pow(beta, b, p) % p
	A2 = 777357
	B2 = 552357
	
	while (i < n):
		x, a, b = do_update(alpha, beta, p, x, a, b, n)
		X2, A2, B2 = do_update(alpha, beta, p, X2, A2, B2, n)
		X2, A2, B2 = do_update(alpha, beta, p, X2, A2, B2, n)

		if (x == X2):
			print (x)
			print (X2)
			print("x = X2")
			bb = (b - B2) % n
			print("bb: ", bb)
			print("b: ", b)
			print("B2: ", B2)
			print("n: ", n)
			print("p: ", p)
			aa = (A2 - a)

			bb = (b - B2) % n
			aa = A2 - a
		
			if bb == 0:
				return -1
			z = (pow(bb, -1, n) * (A2 - a)) % n

			print ("z", z)
			if (beta == pow(alpha, z, p)):
				print ("Passed")
			else:
				print ("failed")
			# do_print(alpha, beta, n, i, x, a, b, A2, B2, z, flag)
			break
		else:
			i = i + 1

if __name__ == "__main__":

	p = 2199023255867
	alpha = 3
	beta = 1228035139812	
	main(alpha, beta, p, True)
	print("Problem One Solved!")
	print("-------------------")
	
	p2 = 2305843009213699919
	alpha2 = 3
	beta2 = 259893785866906004	
	main(alpha2, beta2, p2, False)
	print("Problem Two Solved!")
	print("-------------------")

	# p = 2417851639229258349415043
	# n3 = int(p - 1)
	# alpha = 3
	# beta = 1007149824486452497234736	
	# main(alpha, beta, p, n3)

