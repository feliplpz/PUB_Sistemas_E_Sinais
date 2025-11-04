import sys
from pathlib import Path

import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_less

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.lotka_volterra import calcular_equilibrio, lotka_volterra, resolver_sistema


class TestLotkaVolterra:

    def test_retorna_lista_com_dois_elementos(self):
        """Testa se a função retorna uma lista com 2 elementos."""
        result = lotka_volterra(0.0, [1.0, 1.0], 1.0, 1.0, 1.0, 1.0)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_derivada_presas_sem_predadores(self):
        """Testa crescimento exponencial de presas sem predadores."""
        alpha = 2.0
        x1, x2 = 1.0, 0.0
        dx1_dt, dx2_dt = lotka_volterra(0.0, [x1, x2], alpha, 1.0, 1.0, 1.0)
        assert dx1_dt == alpha * x1

    def test_derivada_predadores_sem_presas(self):
        """Testa decaimento exponencial de predadores sem presas."""
        gamma = 2.0
        x1, x2 = 0.0, 1.0
        dx1_dt, dx2_dt = lotka_volterra(0.0, [x1, x2], 1.0, 1.0, gamma, 1.0)
        assert dx2_dt == -gamma * x2

    def test_interacao_predador_presa(self):
        """Testa termo de interação predador-presa."""
        alpha, beta, gamma, delta = 6.0, 2.0, 2.0, 3.0
        x1, x2 = 1.0, 1.0
        dx1_dt, dx2_dt = lotka_volterra(0.0, [x1, x2], alpha, beta, gamma, delta)

        assert dx1_dt == alpha * x1 - beta * x1 * x2
        assert dx2_dt == -gamma * x2 + delta * x1 * x2

    def test_valores_positivos_geram_valores_finitos(self):
        """Testa se inputs positivos geram outputs finitos."""
        result = lotka_volterra(0.0, [1.0, 1.0], 6.0, 2.0, 2.0, 3.0)
        assert all(np.isfinite(result))


class TestCalcularEquilibrio:
    """Testes para a função calcular_equilibrio."""

    def test_retorna_tupla_com_dois_elementos(self):
        """Testa se retorna tupla com 2 elementos."""
        result = calcular_equilibrio(6.0, 2.0, 2.0, 3.0)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_calculo_matematico_correto(self):
        """Testa se o cálculo matemático está correto."""
        alpha, beta, gamma, delta = 6.0, 2.0, 2.0, 3.0
        x1_eq, x2_eq = calcular_equilibrio(alpha, beta, gamma, delta)

        assert x1_eq == gamma / delta
        assert x2_eq == alpha / beta
        assert_allclose(x1_eq, 2.0 / 3.0)
        assert_allclose(x2_eq, 3.0)

    def test_valores_positivos(self):
        """Testa se os valores de equilíbrio são positivos."""
        x1_eq, x2_eq = calcular_equilibrio(6.0, 2.0, 2.0, 3.0)
        assert x1_eq > 0
        assert x2_eq > 0

    def test_diferentes_parametros(self):
        """Testa com diferentes conjuntos de parâmetros."""
        params_list = [
            (1.0, 1.0, 1.0, 1.0),
            (10.0, 2.0, 3.0, 4.0),
            (0.5, 0.1, 0.2, 0.3),
        ]

        for alpha, beta, gamma, delta in params_list:
            x1_eq, x2_eq = calcular_equilibrio(alpha, beta, gamma, delta)
            assert x1_eq > 0
            assert x2_eq > 0
            assert_allclose(x1_eq, gamma / delta)
            assert_allclose(x2_eq, alpha / beta)


class TestResolverSistema:
    """Testes para a função resolver_sistema."""

    def test_retorna_tres_arrays(self):
        """Testa se retorna 3 arrays."""
        result = resolver_sistema(
            6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=10.0, n_points=100
        )
        assert len(result) == 3
        assert all(isinstance(arr, np.ndarray) for arr in result)

    def test_tamanho_correto_dos_arrays(self):
        """Testa se os arrays têm o tamanho correto."""
        n_points = 100
        t, x1, x2 = resolver_sistema(
            6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=10.0, n_points=n_points
        )
        assert len(t) == n_points
        assert len(x1) == n_points
        assert len(x2) == n_points

    def test_tempo_comeca_em_zero(self):
        """Testa se o tempo começa em zero."""
        t, x1, x2 = resolver_sistema(6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=10.0)
        assert_allclose(t[0], 0.0)

    def test_tempo_termina_em_t_max(self):
        """Testa se o tempo termina em t_max."""
        t_max = 15.0
        t, x1, x2 = resolver_sistema(6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=t_max)
        assert_allclose(t[-1], t_max)

    def test_condicoes_iniciais_corretas(self):
        """Testa se as condições iniciais são respeitadas."""
        x1_0, x2_0 = 2.5, 1.5
        t, x1, x2 = resolver_sistema(6.0, 2.0, 2.0, 3.0, x1_0, x2_0, t_max=10.0)
        assert_allclose(x1[0], x1_0, rtol=1e-5)
        assert_allclose(x2[0], x2_0, rtol=1e-5)

    def test_populacoes_nao_negativas(self):
        """Testa se as populações permanecem não-negativas."""
        t, x1, x2 = resolver_sistema(6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=15.0)
        assert np.all(x1 >= 0), "População de presas ficou negativa"
        assert np.all(x2 >= 0), "População de predadores ficou negativa"

    def test_sem_valores_nan_ou_inf(self):
        """Testa se não há valores NaN ou Inf na solução."""
        t, x1, x2 = resolver_sistema(6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=15.0)
        assert np.all(np.isfinite(t))
        assert np.all(np.isfinite(x1))
        assert np.all(np.isfinite(x2))

    def test_oscilacao_periodica(self):
        """Testa se há comportamento oscilatório."""
        t, x1, x2 = resolver_sistema(
            6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=20.0, n_points=2000
        )

        x1_max = np.max(x1)
        x1_min = np.min(x1)

        assert x1_max > x1[0], "População de presas deve oscilar acima do valor inicial"
        assert (
            x1_min < x1[0]
        ), "População de presas deve oscilar abaixo do valor inicial"

    def test_defasagem_temporal(self):
        """Testa se há defasagem entre picos de presas e predadores."""
        t, x1, x2 = resolver_sistema(
            6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=20.0, n_points=2000
        )

        idx_max_x1 = np.argmax(x1[:1000])
        idx_max_x2 = np.argmax(x2[:1000])

        assert (
            idx_max_x2 > idx_max_x1
        ), "Pico de predadores deve ocorrer após pico de presas"

    def test_parametros_diferentes(self):
        """Testa com diferentes conjuntos de parâmetros."""
        params_sets = [
            (3.0, 1.0, 1.0, 1.5),
            (10.0, 3.0, 4.0, 5.0),
            (1.0, 0.5, 0.5, 1.0),
        ]

        for alpha, beta, gamma, delta in params_sets:
            t, x1, x2 = resolver_sistema(
                alpha, beta, gamma, delta, 1.0, 1.0, t_max=10.0
            )
            assert len(t) > 0
            assert np.all(np.isfinite(x1))
            assert np.all(np.isfinite(x2))
            assert np.all(x1 >= 0)
            assert np.all(x2 >= 0)


class TestIntegracaoSistema:
    """Testes de integração do sistema completo."""

    def test_equilibrio_e_estavel_no_ponto_de_equilibrio(self):
        """Testa se começando no equilíbrio o sistema permanece lá."""
        alpha, beta, gamma, delta = 6.0, 2.0, 2.0, 3.0
        x1_eq, x2_eq = calcular_equilibrio(alpha, beta, gamma, delta)

        t, x1, x2 = resolver_sistema(
            alpha, beta, gamma, delta, x1_eq, x2_eq, t_max=5.0, n_points=100
        )

        assert_allclose(x1, x1_eq, rtol=1e-3, atol=1e-3)
        assert_allclose(x2, x2_eq, rtol=1e-3, atol=1e-3)

    def test_conservacao_energia_orbita_fechada(self):
        """Testa se a órbita é aproximadamente fechada."""
        t, x1, x2 = resolver_sistema(
            6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=50.0, n_points=5000
        )

        x1_inicial = x1[0]
        x2_inicial = x2[0]

        tolerancia = 0.1
        indices_proximos = np.where(
            (np.abs(x1 - x1_inicial) < tolerancia)
            & (np.abs(x2 - x2_inicial) < tolerancia)
        )[0]

        assert (
            len(indices_proximos) > 1
        ), "Sistema deve retornar próximo ao ponto inicial (órbita fechada)"


class TestCasosEspeciais:
    """Testes para casos especiais e edge cases."""

    def test_tempo_muito_pequeno(self):
        """Testa simulação com tempo muito pequeno."""
        t, x1, x2 = resolver_sistema(
            6.0, 2.0, 2.0, 3.0, 1.0, 1.0, t_max=0.01, n_points=2
        )
        assert len(t) >= 1
        assert_allclose(t[0], 0.0)
        assert_allclose(x1[0], 1.0, rtol=1e-2)
        assert_allclose(x2[0], 1.0, rtol=1e-2)

    def test_condicao_inicial_zero_presas(self):
        """Testa com população inicial de presas zero."""
        t, x1, x2 = resolver_sistema(6.0, 2.0, 2.0, 3.0, 0.0, 1.0, t_max=10.0)
        assert_allclose(x1, 0.0)
        assert np.all(x2 <= 1.0), "Predadores devem diminuir sem presas"

    def test_condicao_inicial_zero_predadores(self):
        """Testa com população inicial de predadores zero."""
        t, x1, x2 = resolver_sistema(6.0, 2.0, 2.0, 3.0, 1.0, 0.0, t_max=10.0)
        assert_allclose(x2, 0.0)
        assert np.all(x1 >= 1.0), "Presas devem crescer sem predadores"

    def test_parametros_muito_pequenos(self):
        """Testa com parâmetros muito pequenos."""
        t, x1, x2 = resolver_sistema(0.1, 0.1, 0.1, 0.1, 1.0, 1.0, t_max=10.0)
        assert np.all(np.isfinite(x1))
        assert np.all(np.isfinite(x2))

    def test_parametros_muito_grandes(self):
        """Testa com parâmetros muito grandes."""
        t, x1, x2 = resolver_sistema(
            100.0, 50.0, 50.0, 100.0, 1.0, 1.0, t_max=1.0, n_points=1000
        )
        assert np.all(np.isfinite(x1))
        assert np.all(np.isfinite(x2))


@pytest.mark.parametrize(
    "alpha,beta,gamma,delta",
    [
        (6.0, 2.0, 2.0, 3.0),
        (1.0, 1.0, 1.0, 1.0),
        (10.0, 3.0, 4.0, 5.0),
    ],
)
def test_parametrizado_diferentes_parametros(alpha, beta, gamma, delta):
    """Teste parametrizado com diferentes conjuntos de parâmetros."""
    x1_eq, x2_eq = calcular_equilibrio(alpha, beta, gamma, delta)
    assert x1_eq > 0
    assert x2_eq > 0

    t, x1, x2 = resolver_sistema(alpha, beta, gamma, delta, 1.0, 1.0, t_max=10.0)
    assert np.all(x1 >= 0)
    assert np.all(x2 >= 0)
    assert np.all(np.isfinite(x1))
    assert np.all(np.isfinite(x2))
