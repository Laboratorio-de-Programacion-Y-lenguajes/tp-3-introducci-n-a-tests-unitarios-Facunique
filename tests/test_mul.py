"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul
from pytest import approx


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_mul_por_cero():
    """Multiplicar por cero."""
    assert mul(5, 0) == 0
    assert mul(0, 5) == 0
    @pytest.mark.parametrize("a,b,expected", [
        (5, 0, 0),
        (0, 5, 0),
    ])
    def test_mul_parametrizado(a, b, expected):
        assert mul(a, b) == expected

def test_mul_negativos():
    """Multiplicar dos números negativos (resultado positivo)."""
    assert mul(-3, -4) == 12
    @pytest.mark.parametrize("a,b,expected", [
        (-3, -4, 12),
        (-5, -2, 10),
    ])
    def test_mul_parametrizado(a, b, expected):
        assert mul(a, b) == expected

def test_mul_positivo_y_negativo():
    """Multiplicar un positivo y un negativo (resultado negativo)."""
    assert mul(3, -4) == -12
    assert mul(-3, 4) == -12
    @pytest.mark.parametrize("a,b,expected", [
        (3, -4, -12),
        (-3, 4, -12),
    ])
    def test_mul_parametrizado(a, b, expected):
        assert mul(a, b) == expected

def test_mul_por_uno():
    """Multiplicar por 1 (elemento neutro)."""
    assert mul(5, 1) == 5
    assert mul(1, 5) == 5
    @pytest.mark.parametrize("a,b,expected", [
        (5, 1, 5),
        (1, 5, 5),
    ])
    def test_mul_parametrizado(a, b, expected):
        assert mul(a, b) == expected

def test_mul_decimales():
    """Multiplicar dos decimales."""
    assert mul(1.5, 2.0) == 3.0
    @pytest.mark.parametrize("a,b,expected", [
        (1.5, 2.0, approx(3.0)),
        (0.1, 0.2, approx(0.02)),
    ])
    def test_mul_parametrizado(a, b, expected):
        assert mul(a, b) == expected    

