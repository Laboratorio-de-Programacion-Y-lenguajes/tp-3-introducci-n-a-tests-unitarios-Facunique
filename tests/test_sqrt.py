"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
#   - Raíz de un número negativo → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)

def test_sqrt_cero():
    """Raíz de 0 (resultado: 0.0)."""
    assert sqrt(0) == 0.0
    @pytest.mark.parametrize("x,expected", [
        (0, 0.0),
    ])
    def test_sqrt_parametrizado(x, expected):
        assert sqrt(x) == expected

def test_sqrt_no_cuadrado_perfecto():
    """Raíz de un número que no es cuadrado perfecto (resultado decimal)."""
    assert sqrt(2) == pytest.approx(1.41421356237)
    @pytest.mark.parametrize("x,expected", [
        (2, pytest.approx(1.41421356237)),
        (3, pytest.approx(1.73205080757)),
    ])
    def test_sqrt_parametrizado(x, expected):
        assert sqrt(x) == expected

def test_sqrt_negativo():
    """Raíz de un número negativo → debe lanzar ValueError."""
    with pytest.raises(ValueError):
        sqrt(-4)


