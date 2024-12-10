# 문제 2
"""
도서관 관리 시스템을 만드세요.
Book 클래스를 만들고 다음 기능을 구현하세요:
- 책의 제목, 저자, 출판연도를 초기화하는 생성자
- 책 정보를 출력하는 메서드
- 책의 대여 상태를 관리하는 메서드 (대여/반납)

테스트 코드:
book1 = Book("Python Programming", "John Smith", 2023)
book1.display_info()
book1.borrow()
book1.return_book()
"""

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def display_info(self):
        status = "대여 중" if self.is_borrowed else "대여 가능"
        print(f"제목 : {self.title}")
        print(f"저자 : {self.author}")
        print(f"출판연도 : {self.year}")
        print(f"상태 : {status}")
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("대여됨")
        else:
            print("이미 대여 중")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("책이 반납됨")
        else:
            print("이미 반납됨")

book1 = Book("Python Programming", "John Smith", 2023)
book1.display_info()
book1.borrow()
book1.return_book()