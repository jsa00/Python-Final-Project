from models.specialized_books import GeneralBook, EBook
from utils.helpers import get_menu_choice, get_isbn

books = {}
isbn_set = set()

# ====================
# 도서 등록 함수
# ====================
def register_book():
    print("\n===== 도서 등록 =====")

    title = input("도서명: ").strip()

    # 공백 차단
    if not title:
        print(">> 도서명은 비워둘 수 없습니다.")
        return

    author = input("저자: ").strip()

    if not author:
        print(">> 저자는 비워둘 수 없습니다.")
        return

    isbn = get_isbn()

    # ISBN 중복 여부 확인
    if isbn in isbn_set:
        print(">> 이미 등록된 ISBN입니다.")
        return

    print("\n>> 도서 종류를 선택하세요.")
    print("1. 일반 단행본")
    print("2. 전자 도서")

    while True:
        try:
            book_type = int(input("선택: ").strip())

            if book_type not in (1, 2):
                print(">> 1 또는 2를 입력하세요.")
                continue

            break

        except ValueError:
            print(">> 잘못된 입력입니다. 숫자를 입력하세요.")

    if book_type == 1:
        publisher = input("출판사: ").strip()

        if not publisher:
            print(">> 출판사는 비워둘 수 없습니다.")
            return

        book = GeneralBook(
            title,
            author,
            isbn,
            publisher
        )

        category = "일반 단행본"

    else:
        file_format = input("파일 형식: ").strip()

        if not file_format:
            print(">> 파일 형식은 비워둘 수 없습니다.")
            return

        book = EBook(
            title,
            author,
            isbn,
            file_format
        )

        category = "전자 도서"

    books[isbn] = {
        "book": book,
        "category": category
    }

    isbn_set.add(isbn)

    print(f">> '{title}' 도서가 등록되었습니다.")

# ====================
# 전체 도서 조회
# ====================
def show_all_books():
    print("\n===== 전체 도서 목록 =====")

    if not books:
        print(">> 등록된 도서가 없습니다.")
        return

    for isbn, info in books.items():
        book = info["book"]

        print(f"\nISBN: {isbn}")
        print(f"종류: {info['category']}")

        if book.is_available():
            print("상태: 대여 가능")
        else:
            print("상태: 대여 중")

# ====================
# 도서 검색
# ====================
def search_book():
    print("\n===== 도서 검색 =====")

    isbn = get_isbn()

    if isbn not in books:
        print(">> 해당 ISBN의 도서를 찾을 수 없습니다.")
        return

    book = books[isbn]["book"]
    book.show_info()

# ====================
# 대여/반납 처리
# ====================
def borrow_or_return():
    print("\n===== 대여 / 반납 =====")

    isbn = get_isbn()

    # 등록되지 않은 ISBN인지 확인
    if isbn not in isbn_set:
        print(">> 등록되지 않은 ISBN입니다.")
        return

    book = books[isbn]["book"]

    print(f"\n도서명: {book.get_title()}")
    print(f"저자: {book.get_author()}")

    # 현재 대여 가능 여부에 따라 상태 전환
    if book.is_available():

        # 현재 상태: 대여 가능
        # → 대여 처리
        result = book.borrow()

        if result:
            print(">> 도서가 대여되었습니다.")
            print("현재 상태: 대여 중")

    else:

        # 현재 상태: 대여 중
        # → 반납 처리
        book.return_book()

        print(">> 도서가 반납되었습니다.")
        print("현재 상태: 대여 가능")

# ====================
# 도서 검색
# ====================
def search_book():
    print("\n===== 도서 검색 =====")

    isbn = input(">> 검색할 ISBN을 입력하세요: ").strip()

    if not isbn:
        print(">> ISBN을 입력해야 합니다.")
        return

    if isbn not in books:
        print(">> 해당 ISBN의 도서를 찾을 수 없습니다.")
        return

    info = books[isbn]
    book = info["book"]

    book.show_info()

# ====================
# 메인 메뉴 (반복 실행)
# ====================

while True:
    print("\n===== 도서 관리 시스템 =====")
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 검색")
    print("4. 대여/반납")
    print("5. 종료")
    print("============================")

    menu = input(">> 메뉴를 선택하세요: ")

    # 1. 도서 등록
    if menu == "1":
        register_book()

    # 2. 전체 도서 조회
    elif menu == "2":
        show_all_books()

    # 3. 도서 검색
    elif menu == "3":
        search_book()

    # 4. 대여/반납
    elif menu == "4":
        borrow_or_return()

    # 5. 종료
    elif menu == "5":
        print(">> 도서 관리 시스템을 종료합니다.")
        break

    # 잘못된 메뉴 입력
    else:
        print(">> 잘못된 메뉴입니다. 1~5 중에서 선택하세요.")