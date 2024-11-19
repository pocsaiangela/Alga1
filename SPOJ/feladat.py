def Prime_Generator():
    def isPrime(num):
        if num in cache:
            return cache[num]

        if num <= 1:
            cache[num] = False
            return False

        if num == 2:
            cache[num] = True
            return True

        for i in range(2, num):
            if num % i == 0:
                cache[num] = False
                return False

        cache[num] = True
        return True

    cache = {}
    t = int(input())

    for _ in range(t):
        line = input().split()
        n = int(line[0])
        m = int(line[1])

        for i in range(n, m + 1):
            if isPrime(i):
                print(i)
        print("")

    