"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0

# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)

def test_div_decimal():
    """División que da resultado decimal (float)."""
    assert div(7, 2) == 3.5
    @pytest.mark.parametrize("a,b,expected", [
        (7, 2, 3.5),
        (10, 4, 2.5),
    ])
    def test_div_parametrizado(a, b, expected):
        assert div(a, b) == expected


def test_div_negativos():    
    """División con números negativos."""
    assert div(-10, 2) == -5.0
    assert div(10, -2) == -5.0
    assert div(-10, -2) == 5.0
    @pytest.mark.parametrize("a,b,expected", [
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),
    ])

    def test_div_parametrizado(a, b, expected):
        assert div(a, b) == expected

def test_div_por_cero():
    """División por cero → debe lanzar ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
