random, math, N = __import__("random"), __import__("math"), 1000_0 # N^2 = amount of numbers generated
a, b=[random.randint(1, 100) for i in range(N)], [random.randint(1, 100) for i in range(N)]
c=[math.sqrt((a[i]*b[j])) if math.sqrt((a[i]*b[j])) == int(math.sqrt((a[i]*b[j]))) else 0 for i in range(N) for j in range(N)]
print(f"Total:{len(c)-c.count(0)}\nPercentage: {((len(c)-c.count(0))/N**2)*100}% \nNums{len(c)}")
