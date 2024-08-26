
# n =10000
# prime_numbers = []
# for i in range (2, n):
#     for j in range (2, i):
#           if i % j ==0:
#                break
#     else:
#         prime_numbers.append(i)
# print(prime_numbers) 


n = 1000
twin_primes = []

for i in range(2, n - 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        for k in range(2, i + 2):
            if (i + 2) % k == 0:
                break
        else:
            twin_primes.append((i, i + 2))

print(twin_primes)