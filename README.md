# Домашнее задание N2: рецепты

Проект представляет собой простую систему для работы с рецептами и списком покупок.

В проекте реализованы классы:

- `Ingredient` - ингредиент с названием, количеством и единицей измерения.
- `Recipe` - рецепт блюда со списком ингредиентов.
- `ShoppingList` - список покупок, который объединяет ингредиенты из разных рецептов.
- `DietaryRecipe` - рецепт с диетической категорией.

## Установка

Склонируйте репозиторий:

```bash
git clone https://github.com/lizaaaua/67.git
cd 67
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Использование

Классы находятся в файле:

```text
recipes.py
```

Пример использования:

```python
from recipes import Ingredient, Recipe, ShoppingList

recipe = Recipe("Блины")
recipe.add_ingredient(Ingredient("Мука", 500, "г"))
recipe.add_ingredient(Ingredient("Яйцо", 2, "шт"))

shopping_list = ShoppingList()
shopping_list.add_recipe(recipe, 2)

for ingredient in shopping_list.get_list():
    print(ingredient)
```

## Запуск тестов

```bash
pytest
```

Если команда `pytest` не работает, можно запустить так:

```bash
python -m pytest
```

## Автор

Нечепоренко Елизавета Евгеньевна

Группа: ББИ2510
