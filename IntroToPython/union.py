def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)
p = ['a', 'b', 'c']
q = ['c', 'd', 'e']
union(p, q)
print(p, q)
