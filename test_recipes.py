import pytest

from recipes import Ingredient, Recipe

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

def test_recipe_creation():
    ingredient = Ingredient("Мука", 500, "г")
    recipe = Recipe("Блины", [ingredient])

    assert recipe.title == "Блины"
    assert recipe.ingredients == [ingredient]


def test_recipe_add_new_ingredient():
    recipe = Recipe("Блины")
    ingredient = Ingredient("Мука", 500, "г")

    recipe.add_ingredient(ingredient)

    assert len(recipe) == 1
    assert recipe.ingredients[0] == ingredient


def test_recipe_add_same_ingredient_sums_quantity():
    recipe = Recipe("Блины")

    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Мука", 100, "г"))

    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 600.0


def test_recipe_scale_returns_new_recipe():
    recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])

    scaled_recipe = recipe.scale(2)

    assert scaled_recipe is not recipe
    assert scaled_recipe.title == "Блины"
    assert scaled_recipe.ingredients[0].quantity == 1000.0
    assert recipe.ingredients[0].quantity == 500.0


def test_recipe_scale_with_bad_ratio():
    recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])

    with pytest.raises(ValueError):
        recipe.scale(0)


def test_recipe_len():
    recipe = Recipe("Блины")

    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Яйцо", 2, "шт"))

    assert len(recipe) == 2
