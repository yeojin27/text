class LoginManager:
    def __init__(self, correct_id, correct_pw, max_attempts=3):
        self.correct_id = correct_id
        self.correct_pw = correct_pw
        self.max_attempts = max_attempts

    def login(self):
        for count in range(self.max_attempts):
            user_id = input("ID를 입력하세요: ")
            user_pw = input("PASSWORD를 입력하세요: ")

            if user_id == self.correct_id and user_pw == self.correct_pw:
                print("로그인 되었습니다.")
                return True
            else:
                print("아이디 또는 비밀번호가 틀렸습니다.")

        print("로그인 3회 실패로 프로그램을 종료합니다.")
        return False


class RankingBoard:
    def __init__(self):
        self.records = []

    def add_record(self, nickname, tries):
        record = {
            "name": nickname,
            "tries": tries
        }

        self.records.append(record)

        with open("memo.txt","a",encoding="utf-8")as file:
            file.write(f"{nickname}, {tries}\n")

    def show_ranking(self):
        if len(self.records) == 0:
            print("등록된 기록이 없습니다.")
            return

        self.records.sort(key=lambda x: (x["tries"], x["name"]))

        print("----명예의 전당----")

        for i in range(min(3, len(self.records))):
            print(f"{i + 1}위 {self.records[i]['name']} {self.records[i]['tries']}회")



import random


class UpDownGame:
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.target = random.randint(start, end)
        self.tries = 0

    def input_number(self):
        while True:
            try:
                number = int(input("숫자를 입력하세요: "))
                return number
            except ValueError:
                print("숫자만 입력해주세요.")

    def give_hint(self, guess):
        if guess < self.target:
            print("UP")
        elif guess > self.target:
            print("DOWN")

    def give_extra_hint(self, guess):
        difference = abs(self.target - guess)

        if difference <= 5:
            print("힌트: 거의 다 왔습니다.")
        elif difference <= 15:
            print("힌트: 가까워지고 있습니다.")
        else:
            print("힌트: 아직 멉니다.")

    def play(self):
        print(f"{self.start}부터 {self.end} 사이의 숫자를 맞혀보세요.")

        while True:
            guess = self.input_number()
            self.tries += 1

            if guess == self.target:
                print(f"정답입니다! 시도 횟수: {self.tries}회")
                nickname = input("닉네임을 입력하세요: ")
                return nickname, self.tries

            self.give_hint(guess)
            self.give_extra_hint(guess)


class App:
    def __init__(self):
        self.login_manager = LoginManager("admin", "1234")
        self.ranking_board = RankingBoard()

    def print_menu(self):
        print()
        print("1. 게임 시작")
        print("2. 랭킹 보기")
        print("3. 게임 종료")

    def input_menu(self):
        while True:
            try:
                menu = int(input("메뉴를 선택하세요: "))
                return menu
            except ValueError:
                print("숫자만 입력해주세요.")

    def run(self):
        if not self.login_manager.login():
            return

        while True:
            self.print_menu()
            menu = self.input_menu()

            if menu == 1:
                game = UpDownGame()
                nickname, tries = game.play()
                self.ranking_board.add_record(nickname, tries)

            elif menu == 2:
                self.ranking_board.show_ranking()

            elif menu == 3:
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 메뉴입니다.")


app = App()
app.run()