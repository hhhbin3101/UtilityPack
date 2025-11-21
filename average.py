def average_score():
    score_list = []
    print("점수 입력 : ")

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

average_score()