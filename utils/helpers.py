def get_menu_choice():

    while True:
        try:
            choice = int(input(">> 메뉴를 선택하세요: ").strip())

            # 메뉴 번호는 1~5만 허용
            if choice < 1 or choice > 5:
                print(">> 1~5 사이의 숫자를 입력하세요.")
                continue

            return choice

        except ValueError:
            print(">> 잘못된 입력입니다. 숫자를 입력하세요.")


def get_isbn():

    while True:
        isbn = input(">> ISBN을 입력하세요: ").strip()

        if not isbn:
            print(">> ISBN은 비워둘 수 없습니다.")
            continue

        return isbn