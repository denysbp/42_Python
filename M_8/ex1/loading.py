import importlib
from importlib.metadata import version


def check_imports(packeage: str, util: str) -> bool:
    try:
        importlib.import_module(f"{packeage}")
        print(f"[OK] {packeage} ({version(f"{packeage}")}) - {util}")
        return True
    except ModuleNotFoundError:
        print(f"[MISSING] {packeage}")
        return False

# curl -sSL https://install.python-poetry.org | python3 -


def main() -> None:
    find_np = check_imports("numpy", "Data manipulation ready")
    find_pd = check_imports("pandas", "Numerical computation ready")
    find_rq = check_imports("requests", "Network access ready")
    find_mat = check_imports("matplotlib", "Visualization ready")
    if not (find_mat and find_rq and find_np and find_pd):
        names = {
            "pandas": find_pd,
            "numpy": find_np,
            "requests": find_rq,
            "matplotlib": find_mat
        }
        missing = {name for name, value in names.items() if not value}
        print(f"\nWe detected missing modules: {missing}")
        print("Try create a env: ", end="")
        print("python3 -m venv venv")
        print("For pip; python3 pip install -r requirements.txt")
        print("For poetry: poetry install")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    main()
