"""
주어진 리스트에서 랜덤하게 3개의 아이템을 선택하고, 1부터 10 사이의 랜덤한 숫자를 더해
새로운 리스트를 만드는 프로그램을 작성하세요.

예시:
입력 리스트: ["apple", "banana", "orange", "grape", "kiwi", "mango"]
출력 예시: ['banana+7', 'kiwi+3', 'apple+9']
"""

import random
def random_fruit_combination(fruits):
    result = []

    for _ in range(3):
        fruit = random.choice(fruits)
        number = random.randint(1, 10)
        result.append(f"{fruit} + {number}")
    
    return result

fruits = ["apple", "banana", "orange", "grape", "kiwi", "mango"]
print(random_fruit_combination(fruits))