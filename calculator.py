def calculator():
    num1 = float(input("첫 번째 숫자 입력 : "))
    op = input("연산자(+, -, *, /) 입력 : ")
    num2 = float(input("두 번째 숫자 입력 : "))

    if op == '+':
        print(f"{num1} + {num2} = {num1 + num2}")

    elif op == '-':
        print(f"{num1} - {num2} = {num1 - num2}")

    elif op == '*':
        print(f"{num1} * {num2} = {num1 * num2}")

    elif op == '/':
        if num2 == 0:
            print("0으로는 나눌 수 없습니다.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")

    else:
        print("연산자를 잘못 입력하였습니다.")

calculator()
