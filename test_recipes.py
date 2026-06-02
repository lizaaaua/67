import pytest

from recipes import Ingredient

def test_ingredient_creation():
    ingredient = Ingredient("Мука", 500, "г")

    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"

def test_ingredient_str():
    ingredient = Ingredient("Мука", 500, "г")

    assert str(ingredient) == "Мука: 500.0 г"

def test_ingredient_equal_same_name_and_unit():
    first = Ingredient("Мука", 500, "г")
    second = Ingredient("Мука", 100, "г")

    assert first == second

def test_ingredient_not_equal_different_name():
    first = Ingredient("Мука", 500, "г")
    second = Ingredient("Сахар", 500, "г")

    assert first != second

def test_ingredient_not_equal_different_unit():
    first = Ingredient("Мука", 500, "г")
    second = Ingredient("Мука", 500, "кг")

    assert first != second

def test_ingredient_quantity_must_be_positive():
    with pytest.raises(ValueError):
        Ingredient("Мука", 0, "г")
