# main.py

from quiz_game import QuizGame

def main():
    game = None # game이 정의되기 전에 오류나면 NameError 발생
    try:
        game = QuizGame()
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  프로그램이 중단되었습니다.")
        if game:
            game.save_data()
        print("종료되었습니다.")

if __name__ == "__main__":
    main()