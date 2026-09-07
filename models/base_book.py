class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True

    # 도서명 getter
    def get_title(self):
        return self.__title

    # 저자 getter
    def get_author(self):
        return self.__author

    # ISBN getter
    def get_isbn(self):
        return self.__isbn

    # 대여 가능 여부 getter
    def is_available(self):
        return self.__is_available

    # 대여 처리
    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    # 반납 처리
    def return_book(self):
        self.__is_available = True

    # 도서 상세 정보
    def show_info(self):
        status = "대여 가능" if self.__is_available else "대여 중"

        print(f"도서명: {self.__title}")
        print(f"저자: {self.__author}")
        print(f"ISBN: {self.__isbn}")
        print(f"상태: {status}")