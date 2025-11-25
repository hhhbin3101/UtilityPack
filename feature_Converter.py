class Converter:
    @staticmethod
    def c_m(c):
        return c / 100

    @staticmethod
    def m_c(m):
        return m * 100

    @staticmethod
    def g_kg(g):
        return g / 1000

    @staticmethod
    def kg_g(kg):
        return kg * 1000


want_function = input("원하는 기능을 입력하세요 ()안에 있는걸로... (cm_to_m, m_to_cm, g_to_kg, kg_to_g): ")

if want_function == "cm_to_m":
    c = float(input("cm 값을 입력하세요: "))
    print(Converter.c_m(c))

elif want_function == "m_to_cm":
    m = float(input("m 값을 입력하세요: "))
    print(Converter.m_c(m))

elif want_function == "g_to_kg":
    g = float(input("g 값을 입력하세요: "))
    print(Converter.g_kg(g))

elif want_function == "kg_to_g":
    kg = float(input("kg 값을 입력하세요: "))
    print(Converter.kg_g(kg))

else:
    print("지원하지 않는 기능입니다.")
