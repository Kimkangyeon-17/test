print(list(range(5, 101, 5)))

a = [i for i in range(1,100)
     if i %3 == 0 or i %5 == 0]
print(a)

a = [i for i in range(1,101)
     if i % 2 == 0 or i % 8 == 0]
print(a)