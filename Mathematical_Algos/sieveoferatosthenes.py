import sys
# This code is also part of my blog written here - https://iq.opengenus.org/the-sieve-of-eratosthenes/
def sieve_erato(n):
    loops = 0
    numbers = set(range(2, n))
    for i in range(2, int(n ** 0.5) + 1): #start traversing through unmarked numbers 
        for j in range(i * 2, n, i):  #mark number and multiples of 2 
            numbers.discard(j)
            loops += 1
    return sorted(numbers), loops    #keep repeating until n-1
try:
    primes = sieve_erato(int(input().rstrip()))
except:
    sys.exit()
print(primes[0])
print("\nComputations {}".format(primes[1]))
