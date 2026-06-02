from typing import List, Optional
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
    pass


class DietaryRecipe:
    pass
