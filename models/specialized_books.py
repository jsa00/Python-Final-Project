from .base_book import Book

# 일반 단행본
class GeneralBook(Book):
    def __init__(self, title, author, isbn, publisher):
        super().__init__(title, author, isbn)
        self.__publisher = publisher

    def show_info(self):
        print("\n===== 일반 단행본 =====")
        super().show_info()
        print(f"출판사: {self.__publisher}")


# 전자 도서
class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.__file_format = file_format

    def show_info(self):
        print("\n===== 전자 도서 =====")
        super().show_info()
        print(f"파일 형식: {self.__file_format}")