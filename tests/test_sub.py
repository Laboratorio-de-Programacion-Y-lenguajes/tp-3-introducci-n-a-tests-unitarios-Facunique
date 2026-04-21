"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub
from pytest import approx


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_sub_resta_negativos():
    """Restar un número mayor al primero (resultado negativo)."""
    assert sub(2, 5) == -3
    @pytest.mark.parametrize("a,b,expected", [
        (2, 5, -3),
        (0, 1, -1),
    ])
    def test_sub_parametrizado(a, b, expected):
        assert sub(a, b) == expected

def test_sub_resta_con_cero():
    """Restar cero."""
    assert sub(5, 0) == 5
    assert sub(0, 5) == -5
    @pytest.mark.parametrize("a,b,expected", [
        (5, 0, 5),
        (0, 5, -5),
    ])
    def test_sub_parametrizado(a, b, expected):
        assert sub(a, b) == expected   

def test_sub_resta_negativos():
    """Restar dos números negativos."""
    assert sub(-5, -2) == -3
    @pytest.mark.parametrize("a,b,expected", [
        (-5, -2, -3),
        (-10, -5, -5),
    ])
    def test_sub_parametrizado(a, b, expected):
        assert sub(a, b) == expected

def test_sub_resta_decimales():
    """Restar dos números decimales."""
    assert sub(5.5, 2.5) == 3.0
    @pytest.mark.parametrize("a,b,expected", [
        (5.5, 2.5, 3.0),
        (0.1, 0.2, approx(-0.1)),
    ])
    def test_sub_parametrizado(a, b, expected):
        assert sub(a, b) == expected
