def sum_first_primes(n = 10000):
    
    import numpy as np
    def isPrime(n):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        else:
            for i in range(3, int(np.ceil(np.sqrt(n))) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
    tsum = 0
    counter = 0
    i = 2
    
    while counter < n:
        if isPrime(i):
            tsum += i
            counter += 1
        
        i += 1
    
    return tsum

if __name__ == "__main__":
    print(sum_first_primes(n = 10000))

