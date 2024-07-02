## Project #1
## Advanced Cryptography

Pollard's rho algorithm is an algorithm for integer factorization. It was invented by John Pollard in 1975. It uses only a small amount of space, and its expected running time is proportional to the square root of the smallest prime factor of the composite number being factorized. 


1. Using a software package with big integer arithmetic support (e.g. Maple, Sage,
Python/NumPy, C/GMP) develop a program to compute a discrete logarithm in Z∗
p using either Pollard’s Rho method OR the Index-Calculus Technique. You may
use the large number arithmetic functions, including modular exponentiation, however
you are (obviously) not allowed to use built-in discrete logarithm functions.

Index Calculus is much faster but requires more coding than Pollard’s Rho.
Method.

Find the discrete logarithm x = logα β for
(a) (40 bits) p = 2199023255867, α = 3, and β = 1228035139812.
(b) (60 bits) p = 2305843009213699919, α = 3 and β = 259893785866906004,
(c) (80 bits) p = 2417851639229258349415043, α = 3, and β = 1007149824486452497234736.
(d) (100 bits)
p = 2535301200456458802993406412663, α = 3, and
β = 178675182869912164511023834697.
(e) (120 bits)
p = 2658455991569831745807614120560693943, α = 3, and
β = 612768819408156950694640654258960230.

In your answer, include your implementation. For each case, indicate how much time
was spent completing the attack. Also indicate the platform information (MHz speed,
memory, chip type, number of machines if you are running parallel threads, etc.).

