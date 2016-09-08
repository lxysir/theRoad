##def febonacci(n): #fibonacci by recursion
##    if n == 1:
##        return 1
##    if n == 2:
##        return 2
##    if n > 2:
##        item = febonacci(n-1) + febonacci(n-2)
##    return item

# def febonacci(n): #fibonacci by for loop
#     no1 = 1
#     no2 = 2
#     output = 0
#     if n ==1:
#         return 1
#     if n==2:
#         return 2
#     else:
#         for i in range(3, n+1):
#             output = no1+no2
#             no1 = no2
#             no2 = output
#         return output


def fastFibonacci(n, memo): 
#fast fibonacci by dict [deal with 0/1背包问题，dynamic programming 最优子结构]
	for i in range(0, n+1):
		if i <= 1:
			memo[i] = 1
		if not i in memo:
			memo[i] = fastFibonacci(i-1, memo) + fastFibonacci(i-2, memo)
	return memo[n]


def febonacci(n):
	try:
		assert n >= 0
	except AssertionError:
		print("n < 0")
	else:
		memo = {}
		return fastFibonacci(n, memo)

output = []
for i in range(1, 40):
    if febonacci(i) < 4000000 and febonacci(i)%2 == 0:
        output.append(febonacci(i))
##    if febonacci(i) >4000000:
##        break
print(output)
print(sum(output))

print(febonacci(-1))

#list compehension
#[febonacci(i) for i in range(1, 10) if febonacci(i) < 400 and febonacci(i)%2 == 1]


##sum fibonacci even numbers        
##def PE002(M=4000000):
##  a, b, S  =  0, 1, 0
##  while b<=M:
##    a, b =  b, a+b
##    if a%2==0: S+=a
##  return S