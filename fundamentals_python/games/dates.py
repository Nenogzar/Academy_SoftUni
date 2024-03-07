# Develop a program that is capable of:
#1) Read a string from standard input, in the format dd/mm/yyyy.
#2) Display the date on standard output, in dd/mm/yyyy format.
#3) Display the date in standard output in words. E.g.: “February 1, 2024”.
#4) Check if the date is valid.
#5) Add days to a date.
#6) Calculate the difference between two dates in years.

def ler_data(texto_data: str) -> tuple[int, int, int]:
    texto_separado = texto_data.split('/')
    dia = int(texto_separado[0])
    mes = int(texto_separado[1])
    ano = int(texto_separado[2])
    data = dia, mes, ano
    return data


def eh_ano_bissexto(a: int) -> bool:
    """The year is a leap year when:
        1) It is a multiple of 4;
        2) It is not a multiple of 100, unless it is a multiple of 400."""
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            return False
        return True
    return False


dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def data_eh_valida(d: int, m: int, a: int) -> bool:
    if 1 <= m <= 12:
        dias = dias_no_mes[m - 1]
        if m == 2 and eh_ano_bissexto(a):
            dias = 29
        if 1 <= d <= dias:
            return True
    return False


def exibir_data(d: int, m: int, a: int) -> None:
    print(f"{d:02d}/{m:02d}/{a:04d}")


mes_por_extenso = ['January February March',
                    'April', 'May', 'June', 'July',
                    'August September October',
                    'November December']


def exibir_data_por_extenso(d: int, m: int, a: int) -> None:
    # 03/01/2024 ~> "March 1, 2024"
    # 02/28/2024 ~> "February 28, 2024"
    mes = mes_por_extenso[m - 1]
    primeiro = 'º' if d == 1 else ''
    print(f"{d}{primeiro} of {mes} of {a}")


def adicionar_dias_a_data(dias: int,
                          data_dia: int,
                          data_mes: int,
                          data_ano: int) -> tuple[int, int, int]:
    pass


def compara_datas(d1: int, m1: int, a1: int,
                  d2: int, m2: int, a2: int) -> int:
    """Compares two dates. Returns 0 if the dates are the same.
            Returns 1 if date 1 is greater than date 2.
            Returns -1 if date 2 is greater than date 1."""
    pass


def diferenca_entre_datas_em_anos(d1: int, m1: int, a1: int,
                                  d2: int, m2: int, a2: int) -> int:
    """Calculates the difference in years between two dates.
            The calculation must start with the difference between the values of the years, a1 - a2 (if a1 >= a2),
            or a2 - a1 (otherwise). If the month of the earliest date is greater than the month of the earliest date
            new, subtract 1 from the difference between years. If the months are the same, and the day of the date
            oldest date is greater than the day of the newest date, subtract 1 from the difference between years."""
    pass


d1, m1, a1 = ler_data(input("Report to data 1: "))
d2, m2, a2 = ler_data(input("Report to data 2: "))
c = compara_datas(d1, m1, a1, d2, m2, a2)
if c == 0:
    print("The dates are the same.")
elif c == 1:
    print("Date 1 is greater than date 2.")
else:
    print("Date 1 is less than date 2.")

str_data = input("Data report: ")
dia, mes, ano = ler_data(str_data)
exibir_data(dia, mes, ano)
if data_eh_valida(dia, mes, ano):
    print("Valid data.")
    exibir_data_por_extenso(dia, mes, ano)
    d2, m2, a2 = adicionar_dias_a_data(1400, dia, mes, ano)
    exibir_data(d2, m2, a2)
    diferenca = diferenca_entre_datas_em_anos(dia, mes, ano,
                                              d2, m2, a2)
    print(f"Difference in years: {diferenca}.")
else:
    print("Invalid data.")
