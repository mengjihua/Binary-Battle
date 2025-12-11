def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes():
    primes = [num for num in range(2, 101) if is_prime(num)]
    print("(1) 2~100中的素数: ")
    print(primes)
    return primes


def find_twin_primes(primes):
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i+1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i+1]))
    print("\n(2) 2~100中的孪生素数对: ")
    print(twin_primes)


def decompose_even(primes):
    print("\n(3) 4~20偶数分解为两个素数的和: ")
    for even in range(4, 21, 2):
        decompositions = []
        for p in primes:
            if p > even:
                break
            q = even - p
            if q >= p and is_prime(q):
                decompositions.append(f"{p} + {q}")
        print(f"{even} = " + "、".join(decompositions))


if __name__ == "__main__":
    primes_list = find_primes()
    find_twin_primes(primes_list)
    decompose_even(primes_list)