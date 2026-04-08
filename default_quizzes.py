# default_quizzes.py

from quiz import Quiz

def get_default_quizzes():
    """기본 퀴즈 5개 이상 (주제: 파이썬 프로그래밍)"""
    return [
        Quiz(
            question="파이썬에서 리스트를 생성하는 올바른 방법은?",
            choices=["list = (1,2,3)", "list = [1,2,3]", 
                     "list = {1,2,3}", "list = <1,2,3>"],
            answer=2,
            hint="대괄호를 사용합니다"
        ),
        Quiz(
            question="파이썬에서 주석을 작성할 때 사용하는 기호는?",
            choices=["//", "/* */", "#", "--"],
            answer=3,
            hint="유명한 가수 이름이 기호입니다 (내입술 ..따뜻한 커피처럼)"
        ),
        Quiz(
            question="다음 중 파이썬의 반복문이 아닌 것은?",
            choices=["for", "while", "do-while", "for-in"],
            answer=3,
            hint="파이썬에는 없는 C 스타일 반복문입니다"
        ),
        Quiz(
            question="len('Hello')의 결과는?",
            choices=["4", "5", "6", "에러"],
            answer=2,
            hint="각 문자를 세어보세요"
        ),
        Quiz(
            question="파이썬에서 None의 타입은?",
            choices=["int", "str", "NoneType", "bool"],
            answer=3,
            hint="None만의 고유한 타입이 있습니다"
        ),
    ]