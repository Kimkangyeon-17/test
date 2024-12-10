'''
1. 함수를 만든다.
2. 함수의 파라미터는 2개를 받는다.
3. 함수의 기능은 두개의 파라미터를 활용해서
dict.fromkeys()함수를 사용하여
dict를 만들어 리턴한다.
4. 함수를 호출하여 리턴된 dict를 출력한다.'''

# def make_dict(x, y):
#     return dict.fromkeys(x, y)

# print(make_dict([1, 2, 3], 'a'))

# d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
# d.update({'one' : 1, 'two' : 2})
# d['three'] = 3
# print(d)

d = {'two' : 2, 'three' : '셋'}
for i in d:
    print(i, d[i])