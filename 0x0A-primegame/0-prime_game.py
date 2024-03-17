#!/usr/bin/python3


# Sieve of Eratosthenes to find prime numbers
def generate_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    for p in range(2, n+1):
        if prime[p]:
            yield p


# Determine winner by counting the number of primes
# If the number of primes is even, Ben wins 
#   because he'll be the last to choose a prime number
# If the number of primes is odd, Maria wins                        
def isWinner(x, nums):
    if x < 1 or x > 10**5:
        return None
    
    maria_wins = 0
    ben_wins = 0
    
    max_n = max(nums)  # Find the maximum value of n to generate primes up to this value
    primes = generate_primes(max_n)
    
    for i in range(x):
        n = nums[i]
        num_primes = len([p for p in primes if p <= n])  # Count primes up to n
        if num_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

