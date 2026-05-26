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
    print("\n")
    print(f"Current Python: {sys.base_prefix}")
    if is_deactivate():
        print("Virtual Environment: None detected")
        print("\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\n")
        print("Then run this program again.")
    else:
        venv_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(site.getsitepackages())


if __name__ == "__main__":
    main()
