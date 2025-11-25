import sys
# 각자 사용 모듈 있으면 import 해주세요

# 본인이 만든 기능 함수로 추가해주세요
def average_score():
    score_list = []
    print("점수 입력(계산 원할 경우 0 입력)")

    while True:
        user_input = input("> ").strip()

        if user_input == '0':
            break
        if not user_input:
            print("다시 입력하세요")
            continue
        try:
            current_score = float(user_input)
            score_list.append(current_score)
        except ValueError:
            print("올바른 형식으로 입력해주세요")

    if score_list:
        total = sum(score_list)
        count = len(score_list)
        average = total / count

        print(f"평균 : {average:.2f}")
    else:
        print("계산 오류")

def main():
    """
    프로그램의 메인 메뉴입니다.
    팀원들은 여기 메뉴 이름을 수정하여 충돌(Conflict)을 유도하세요.
    """
    while True:
        print("[ 팀 프로젝트 ] 미니 도구 모음")
        print("1. 단위 변환기")
        print("2. 간단 계산기")
        print("3. 점수 평균 계산")
        print("4. 문자열 처리")
        print("5. 비밀번호 생성기")
        print("0. 프로그램 종료")

        choice = input(">")

        if choice == '1':
            # 단위 변환기 함수 불러오기 해주세요
        elif choice == '2':
            # 간단 계산기 함수 불러오기 해주세요
        elif choice == '3':
            average_score()
        elif choice == '4':
            # 문자열 처리 함수 불러오기 해주세요
        elif choice == '5':
            # 비밀번호 생성기 함수 불러오기 해주세요
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()