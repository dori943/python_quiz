# quiz_game.py

import json
import os
import random
from datetime import datetime
from quiz import Quiz
from default_quizzes import get_default_quizzes

class QuizGame:
    """게임 전체를 관리하는 클래스"""
    
    DATA_FILE = "state.json"
    
    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.has_played = False
        self.score_history = []
        self.load_data()
    
    # ─── 메뉴 ───
    def show_menu(self):
        print("\n" + "=" * 40)
        print("       🎯 퀴즈 게임 🎯")
        print("=" * 40)
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 퀴즈 삭제")
        print("  6. 퀴즈 초기화")
        print("  7. 종료")
        print("=" * 40)
    
    def get_menu_choice(self):
        while True:
            try:
                raw = input("메뉴를 선택하세요 (1~7): ").strip()
                if not raw:
                    print("⚠️  빈 입력입니다. 1~7 중 선택해주세요.")
                    continue
                num = int(raw)
                if num < 1 or num > 7:
                    print("⚠️  1~7 사이의 번호를 입력해주세요.")
                    continue
                return num
            except ValueError:
                print("⚠️  숫자를 입력해주세요.")
    
    def run(self):
        print("!!퀴즈 게임를 시작합니다!!")
        while True:
            self.show_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.delete_quiz()
            elif choice == 6:
                self.reset_game()
            elif choice == 7:
                self.save_data()
                print("\n👋 게임을 종료합니다. 다음에 또 만나요!")
                break
    
    # ─── 퀴즈 풀기 ───
    def play_quiz(self):
        if not self.quizzes:
            print("\n📭 등록된 퀴즈가 없습니다.")
            return
        
        total = len(self.quizzes)
        print(f"\n총 {total}개의 퀴즈가 있습니다.")
        
        # 문제 수 선택
        while True:
            try:
                raw = input(f"몇 문제를 풀까요? (1~{total}): ").strip()
                if not raw:
                    print("⚠️  빈 입력입니다.")
                    continue
                count = int(raw)
                if count < 1 or count > total:
                    print(f"⚠️  1~{total} 사이의 숫자를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("⚠️  숫자를 입력해주세요.")
        
        # 문제 섞기
        selected = random.sample(self.quizzes, count)
        score = 0
        
        print(f"\n🚀 {count}문제를 시작합니다!\n")
        
        for i, quiz in enumerate(selected, 1):
            print(f"[{i}/{count}]", end="")
            quiz.display()
            print("  H. 힌트 보기")
            
            hint_used = False
            
            # 정답 입력
            while True:
                try:
                    raw = input("정답을 입력하세요 (1~4, 힌트는 H): ").strip().upper()
                    if not raw:
                        print("⚠️  빈 입력입니다.")
                        continue
                    
                    # 힌트 요청
                    if raw == "H":
                        if quiz.hint:
                            print(f"💡 힌트: {quiz.hint}")
                            hint_used = True
                        else:
                            print("💡 힌트가 없습니다.")
                        continue
                    
                    ans = int(raw)
                    if ans < 1 or ans > 4:
                        print("⚠️  1~4 사이의 번호를 입력해주세요.")
                        continue
                    break
                except ValueError:
                    print("⚠️  숫자를 입력하거나 H를 입력해주세요.")
            
            # 정답 확인
            if quiz.check_answer(ans):
                if hint_used:
                    print("✅ 정답입니다! (힌트 사용으로 0.5점)")
                    score += 0.5
                else:
                    print("✅ 정답입니다! (+1점)")
                    score += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번이었습니다.")
        
        # 결과 출력
        print("\n" + "=" * 40)
        print(f"🏁 결과: {count}문제 중 {score}점 획득!")
        print("=" * 40)
        
        # 최고 점수 갱신
        if not self.has_played or score > self.best_score:
            self.best_score = score
            print("🏆 새로운 최고 점수입니다!")
        
        self.has_played = True   # 한 번이라도 풀었음을 기록
        
        # 기록 저장
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "total": count,
            "score": score
        }
        self.score_history.append(record)
        self.save_data()
    
    # ─── 퀴즈 추가 ───
    def add_quiz(self):
        print("\n📝 새 퀴즈 추가")
        print("-" * 40)
        
        # 문제 입력
        while True:
            question = input("문제를 입력하세요: ").strip()
            if not question:
                print("⚠️  문제를 입력해주세요.")
                continue
            break
        
        # 선택지 4개 입력
        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}번을 입력하세요: ").strip()
                if not choice:
                    print("⚠️  선택지를 입력해주세요.")
                    continue
                choices.append(choice)
                break
        
        # 정답 번호 입력
        while True:
            try:
                raw = input("정답 번호를 입력하세요 (1~4): ").strip()
                if not raw:
                    print("⚠️  빈 입력입니다.")
                    continue
                answer = int(raw)
                if answer < 1 or answer > 4:
                    print("⚠️  1~4 사이의 번호를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("⚠️  숫자를 입력해주세요.")
        
        # 힌트 입력 (선택)
        hint = input("힌트를 입력하세요 (없으면 Enter): ").strip()
        
        # Quiz 객체 생성 후 추가
        new_quiz = Quiz(question=question, choices=choices, answer=answer, hint=hint)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("✅ 퀴즈가 추가되었습니다!")
    
    # ─── 퀴즈 목록 ───
    def show_quiz_list(self):
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
    
    # ─── 점수 확인 ───
    def show_score(self):
        print("\n" + "=" * 40)
        print("         🏆 점수 확인")
        print("=" * 40)
        
        if not self.has_played:
            print("  아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"  최고 점수: {self.best_score}점")
        
        if self.score_history:
            print("\n  📜 게임 기록")
            print("-" * 40)
            for record in self.score_history:
                print(f"  {record['date']} | {record['total']}문제 | {record['score']}점")
        else:
            print("\n  게임 기록이 없습니다.")
        
        print("=" * 40)

    
    
    
    # ─── 저장 / 불러오기 ───
    def save_data(self):
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "score_history": self.score_history
        }
        try:
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except (IOError, OSError) as e:
            print(f"⚠️  저장 중 오류 발생: {e}")
    
    def load_data(self):
        if not os.path.exists(self.DATA_FILE):
            print("📂 저장 파일이 없습니다. 기본 퀴즈를 불러옵니다.")
            self.quizzes = get_default_quizzes()
            return
        
        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
            self.best_score = data.get("best_score", None)
            self.has_played = data.get("has_played", False)
            self.score_history = data.get("score_history", [])
            
            if not self.quizzes:
                print("⚠️  저장된 퀴즈가 없어 기본 퀴즈를 불러옵니다.")
                self.quizzes = get_default_quizzes()
            else:
                print(f"✅ 데이터 로드 완료! (퀴즈 {len(self.quizzes)}개)")
        
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"⚠️  파일이 손상되었습니다: {e}")
            print("기본 퀴즈 데이터로 초기화합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.has_played = False
            self.score_history = []