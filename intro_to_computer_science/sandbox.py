def genPrimes():
    prime = 2
    while True:
        not_prime = False
        #print(f"prime trial {prime}")
        for num in range(2, prime):
            if prime % num == 0:
                prime += 1
                not_prime = True
                break
        if not_prime:
            continue
        yield prime
        prime += 1

gen = genPrimes()

counter = 0
while counter < 25:
    print(gen.__next__())
    counter += 1