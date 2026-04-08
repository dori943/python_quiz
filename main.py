# main.py

from quiz_game import QuizGame

def main():
    try:
        game = QuizGame()
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  프로그램이 중단되었습니다. 데이터를 저장합니다...")
        game.save_data()
        print("종료되었습니다.")

if __name__ == "__main__":
    main()