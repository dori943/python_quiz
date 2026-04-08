# quiz_game.py

import json
import os
from quiz import Quiz
from default_quizzes import get_default_quizzes

class QuizGame:
    """게임 전체를 관리하는 클래스"""
    
    DATA_FILE = "state.json"
    
    def __init__(self):
        self.quizzes = []
        self.best_score = None   # 최고 점수 (None = 아직 안 품)
        self.score_history = []
        self.load_data()
    
    # ─── 메뉴 ───
    def show_menu(self):
        """메뉴 출력"""
        print("\n" + "=" * 40)
        print("       🎯 퀴즈 게임 🎯")
        print("=" * 40)
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("=" * 40)
    
    def get_menu_choice(self):
        """메뉴 선택 입력"""
        while True:
            try:
                raw = input("메뉴를 선택하세요 (1~5): ").strip()
                if not raw:
                    print("⚠️  빈 입력입니다. 1~5 중 선택해주세요.")
                    continue
                num = int(raw)
                if num < 1 or num > 5:
                    print("⚠️  1~5 사이의 번호를 입력해주세요.")
                    continue
                return num
            except ValueError:
                print("⚠️  숫자를 입력해주세요.")
    
    def run(self):
        """메인 게임 루프"""
        print("퀴즈 게임에 오신 것을 환영합니다! 🎉")
        
        while True:
            self.show_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:
                self.play_quiz() #퀴즈 풀기
            elif choice == 2:
                self.add_quiz() #퀴즈 추가
            elif choice == 3:
                self.show_quiz_list() #퀴즈 목록
            elif choice == 4:
                self.show_score() #점수 확인
            elif choice == 5:
                self.save_data()
                print("\n👋 게임을 종료합니다. 다음에 또 만나요!")
                break
    
    # ─── 각 기능 (이후 단계에서 구현) ───
    def play_quiz(self):
        print("\n[퀴즈 풀기 - 아직 미구현]")
    
    def add_quiz(self):
        print("\n[퀴즈 추가 - 아직 미구현]")
    
    def show_quiz_list(self):
        print("\n[퀴즈 목록 - 아직 미구현]")
    
    def show_score(self):
        print("\n[점수 확인 - 아직 미구현]")
    
    def save_data(self):
        pass  # 5단계에서 구현
    
    def load_data(self):
        self.quizzes = get_default_quizzes()  # 임시