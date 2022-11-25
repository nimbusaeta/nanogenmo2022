import random

def pasillo(etapa):
    if etapa == 1:
        with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/01-pasillo/etapa-01/phil-01.txt", encoding="UTF-8") as f:
            lines = f.readlines()
        
        number = random.randint(0, len(lines)-1)
        print(lines[number].strip())

        with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/01-pasillo/etapa-01/hombre-01.txt", encoding="UTF-8") as f:
            lines = f.readlines()
        
        number = random.randint(0, len(lines)-1)
        print(lines[number].strip())

def generar_dia_etapa_1():
    with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/01-pasillo/dia-01.txt", encoding="UTF-8") as f:
        lines = f.readlines()
    print(lines[0].strip())

    pasillo(1)

    print()

for i in range(4, 10):
    print("Día ", i)
    generar_dia_etapa_1()

