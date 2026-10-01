def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    # [True, True, True, True , True, True, True]
    # [True, True, True, True , False, True, False]
    # [0 , 1, 2, 3, 4, 5, 6, 7]
    p = 2
    while (p * p <= num): #4 <= 7 
        if (prime[p] == True):
            # range(2 * 2, 7 + 1, 2)
            # 4, 8, 2
            # 4 , 6
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    for p in range(2, num+1):
        if prime[p]:
            print(p)

num = int(input("Enter a number"))
print("Following are the prime numbers smaller")
print("than or equal to", num)
SieveOfEratosthenes(num)