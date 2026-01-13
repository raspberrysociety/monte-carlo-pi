# Estimativa do Valor de Pi (π)
**Estimativa de π pelo Método de Monte Carlo**

O método de **Monte Carlo** estima o valor de $\pi$ simulando a distribuição de pontos aleatórios em uma área geométrica.

## Conceito Geométrico
A simulação baseia-se em um **quadrado unitário** que contém um **quadrante de círculo**:
* A área do quadrado é 1, e a área do quadrante de círculo é `A = π/4`
* A razão entre os pontos que caem dentro do círculo ($N_{dentro}$) e o total de pontos gerados ($N_{total}$) aproxima-se da razão entre as áreas: $$\frac{N_{dentro}}{N_{total}} \approx \frac{\pi}{4}$$

# A Fórmula
* Para encontrar o valor aproximado de $\pi$, multiplicamos a razão por 4: $$\pi \approx 4 \times \frac{N_{dentro}}{N_{total}}$$

# Algoritmo de Cálculo
O processo segue quatro passos principais:
1. **Gerar Pontos:** Criar pares aleatórios $(x, y)$ com $x, y \in [0, 1]$.
2. **Verificar Condição:** Um ponto está dentro do círculo se satisfazer a inequação:
    $$x^2 + y^2 \le 1$$
4. **Contar:** Armazenar a quantidade de pontos dentro ($N_{dentro}$) e o total de tentativas ($N_{total}$).
5. **Calcular:** Aplicar a fórmula de aproximação para obter o resultado.
