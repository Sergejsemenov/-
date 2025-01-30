x =input("Введите пример")
def prov():
    srez1=x[0:poz]
    if srez1.isdigit():
        if 0<int(srez1)<11:
            x1=int(srez1)
            return x1
        print ("throws Exception")
        exit()
    print("throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
    exit()
def prov1():
    srez2 = x[poz + 1:len(x)]
    if srez2.isdigit():
        if 0<int(srez2) < 11:
            x2=int(srez2)
            #print("x2=", x2)
            return x2
        print("throws Exception")
        exit()
    print("throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
    exit()
if x.find(chr(42))>-1:
    poz = x.index(chr(42))
    rez = prov() * prov1()
    print(rez)
elif x.find(chr(43))>-1:
    poz = x.index(chr(43))
    rez = prov() + prov1()
    print(rez)
elif x.find(chr(45))>-1:
    poz = x.index(chr(45))
    rez = prov() - prov1()
    print(rez)
elif x.find(chr(47)) > -1:
    poz = x.index(chr(47))
    rez=prov() / prov1()
    print (rez)
else:
    print("throws Exception //т.к. строка не является математической операцией")
