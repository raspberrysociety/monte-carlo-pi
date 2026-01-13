import random

def calcular_pi(n_pontos):
    pontos_dentro = 0
    pontos = []

    for _ in range(n_pontos):
        x = random.random()
        y = random.random()
        pontos.append((x, y))

        if x**2 + y**2 <= 1:
            pontos_dentro += 1

    pi_estimado = 4 * pontos_dentro / n_pontos
    return pi_estimado, pontos_dentro
