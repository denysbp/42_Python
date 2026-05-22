from .light_splellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = [item.lower() for item in light_spell_allowed_ingredients()]
    items = [i.lower().strip() for i in ingredients.split(",")]
    if any(item in allowed for item in items):
        return f"{ingredients} VALID"
    else:
        return f"{ingredients} INVALID"
