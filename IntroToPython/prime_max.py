def prime(n):
    output = []
    i = 2
    while i <=n:
        if n%i == 0:
            output.append(i)
            n = int(n/i)
        i +=1
    return output

print(prime(600851475143))

d, n = 3, 60
while (d * d < n):
    if n % d == 0: n /= d
    else: d += 2
print(n)

roots = []; product = 1; x = 2; number = 60; y = number
while product != number:
	while (y % x == 0):
		roots.append(x)
		y /= x
		product *= roots[-1]
	x += 1
print(roots)
