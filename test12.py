s = {1, 2, 3, 4}
ss = {3, 4, 5, 6}

print(s^ss)

set.symmetric_difference(s, ss)

# 1. 다음은 python 강좌 학생들의 시험 점수를 딕셔너리로 나타낸 것입니다.
    
    

student_score = {
        '홍의': 97,
        '원희': 60,
        '동해': 77,
        '변수': 79,
        '창현': 89,
}
    

# - 학생들의 **총점**을 구하는 코드를 작성하세요.
# - 학생들의 **평균 점수**를 구하는 코드를 작성하세요.
# - 점수가 가장 **높은** 학생의 이름과 그 점수를 구하는 코드를 작성하세요.
# - 점수가 가장 **낮은** 학생의 이름과 그 점수를 구하는 코드를 작성하세요.

total = sum(student_score.values())
print(total)
print(total/len(student_score))
max_name = max(student_score, key=student_score.get)
print(max_name, student_score[max_name])
min_name = min(student_score)
print(min_name, student_score[min_name])

like = ['볶음밥', '라면', '국수', '파스타', '치킨', '짜장면', '국밥']
like_menu = set(like)
dislike = ['국밥', '짬뽕', '찜닭', '파스타', '국수', '카레', '덮밥']
dislike_menu = set(dislike)

last_menu = list(like_menu- dislike_menu)
print(last_menu)


final_menu = []
for menu in like:
    if menu not in dislike:
        final_menu.append(menu)
print(final_menu)