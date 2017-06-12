def is_prime(n):
    i = 2
    j = int(n**0.5)
    while i <= j:
        if n%i == 0:
            return
        else:
            i=i+1
    return 'true'

for n in range(1,100):
    if is_prime(n):
        print(n)
