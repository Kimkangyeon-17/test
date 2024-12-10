# li = list(range(1, 1001))
# li_2 = [j for j in li if j % 2 == 0 or j % 5 == 0]
# ki = sum(li_2)
# di = len(li_2)
# print(li)
# print(li_2)
# print(ki)
# print(di)

# while True:
    # N = int(input())
    # if N == 0:
    #     break
    # else:
    #     print(N)

for i in range(2, 10):
    for j in range(1, 10):
        if j > 5:
            break
        print(f'{i} X {j} = {i*j}')