import os
import sys
import site


def is_deactivate() -> bool:
    return sys.prefix == sys.base_prefix


def main() -> None:
    print("MATRIX STATUS: ", end="")
    if is_deactivate():
        print("You're still plugged in")
    else:
        print("Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    if is_deactivate():
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        venv_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()
