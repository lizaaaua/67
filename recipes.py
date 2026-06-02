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
    pass


class ShoppingList:
    pass


class DietaryRecipe:
    pass
