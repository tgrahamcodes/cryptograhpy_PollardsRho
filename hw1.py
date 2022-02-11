import time as t

p = 2199023255867
n = p - 1
alpha = 3
beta = 1228035139812
time = t.perf_counter()

def do_update(x, a, b):
	if (x % 3 == 0): 
		x = (x * x) % p
		a =  (a*2) % n
		b =  (b*2) % n
		return x, a, b

	if (x % 3 == 1):
		x = (x * alpha) % p
		a = (a+1) % n
		return x, a, b

	if (x % 3 == 2):
		x = (x * beta)  % p
		b = (b+1) % n
		return x, a, b

def do_print(i, x, a, b, X, A2, B2):
	print ("-----------------------------------------------")
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
	print ("Operating System:\t macOS Monterey")
	print ("CPU:\t\t\t Apple M1")
	print ("RAM:\t\t\t 8GB")
	print ("IDE:\t\t\t Visual Studio Code")
	print ("----------------------------------------------\n")
	check(x, p)

def check(x, p):
	test3 = pow(alpha, x, p) 
	if (test3 == beta):
		print ("They are equal")
	else:
		print (test3)
		print (beta)

def main():
	x = 1
	a = 0
	b = 0
	i = 1

	X2 = x
	A2 = a
	B2 = b
	
	while (i < n):
		x, a, b = do_update(x, a, b)
		X2, A2, B2 = do_update(X2, A2, B2)
		X2, A2, B2 = do_update(X2, A2, B2)
		if (x == X2):
			z = b - B2
			if z == 0:
				return -1
			#x = (pow(z, -1) * (A2 - a)) % p
			print ("z: ", z)
			print ("beta: ", beta)
			print()
			do_print(i, x, a, b, X2, A2, B2)
			break
		else:
			i = i + 1

if __name__ == "__main__":
	main()