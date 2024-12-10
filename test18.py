def solution(array):
    if len(array) == 1:
        return array[0]
    arr = counter(array)
    if arr.most_common(1)[0][1] == len(array):
        return array[0]
    one, two = arr.most_common(2)
    if one[1] == two[1]:
        return -1
    return one[0]

solution([1, 2, 3, 3, 3, 4])