class Ingredient:

    def __init__(self, name: str, quantity: float, unit: str):
        self._name = name
        self._quantity = None
        self._unit = unit
        self.quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, value) -> None:
        value = float(value)

        if value <= 0:
            raise ValueError("Количество должно быть положительным")

        self._quantity = value

    @property
    def unit(self) -> str:
        return self._unit
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"
    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    def __eq__(self, other) -> bool:
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

class Recipe:
    def __init__(self, title: str, ingredients: Optional[List[Ingredient]] = None):
        self.title = title
        self._ingredients = ingredients if ingredients is not None else []

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients.copy()

    def add_ingredient(self, ingredient: Ingredient) -> None:
        for existing in self._ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self._ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        try:
            ratio = float(ratio)
            return ratio > 0
        except (TypeError, ValueError):
            return False

    def scale(self, ratio: float) -> "Recipe":
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным")
        ratio = float(ratio)
        scaled_ingredients = []
        for ingredient in self._ingredients:
            scaled_ingredient = Ingredient(
                ingredient.name,
                ingredient.quantity * ratio,
                ingredient.unit
            )
            scaled_ingredients.append(scaled_ingredient)

        return Recipe(self.title, scaled_ingredients)

    def __len__(self) -> int:
        return len(self._ingredients)
    def __str__(self) -> str:
        result = f"Рецепт: {self.title}\n"
        result += "Ингредиенты:\n"

        for ingredient in self._ingredients:
            result += f"- {ingredient}\n"
        return result


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str) -> None:
        new_items = []

        for ingredient, recipe_title in self._items:
            if recipe_title != title:
                new_items.append((ingredient, recipe_title))

        self._items = new_items

    def get_list(self) -> List[Ingredient]:
        result = {}

        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)

            if key not in result:
                result[key] = 0

            result[key] += ingredient.quantity

        shopping_list = []

        for key in result:
            name, unit = key
            quantity = result[key]
            shopping_list.append(Ingredient(name, quantity, unit))

        shopping_list.sort(key=lambda ingredient: ingredient.name)

        return shopping_list

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items.copy() + other._items.copy()
        return new_list


class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: Optional[List[Ingredient]] = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float) -> "DietaryRecipe":
        scaled_recipe = super().scale(ratio)

        return DietaryRecipe(
            scaled_recipe.title,
            self.diet_type,
            scaled_recipe.ingredients
        )

    def __str__(self) -> str:
        return f"[{self.diet_type}] {super().__str__()}"
