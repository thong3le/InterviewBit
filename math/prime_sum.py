class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        prime_test = [False, False, True, True] + [False, True] * (A//2)
        for i in range(3, int(A**0.5) + 1, 2):
            for k in range(i*i, A+1, i):
                prime_test[k] = False
        primes = [i for i in range(A+1) if prime_test[i] and i <= A//2]
        for i in primes:
            if prime_test[A-i]:
                return [i, A-i]