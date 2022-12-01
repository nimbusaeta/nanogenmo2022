import random

def radio():
    print("VOZ 1 (en la radio): Bien, excursionistas, ¡arriba! Despertad y no olvidéis los descansos porque hoy hace ¡frrrrío!")
    print("VOZ 2: Hace frío todos los días. ¿Dónde creías que estabas, en Miami?")
    print()


def pasillo(etapa):
    if etapa == 1:
        with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/01-pasillo/etapa-01/phil-01.txt", encoding="UTF-8") as f:
            lines = f.readlines()
        number = random.randint(0, len(lines)-1)
        print("PHIL:", lines[number].strip())

        with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/01-pasillo/etapa-01/hombre-01.txt", encoding="UTF-8") as f:
            lines = f.readlines()
        number = random.randint(0, len(lines)-1)
        print("HUÉSPED:", lines[number].strip())

        print()

def lancaster(etapa):
    if etapa == 1:
        with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/02-lancaster/etapa-01/phil-01.txt", encoding="UTF-8") as f:
            lines = f.readlines()
        number = random.randint(0, len(lines)-1)
        print("PHIL:", lines[number].strip())

        print()
        


def generar_dia_etapa_1():
    # radio
    print("Suena 'I got you, babe' en la radio a las 6 en punto de la mañana.")
    radio()

    # pasillo
    print("Phil sale de la habitación y se encuentra con otro huésped en el rellano.")
    with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/01-pasillo/dia-01.txt", encoding="UTF-8") as f:
        lines = f.readlines()
    print("HUÉSPED:", lines[0].strip())
    pasillo(1)

    # Lancaster
    print("Phil baja a desayunar. Se le acerca la casera, la señora Lancaster.")
    with open("C:/Users/Leticia/Documents/GitHub/nanogenmo2022/textos/02-lancaster/dia-01.txt", encoding="UTF-8") as f:
        lines = f.readlines()
    print("SEÑORA LANCASTER:", lines[0].strip())
    lancaster(1)

    print()

for i in range(4, 10):
    print("Día ", i)
    generar_dia_etapa_1()

