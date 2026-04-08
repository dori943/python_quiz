# quiz.py

class Quiz:
    """개별 퀴즈를 표현하는 클래스"""
    
    def __init__(self, question, choices, answer, hint=""):
        """
        Args:
            question (str): 문제 텍스트
            choices (list): 4개의 선택지 리스트
            answer (int): 정답 번호 (1~4)
            hint (str): 힌트
        """
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
    
    def display(self):
        """퀴즈를 화면에 출력"""
        print(f"\n📝 {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")
    
    def check_answer(self, user_answer):
        """정답 확인"""
        return user_answer == self.answer
    
    def to_dict(self):
        """JSON 저장용 딕셔너리 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }
    
    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 Quiz 객체 생성"""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", "")
        )