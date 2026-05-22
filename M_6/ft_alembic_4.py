import alchemy

print("=== Alembic 4 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")
print(alchemy.create_air())
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print(alchemy.create_earth())
