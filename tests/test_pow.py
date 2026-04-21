"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_pow_exponente_cero():
    """Cualquier número elevado a 0 (resultado: 1)."""
    assert pow_(5, 0) == 1
    assert pow_(-3, 0) == 1
    @pytest.mark.parametrize("a,expected", [
        (5, 1),
        (-3, 1),
    ])
    def test_pow_parametrizado(a, expected):
        assert pow_(a, 0) == expected

def test_pow_exponente_uno():
    """Número elevado a 1 (resultado: el mismo número)."""
    assert pow_(5, 1) == 5
    assert pow_(-3, 1) == -3
    @pytest.mark.parametrize("a,expected", [
        (5, 5),
        (-3, -3),
    ])
    def test_pow_parametrizado(a, expected):
        assert pow_(a, 1) == expected

def test_pow_base_negativa_exponente_par():
    """Base negativa con exponente par (resultado positivo)."""
    assert pow_(-2, 4) == 16
    @pytest.mark.parametrize("a,b,expected", [
        (-2, 4, 16),
        (-3, 2, 9),
    ])
    def test_pow_parametrizado(a, b, expected):
        assert pow_(a, b) == expected

def test_pow_exponente_decimal():
    """Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)."""
    assert pow_(9, 0.5) == 3
    @pytest.mark.parametrize("a,b,expected", [
        (9, 0.5, 3),
        (16, 0.25, 2),
    ])
    def test_pow_parametrizado(a, b, expected):
        assert pow_(a, b) == expected


