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
        """저장된 퀴즈 목록 출력"""
        if not self.quizzes:
            print("\n📭 등록된 퀴즈가 없습니다.")
            return
        
        print(f"\n📋 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"  {i}. {quiz.question}")
            for j, choice in enumerate(quiz.choices, 1):
                marker = "✔" if j == quiz.answer else " "
                print(f"     {j}) {choice} {marker}")
            print()
    
    def show_score(self):
        print("\n[점수 확인 - 아직 미구현]")

    def save_data(self):
        """state.json에 데이터 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "score_history": self.score_history
        }
        try:
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("💾 데이터가 저장되었습니다.")
        except (IOError, OSError) as e:
            print(f"⚠️  저장 중 오류 발생: {e}")

    def load_data(self):
        """state.json에서 데이터 불러오기"""
        if not os.path.exists(self.DATA_FILE):
            print("📂 저장 파일이 없습니다. 기본 퀴즈를 불러옵니다.")
            self.quizzes = get_default_quizzes()
            return
        
        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = data.get("best_score", None)
            self.score_history = data.get("score_history", [])
            
            if not self.quizzes:
                print("⚠️  저장된 퀴즈가 없어 기본 퀴즈를 불러옵니다.")
                self.quizzes = get_default_quizzes()
            
            print(f"✅ 데이터 로드 완료! (퀴즈 {len(self.quizzes)}개)")
            
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"⚠️  파일이 손상되었습니다: {e}")
            print("기본 퀴즈 데이터로 초기화합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.score_history = []
    
    def load_data(self):
        self.quizzes = get_default_quizzes()