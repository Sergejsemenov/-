import re
def main(input: str) -> str:
    stroka11 =Stroka
    stroka11=stroka11.replace("*"," * ")
    stroka11=stroka11.replace("/", " / ")
    stroka11=stroka11.replace("-", " - ")
    stroka11=stroka11.replace("+", " + ")
    elements = re.split(r'['' ]+', stroka11)

    if len(elements) < 3:
        print ("throws Exception //т.к. строка не является математической операцией")
        exit()
    elif len(elements) > 3:
        print("throws Exception //т.к. формат математической операции не удовлетворяет заданию")
        exit()

    operand1 = elements[0]
    operand2 = elements[2]
    if operand1.isdigit() and operand2.isdigit():
        operand1 = int(operand1)
        operand2 = int(operand2)
    else:
        print("Числа должны быть целыми числами от 1 до 10")
        exit()

    if not(1 <= operand1 <= 10) or not(1 <= operand2 <= 10):
        print ("Числа должны быть целыми числами от 1 до 10")
        exit()
    operator = elements[1]
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 // operand2
    else:
        print("Проверьте формат ввода: возможные операции: +, -, *, /")
        exit()
    return result
Stroka= input("Введите выражение для вычисления: ")

print(main(Stroka))