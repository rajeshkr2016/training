'''
Given int x, determine the set of prime factors
f(5) = [1,5]
f(6) = [2,3]
f(8) = [2,2,2]
f(10) = [2,5]

1) While n is divisible by 2, print 2 and divide n by 2.
2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i, increment i by 2 and continue.
3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2.

'''

def primefactor(n):
    print(n)
    if n < 2:
        print("The number cannot have prime factors")
    while n % 2 == 0:
        print("while loop")
        print(2)
        n = n/2
    for i in range(3, n+1, 2):
        while (n % i) == 0:
            print(i)
            n = n / i

n = 10
primefactor(n)
