import pytest

from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

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

def test_shopping_list_add_recipe():
    recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])
    shopping_list = ShoppingList()

    shopping_list.add_recipe(recipe, 2)
    result = shopping_list.get_list()

    assert len(result) == 1
    assert result[0].name == "Мука"
    assert result[0].quantity == 1000.0
    assert result[0].unit == "г"


def test_shopping_list_add_recipe_bad_portions():
    recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])
    shopping_list = ShoppingList()

    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, 0)


def test_shopping_list_remove_recipe():
    first_recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])
    second_recipe = Recipe("Омлет", [Ingredient("Яйцо", 2, "шт")])
    shopping_list = ShoppingList()

    shopping_list.add_recipe(first_recipe, 1)
    shopping_list.add_recipe(second_recipe, 1)
    shopping_list.remove_recipe("Блины")

    result = shopping_list.get_list()

    assert len(result) == 1
    assert result[0].name == "Яйцо"


def test_shopping_list_remove_missing_recipe():
    recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])
    shopping_list = ShoppingList()

    shopping_list.add_recipe(recipe, 1)
    shopping_list.remove_recipe("Пирог")

    result = shopping_list.get_list()

    assert len(result) == 1
    assert result[0].name == "Мука"


def test_shopping_list_same_ingredients_are_summed():
    first_recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])
    second_recipe = Recipe("Пирог", [Ingredient("Мука", 300, "г")])
    shopping_list = ShoppingList()

    shopping_list.add_recipe(first_recipe, 1)
    shopping_list.add_recipe(second_recipe, 1)

    result = shopping_list.get_list()

    assert len(result) == 1
    assert result[0].name == "Мука"
    assert result[0].quantity == 800.0


def test_shopping_list_result_is_sorted_by_name():
    recipe = Recipe("Завтрак", [
        Ingredient("Яйцо", 2, "шт"),
        Ingredient("Мука", 500, "г"),
    ])
    shopping_list = ShoppingList()

    shopping_list.add_recipe(recipe, 1)

    result = shopping_list.get_list()

    assert result[0].name == "Мука"
    assert result[1].name == "Яйцо"


def test_shopping_list_add_two_lists():
    first_recipe = Recipe("Блины", [Ingredient("Мука", 500, "г")])
    second_recipe = Recipe("Омлет", [Ingredient("Яйцо", 2, "шт")])

    first_list = ShoppingList()
    second_list = ShoppingList()

    first_list.add_recipe(first_recipe, 1)
    second_list.add_recipe(second_recipe, 1)

    new_list = first_list + second_list
    result = new_list.get_list()

    assert len(result) == 2
    assert len(first_list.get_list()) == 1
    assert len(second_list.get_list()) == 1
def test_dietary_recipe_creation():
    recipe = DietaryRecipe("Салат", "веган", [
        Ingredient("Огурец", 2, "шт")
    ])

    assert recipe.title == "Салат"
    assert recipe.diet_type == "веган"
    assert len(recipe) == 1


def test_dietary_recipe_scale_returns_dietary_recipe():
    recipe = DietaryRecipe("Салат", "веган", [
        Ingredient("Огурец", 2, "шт")
    ])

    scaled_recipe = recipe.scale(3)

    assert isinstance(scaled_recipe, DietaryRecipe)
    assert scaled_recipe.title == "Салат"
    assert scaled_recipe.diet_type == "веган"
    assert scaled_recipe.ingredients[0].quantity == 6.0


def test_dietary_recipe_str_contains_diet_type():
    recipe = DietaryRecipe("Салат", "веган", [
        Ingredient("Огурец", 2, "шт")
    ])

    assert str(recipe).startswith("[веган]")
