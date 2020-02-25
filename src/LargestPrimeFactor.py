def main():
    n = 600851475143
    largestprime(n)


def largestprime(o):
    prime = 1
    if o % prime == 0:
        prime += 1
    x = max(prime)
    print(f'this is the largest primefactor', {x})

# largestprime(600851475143)
