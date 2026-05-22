from .dark_splellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = [item.lower() for item in dark_spell_allowed_ingredients()]
    items = [i.lower().strip() for i in ingredients.split(",")]
    if any(item in allowed for item in items):
        return f"{ingredients} VALID"
    else:
        return f"{ingredients} INVALID"

# mypy is not allowed on this one+
