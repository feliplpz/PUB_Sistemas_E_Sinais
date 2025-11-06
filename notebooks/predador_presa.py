# %% [markdown]
# # Modelo Predador-Presa (Lotka-Volterra)
#
# ## Descrição do Modelo
#
# Este é um modelo clássico em biologia que descreve a dinâmica de duas populações:
# - **x₁(t)**: População de herbívoros (presas)
# - **x₂(t)**: População de carnívoros (predadores)
#
# ### Equações Diferenciais
#
# $$\frac{dx_1}{dt} = \alpha \cdot x_1 - \beta \cdot x_1 \cdot x_2$$
#
# $$\frac{dx_2}{dt} = -\gamma \cdot x_2 + \delta \cdot x_1 \cdot x_2$$
#
# Onde:
# - **α**: Taxa de crescimento das presas (sem predadores)
# - **β**: Taxa de predação (impacto dos encontros nas presas)
# - **γ**: Taxa de mortalidade dos predadores (sem presas)
# - **δ**: Eficiência de conversão (crescimento de predadores por presa consumida)
#
# ### Pontos de Equilíbrio
#
# - **(0, 0)**: Extinção de ambas as populações
# - **(γ/δ, α/β)**: Equilíbrio não-trivial

# %%
from typing import Tuple, List
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy.typing import NDArray

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11


# %% [markdown]
# ## Definição do Sistema de EDOs

# %%
def lotka_volterra(
        t: float,
        y: List[float],
        alpha: float,
        beta: float,
        gamma: float,
        delta: float
) -> List[float]:
    """
    Sistema de equações diferenciais do modelo Lotka-Volterra.

    Parameters
    ----------
    t : float
        Tempo atual
    y : List[float]
        Vetor de estado [x1, x2] onde x1 é a população de presas
        e x2 é a população de predadores
    alpha : float
        Taxa de crescimento das presas
    beta : float
        Taxa de predação
    gamma : float
        Taxa de mortalidade dos predadores
    delta : float
        Eficiência de conversão

    Returns
    -------
    List[float]
        Derivadas [dx1/dt, dx2/dt]
    """
    x1, x2 = y
    dx1_dt = alpha * x1 - beta * x1 * x2
    dx2_dt = -gamma * x2 + delta * x1 * x2
    return [dx1_dt, dx2_dt]


def resolver_sistema(
        alpha: float,
        beta: float,
        gamma: float,
        delta: float,
        x1_0: float,
        x2_0: float,
        t_max: float = 50.0,
        n_points: int = 1000
) -> Tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """
    Resolve o sistema de EDOs numericamente usando o método de Runge-Kutta.

    Parameters
    ----------
    alpha : float
        Taxa de crescimento das presas
    beta : float
        Taxa de predação
    gamma : float
        Taxa de mortalidade dos predadores
    delta : float
        Eficiência de conversão
    x1_0 : float
        População inicial de presas
    x2_0 : float
        População inicial de predadores
    t_max : float, optional
        Tempo final de simulação (padrão: 50.0)
    n_points : int, optional
        Número de pontos para avaliação (padrão: 1000)

    Returns
    -------
    Tuple[NDArray, NDArray, NDArray]
        Tupla contendo (t, x1, x2) onde t é o vetor de tempos,
        x1 é a população de presas e x2 é a população de predadores
    """
    y0 = [x1_0, x2_0]
    t_span = (0.0, t_max)
    t_eval = np.linspace(0.0, t_max, n_points)

    sol = solve_ivp(
        lotka_volterra,
        t_span,
        y0,
        args=(alpha, beta, gamma, delta),
        t_eval=t_eval,
        method='RK45',
        dense_output=True
    )

    return sol.t, sol.y[0], sol.y[1]


def calcular_equilibrio(
        alpha: float,
        beta: float,
        gamma: float,
        delta: float
) -> Tuple[float, float]:
    """
    Calcula o ponto de equilíbrio não-trivial do sistema.

    Parameters
    ----------
    alpha : float
        Taxa de crescimento das presas
    beta : float
        Taxa de predação
    gamma : float
        Taxa de mortalidade dos predadores
    delta : float
        Eficiência de conversão

    Returns
    -------
    Tuple[float, float]
        Tupla (x1_eq, x2_eq) com as populações de equilíbrio
    """
    x1_eq = gamma / delta
    x2_eq = alpha / beta
    return x1_eq, x2_eq


# %% [markdown]
# ## Simulação com Parâmetros Padrão
#
# Valores utilizados conforme exemplo do texto:
# - α = 6.0 (presas crescem rapidamente)
# - β = 2.0 (predação moderada)
# - γ = 2.0 (predadores morrem moderadamente)
# - δ = 3.0 (eficiência alta de conversão)
# - Condições iniciais: x₁(0) = 1.0, x₂(0) = 1.0

# %%
alpha: float = 6.0
beta: float = 2.0
gamma: float = 2.0
delta: float = 3.0

x1_0: float = 1.0
x2_0: float = 1.0

t_max: float = 15.0

t, x1, x2 = resolver_sistema(alpha, beta, gamma, delta, x1_0, x2_0, t_max)
x1_eq, x2_eq = calcular_equilibrio(alpha, beta, gamma, delta)

print(f"Ponto de Equilíbrio:")
print(f"  x₁ (presas) = {x1_eq:.3f}")
print(f"  x₂ (predadores) = {x2_eq:.3f}")

# %% [markdown]
# ## Visualização: Populações ao Longo do Tempo

# %%
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(t, x1, 'b-', linewidth=2.5, label='Presas (x₁)', alpha=0.8)
ax.plot(t, x2, 'r-', linewidth=2.5, label='Predadores (x₂)', alpha=0.8)
ax.axhline(y=x1_eq, color='b', linestyle='--', linewidth=1.5, alpha=0.5,
           label=f'Equilíbrio x₁ = {x1_eq:.2f}')
ax.axhline(y=x2_eq, color='r', linestyle='--', linewidth=1.5, alpha=0.5,
           label=f'Equilíbrio x₂ = {x2_eq:.2f}')

ax.set_xlabel('Tempo (t)', fontsize=14, fontweight='bold')
ax.set_ylabel('População', fontsize=14, fontweight='bold')
ax.set_title('Dinâmica Predador-Presa (Lotka-Volterra)', fontsize=16, fontweight='bold')
ax.legend(fontsize=12, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### Observações
#
# 1. **Comportamento Cíclico**: As populações oscilam periodicamente
# 2. **Defasagem Temporal**: O pico de predadores ocorre após o pico de presas
# 3. **Causalidade**:
#    - Aumento de presas leva ao aumento de predadores
#    - Aumento de predadores leva à diminuição de presas
#    - Diminuição de presas leva à diminuição de predadores
#    - Diminuição de predadores leva ao aumento de presas

# %% [markdown]
# ## Diagrama de Fase (Retrato de Fase)
#
# Mostra a relação direta entre as duas populações, eliminando a variável tempo.

# %%
fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(x1, x2, 'purple', linewidth=2.5, label='Trajetória', alpha=0.8)
ax.plot(x1_0, x2_0, 'go', markersize=15, label='Início', zorder=5)
ax.plot(x1_eq, x2_eq, 'r*', markersize=20, label='Equilíbrio', zorder=5)

n_arrows: int = 8
for i in range(0, len(t), len(t) // n_arrows):
    if i < len(t) - 1:
        dx = x1[i + 1] - x1[i]
        dy = x2[i + 1] - x2[i]
        ax.arrow(x1[i], x2[i], dx * 0.3, dy * 0.3, head_width=0.05,
                 head_length=0.05, fc='black', ec='black', alpha=0.5)

ax.set_xlabel('População de Presas (x₁)', fontsize=14, fontweight='bold')
ax.set_ylabel('População de Predadores (x₂)', fontsize=14, fontweight='bold')
ax.set_title('Diagrama de Fase: Predador vs Presa', fontsize=16, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### Interpretação
#
# - A trajetória forma uma órbita fechada em torno do ponto de equilíbrio
# - O sistema é conservativo: não converge para o equilíbrio, mas orbita indefinidamente
# - A amplitude da órbita depende das condições iniciais

# %% [markdown]
# ## Análise de Sensibilidade
#
# Análise de como a variação de cada parâmetro afeta o comportamento do sistema.

# %% [markdown]
# ### Variação de α (Taxa de Crescimento das Presas)

# %%
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

alphas: List[float] = [3.0, 6.0, 9.0, 12.0]
colors: List[str] = ['blue', 'green', 'orange', 'red']

for idx, (alpha_var, color) in enumerate(zip(alphas, colors)):
    ax = axes[idx // 2, idx % 2]

    t_var, x1_var, x2_var = resolver_sistema(alpha_var, beta, gamma, delta, x1_0, x2_0, t_max)
    x1_eq_var, x2_eq_var = calcular_equilibrio(alpha_var, beta, gamma, delta)

    ax.plot(t_var, x1_var, color=color, linewidth=2, label='Presas', alpha=0.8)
    ax.plot(t_var, x2_var, color=color, linewidth=2, linestyle='--', label='Predadores', alpha=0.8)
    ax.axhline(y=x1_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)
    ax.axhline(y=x2_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)

    ax.set_xlabel('Tempo (t)', fontsize=12)
    ax.set_ylabel('População', fontsize=12)
    ax.set_title(f'α = {alpha_var:.1f} (Eq: x₁={x1_eq_var:.2f}, x₂={x2_eq_var:.2f})',
                 fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

plt.suptitle('Sensibilidade ao Parâmetro α (Taxa de Crescimento das Presas)',
             fontsize=16, fontweight='bold', y=1.00)
plt.tight_layout()
plt.show()

# %% [markdown]
# Conclusão: Aumentar α (crescimento de presas) aumenta a população de equilíbrio de predadores (x₂).

# %% [markdown]
# ### Variação de β (Taxa de Predação)

# %%
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

betas: List[float] = [1.0, 2.0, 3.0, 4.0]
colors: List[str] = ['blue', 'green', 'orange', 'red']

for idx, (beta_var, color) in enumerate(zip(betas, colors)):
    ax = axes[idx // 2, idx % 2]

    t_var, x1_var, x2_var = resolver_sistema(alpha, beta_var, gamma, delta, x1_0, x2_0, t_max)
    x1_eq_var, x2_eq_var = calcular_equilibrio(alpha, beta_var, gamma, delta)

    ax.plot(t_var, x1_var, color=color, linewidth=2, label='Presas', alpha=0.8)
    ax.plot(t_var, x2_var, color=color, linewidth=2, linestyle='--', label='Predadores', alpha=0.8)
    ax.axhline(y=x1_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)
    ax.axhline(y=x2_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)

    ax.set_xlabel('Tempo (t)', fontsize=12)
    ax.set_ylabel('População', fontsize=12)
    ax.set_title(f'β = {beta_var:.1f} (Eq: x₁={x1_eq_var:.2f}, x₂={x2_eq_var:.2f})',
                 fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

plt.suptitle('Sensibilidade ao Parâmetro β (Taxa de Predação)',
             fontsize=16, fontweight='bold', y=1.00)
plt.tight_layout()
plt.show()

# %% [markdown]
# Conclusão: Aumentar \beta (predação) diminui a população de equilíbrio de predadores (x₂).

# %% [markdown]
# ### Variação de γ (Taxa de Mortalidade dos Predadores)

# %%
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

gammas: List[float] = [1.0, 2.0, 3.0, 4.0]
colors: List[str] = ['blue', 'green', 'orange', 'red']

for idx, (gamma_var, color) in enumerate(zip(gammas, colors)):
    ax = axes[idx // 2, idx % 2]

    t_var, x1_var, x2_var = resolver_sistema(alpha, beta, gamma_var, delta, x1_0, x2_0, t_max)
    x1_eq_var, x2_eq_var = calcular_equilibrio(alpha, beta, gamma_var, delta)

    ax.plot(t_var, x1_var, color=color, linewidth=2, label='Presas', alpha=0.8)
    ax.plot(t_var, x2_var, color=color, linewidth=2, linestyle='--', label='Predadores', alpha=0.8)
    ax.axhline(y=x1_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)
    ax.axhline(y=x2_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)

    ax.set_xlabel('Tempo (t)', fontsize=12)
    ax.set_ylabel('População', fontsize=12)
    ax.set_title(f'γ = {gamma_var:.1f} (Eq: x₁={x1_eq_var:.2f}, x₂={x2_eq_var:.2f})',
                 fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

plt.suptitle('Sensibilidade ao Parâmetro γ (Mortalidade dos Predadores)',
             fontsize=16, fontweight='bold', y=1.00)
plt.tight_layout()
plt.show()

# %% [markdown]
# Conclusão: Aumentar γ (mortalidade de predadores) aumenta a população de equilíbrio de presas (x₁).

# %% [markdown]
# ### Variação de δ (Eficiência de Conversão)

# %%
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

deltas: List[float] = [1.5, 3.0, 4.5, 6.0]
colors: List[str] = ['blue', 'green', 'orange', 'red']

for idx, (delta_var, color) in enumerate(zip(deltas, colors)):
    ax = axes[idx // 2, idx % 2]

    t_var, x1_var, x2_var = resolver_sistema(alpha, beta, gamma, delta_var, x1_0, x2_0, t_max)
    x1_eq_var, x2_eq_var = calcular_equilibrio(alpha, beta, gamma, delta_var)

    ax.plot(t_var, x1_var, color=color, linewidth=2, label='Presas', alpha=0.8)
    ax.plot(t_var, x2_var, color=color, linewidth=2, linestyle='--', label='Predadores', alpha=0.8)
    ax.axhline(y=x1_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)
    ax.axhline(y=x2_eq_var, color=color, linestyle=':', linewidth=1, alpha=0.5)

    ax.set_xlabel('Tempo (t)', fontsize=12)
    ax.set_ylabel('População', fontsize=12)
    ax.set_title(f'δ = {delta_var:.1f} (Eq: x₁={x1_eq_var:.2f}, x₂={x2_eq_var:.2f})',
                 fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

plt.suptitle('Sensibilidade ao Parâmetro δ (Eficiência de Conversão)',
             fontsize=16, fontweight='bold', y=1.00)
plt.tight_layout()
plt.show()

# %% [markdown]
# Conclusão: Aumentar δ (eficiência) diminui a população de equilíbrio de presas (x₁).

# %% [markdown]
# ## Comparação de Diferentes Condições Iniciais

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

initial_conditions: List[Tuple[float, float, str]] = [
    (0.5, 0.5, 'blue'),
    (1.0, 1.0, 'green'),
    (2.0, 2.0, 'red'),
    (x1_eq, x2_eq, 'purple')
]

for x1_init, x2_init, color in initial_conditions:
    t_ic, x1_ic, x2_ic = resolver_sistema(alpha, beta, gamma, delta, x1_init, x2_init, t_max)
    ax1.plot(t_ic, x1_ic, color=color, linewidth=2, alpha=0.7,
             label=f'x₁(0)={x1_init:.1f}, x₂(0)={x2_init:.1f}')
    ax1.plot(t_ic, x2_ic, color=color, linewidth=2, linestyle='--', alpha=0.7)

ax1.set_xlabel('Tempo (t)', fontsize=13, fontweight='bold')
ax1.set_ylabel('População', fontsize=13, fontweight='bold')
ax1.set_title('Evolução Temporal', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

for x1_init, x2_init, color in initial_conditions:
    t_ic, x1_ic, x2_ic = resolver_sistema(alpha, beta, gamma, delta, x1_init, x2_init, t_max)
    label = f'({x1_init:.1f}, {x2_init:.1f})'
    if x1_init == x1_eq:
        label = 'Equilíbrio'
    ax2.plot(x1_ic, x2_ic, color=color, linewidth=2.5, alpha=0.7, label=label)
    ax2.plot(x1_init, x2_init, 'o', color=color, markersize=10)

ax2.plot(x1_eq, x2_eq, 'r*', markersize=20, label='Ponto de Equilíbrio', zorder=10)
ax2.set_xlabel('População de Presas (x₁)', fontsize=13, fontweight='bold')
ax2.set_ylabel('População de Predadores (x₂)', fontsize=13, fontweight='bold')
ax2.set_title('Diagrama de Fase', fontsize=14, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.suptitle('Efeito das Condições Iniciais', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Observação Importante
#
# - Cada condição inicial gera uma órbita diferente
# - Todas as órbitas são fechadas (ciclos periódicos)
# - As órbitas não convergem para o ponto de equilíbrio
# - O sistema é estruturalmente instável (centro não hiperbólico)

# %% [markdown]
# ## Experimento: Caça de 30% dos Predadores
#
# Simulação do efeito de eliminar 30% dos predadores em um momento específico.

# %%
t1_hunt, x1_hunt1, x2_hunt1 = resolver_sistema(alpha, beta, gamma, delta, x1_0, x2_0, t_max=5.0)

x1_hunt_restart: float = x1_hunt1[-1]
x2_hunt_restart: float = x2_hunt1[-1] * 0.7

t2_hunt, x1_hunt2, x2_hunt2 = resolver_sistema(
    alpha, beta, gamma, delta, x1_hunt_restart, x2_hunt_restart, t_max=15.0
)
t2_hunt = t2_hunt + 5.0

t_ref, x1_ref, x2_ref = resolver_sistema(alpha, beta, gamma, delta, x1_0, x2_0, t_max=20.0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

ax1.plot(t_ref, x1_ref, 'b-', linewidth=2, label='Presas (sem caça)', alpha=0.7)
ax1.plot(t_ref, x2_ref, 'r-', linewidth=2, label='Predadores (sem caça)', alpha=0.7)
ax1.plot(t1_hunt, x1_hunt1, 'b-', linewidth=2.5, label='Presas (com caça)')
ax1.plot(t1_hunt, x2_hunt1, 'r-', linewidth=2.5, label='Predadores (com caça)')
ax1.plot(t2_hunt, x1_hunt2, 'b-', linewidth=2.5)
ax1.plot(t2_hunt, x2_hunt2, 'r-', linewidth=2.5)
ax1.axvline(x=5, color='black', linestyle='--', linewidth=2, label='Caça (t=5)')

ax1.set_xlabel('Tempo (t)', fontsize=13, fontweight='bold')
ax1.set_ylabel('População', fontsize=13, fontweight='bold')
ax1.set_title('Efeito da Caça de 30% dos Predadores em t=5', fontsize=15, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

ax2.plot(x1_ref, x2_ref, 'purple', linewidth=2, label='Sem caça', alpha=0.7)
ax2.plot(x1_hunt1, x2_hunt1, 'green', linewidth=2.5, label='Com caça (antes)')
ax2.plot(x1_hunt2, x2_hunt2, 'orange', linewidth=2.5, label='Com caça (depois)')
ax2.plot(x1_hunt_restart, x2_hunt_restart, 'ro', markersize=12, label='Momento da caça', zorder=5)
ax2.plot(x1_eq, x2_eq, 'r*', markersize=20, label='Equilíbrio', zorder=10)

ax2.set_xlabel('População de Presas (x₁)', fontsize=13, fontweight='bold')
ax2.set_ylabel('População de Predadores (x₂)', fontsize=13, fontweight='bold')
ax2.set_title('Mudança de Órbita no Diagrama de Fase', fontsize=15, fontweight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %% [markdown]
# ### Interpretação
#
# - A caça não leva ao equilíbrio
# - O sistema muda para uma órbita diferente
# - A nova órbita tem amplitude diferente
# - As populações continuam oscilando indefinidamente

# %% [markdown]
# ## Resumo e Conclusões
#
# ### Comportamento do Sistema
#
# 1. **Oscilações Periódicas**: As populações oscilam indefinidamente com período constante
# 2. **Dependência das Condições Iniciais**: A amplitude das oscilações depende das populações iniciais
# 3. **Ponto de Equilíbrio Instável**: O equilíbrio não-trivial existe, mas não é atrativo
# 4. **Defasagem Temporal**: Picos de predadores ocorrem após picos de presas
#
# ### Sensibilidade dos Parâmetros
#
# | Parâmetro | Aumento | Efeito em x₁_eq | Efeito em x₂_eq |
# |-----------|---------|-----------------|-----------------|
# | α (crescimento presas) | ↑ | - | ↑ |
# | β (predação) | ↑ | - | ↓ |
# | γ (mortalidade predadores) | ↑ | ↑ | - |
# | δ (eficiência conversão) | ↑ | ↓ | - |
#
# ### Limitações do Modelo
#
# - Não considera capacidade de carga do ambiente
# - Assume interações lineares entre populações
# - Ignora fatores externos (clima, doenças, etc.)
# - Modelo simplificado para populações reais
#
# ### Aplicações Práticas
#
# - Gestão de recursos pesqueiros
# - Controle de pragas agrícolas
# - Conservação de espécies ameaçadas
# - Epidemiologia (modelo SIR é similar)

# %% [markdown]
# ## Área Interativa: Teste Seus Próprios Parâmetros
#
# Experimente alterar os valores abaixo e execute a célula para visualizar o resultado.

# %%
alpha_custom: float = 8.0
beta_custom: float = 2.5
gamma_custom: float = 3.0
delta_custom: float = 2.0

x1_0_custom: float = 1.5
x2_0_custom: float = 0.8

t_max_custom: float = 25.0

t_custom, x1_custom, x2_custom = resolver_sistema(
    alpha_custom, beta_custom, gamma_custom, delta_custom,
    x1_0_custom, x2_0_custom, t_max_custom
)
x1_eq_custom, x2_eq_custom = calcular_equilibrio(
    alpha_custom, beta_custom, gamma_custom, delta_custom
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

ax1.plot(t_custom, x1_custom, 'b-', linewidth=2.5, label='Presas')
ax1.plot(t_custom, x2_custom, 'r-', linewidth=2.5, label='Predadores')
ax1.axhline(y=x1_eq_custom, color='b', linestyle='--', alpha=0.5)
ax1.axhline(y=x2_eq_custom, color='r', linestyle='--', alpha=0.5)
ax1.set_xlabel('Tempo (t)', fontsize=13)
ax1.set_ylabel('População', fontsize=13)
ax1.set_title(
    f'Simulação Customizada\n(α={alpha_custom}, β={beta_custom}, γ={gamma_custom}, δ={delta_custom})',
    fontsize=14, fontweight='bold'
)
ax1.legend(fontsize=12)
ax1.grid(True, alpha=0.3)

ax2.plot(x1_custom, x2_custom, 'purple', linewidth=2.5)
ax2.plot(x1_0_custom, x2_0_custom, 'go', markersize=12, label='Início')
ax2.plot(x1_eq_custom, x2_eq_custom, 'r*', markersize=20, label='Equilíbrio')
ax2.set_xlabel('Presas (x₁)', fontsize=13)
ax2.set_ylabel('Predadores (x₂)', fontsize=13)
ax2.set_title('Diagrama de Fase', fontsize=14, fontweight='bold')
ax2.legend(fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"\nResultados da Simulação Customizada:")
print(f"   Ponto de Equilíbrio: x₁ = {x1_eq_custom:.3f}, x₂ = {x2_eq_custom:.3f}")
print(f"   População máxima de presas: {np.max(x1_custom):.3f}")
print(f"   População máxima de predadores: {np.max(x2_custom):.3f}")
print(f"   População mínima de presas: {np.min(x1_custom):.3f}")
print(f"   População mínima de predadores: {np.min(x2_custom):.3f}")

# %%
