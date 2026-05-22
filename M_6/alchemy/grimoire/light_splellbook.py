

def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # importação local, evita circularidade
    from .light_validator import validate_ingredients
    if "INVALID" in validate_ingredients(ingredients):
        return f"{spell_name} rejected"
    else:
        return f"{spell_name} recorded"
