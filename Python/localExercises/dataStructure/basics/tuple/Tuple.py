t = (1, 2, 3)

print(t)

print(t[0])
print(t[1])

t2 = (1, 4, 5)

intersectionTuple = ()

for i in t2:
    if i in t:
        intersectionTuple = (i,)
        break

print(intersectionTuple)