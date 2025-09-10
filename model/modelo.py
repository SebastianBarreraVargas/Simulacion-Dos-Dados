import random

def simular_dado(lado):
    lanzamientos = [1, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    probabilidades = []

    for n in lanzamientos:
        favorables = 0

        for _ in range(n):
            resultado1 = random.randint(1,6)
            resultado2 = random.randint(1,6)
            if resultado1 & resultado2 == lado:
                favorables += 1

        probabilidad = (favorables / n) * 100
        probabilidades.append(probabilidad)

    return tuple(probabilidades), lanzamientos