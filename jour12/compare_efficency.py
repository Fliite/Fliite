n = int(input("Enter an integer number:"))
prime = [] # An empty list
for i in range(n+1):
    prime.append(i)

prime[0]=0
prime[1]=0   

p = 2
while (p * p <= n): 
    # If prime[p] is not changed, then it is a prime 
    if (p != 0): 
        # Update all multiples of p to zero
        for i in range(p*2, n+1, p): 
            prime[i] = 0

    p += 1
    
print(prime)
#print all element of list which are not zero
print("All the prime numbers up to", n, "are:")
for i in range(len(prime)):
    if (prime[i] != 0):
        liste1.append(prime[i])