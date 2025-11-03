"""
Módulo com implementação do modelo Predador-Presa de Lotka-Volterra.
"""

from typing import Tuple, List
import numpy as np
from scipy.integrate import solve_ivp
from numpy.typing import NDArray


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
