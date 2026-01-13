from calcular_pi import calcular_pi

def main():
    n_pontos = int(input("Digite o número de pontos para a simulação: "))

    pi_estimado, pontos, pontos_dentro = calcular_pi(n_pontos)

    print(f"Pontos dentro do círculo: {pontos_dentro}")
    print(f"Total de pontos: {n_pontos}")
    print(f"Estimativa de π: {pi_estimado}")

if __name__ == "__main__":
    main()