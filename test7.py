# l = [[1, 10, 'leehojun'], 
#      [20, 30, 'hojun'], 
#      [10, 20, 'weniv!'], 
#      [1, 2, 'hello world'], 
#      [55, 11, 'sun']]

# # 1. 글자 수 대로 정렬해주세요.

# # 2. 맨 앞에 위치한 숫자대로 정렬해주세요.

# # 3. 중앙에 위치한 값대로 정렬해주세요.

# def f(x):
#     return len(x[2])

# print(sorted(l, key=f, reverse=False))
# # print(sorted(l, key=lambda x:len(x[2]), reverse=False))

# def f2(x):
#     return x[0]

# print(sorted(l, key=f2, reverse=False))

# def f3(x):
#     return x[1]

# print(sorted(l, key=f3, reverse=False))

l = [[1, 10, 32], 
     [20, 30, 11], 
     [10, 20, 22], 
     [1, 2, 13], 
     [55, 11, 44]]

def f4(x):
    return x[0] + x[1] + x[2]

def f5(x):
    return sum(x)

print(sorted(l, key=f4))
print(sorted(l, key=f5))