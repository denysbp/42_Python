import importlib
from importlib.metadata import version
from typing import Any


def check_imports(package: str, util: str) -> bool:
    try:
        importlib.import_module(package)
        try:
            v = version(package)
        except Exception:
            v = "unknown"
        print(f"[OK] {package} ({v}) - {util}")
        return True
    except ModuleNotFoundError:
        print(f"[MISSING] {package}")
        return False


def process_data(n: int = 1000) -> dict[str, Any]:
    import numpy as np

    rng = np.random.default_rng(42)
    signal = rng.normal(loc=50, scale=15, size=n)
    noise = rng.integers(low=0, high=100, size=n)
    score = np.abs(signal - signal.mean())

    return {
        "signal": signal,
        "noise": noise,
        "score": score
    }


def analyze_matrix_data() -> None:
    import numpy as np
    import pandas as pd  # type: ignore[import-untyped]
    import matplotlib.pyplot as plt  # type: ignore[import-not-found]

    data = process_data(1000)
    df = pd.DataFrame(data)
    print(df)
    weird_data = np.percentile(df["score"], 98)
    df["anomaly"] = df["score"] >= weird_data
    plt.plot(df["signal"], label="signal")
    plt.scatter(
        df.index[df["anomaly"]],
        df.loc[df["anomaly"], "signal"],
        color="blue",
        s=15,
        label="anomaly"
    )
    plt.title("Matrix Analysis")
    plt.legend()
    plt.tight_layout()
    plt.xlabel("index")
    plt.ylabel("signal")
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    print("Checking dependencies:")
    find_np = check_imports("numpy", "Numerical computation ready")
    find_pd = check_imports("pandas", "Data manipulation ready")
    find_mat = check_imports("matplotlib", "Visualization ready")
    if not (find_mat and find_np and find_pd):
        names = {
            "pandas": find_pd,
            "numpy": find_np,
            "matplotlib": find_mat,
        }
        missing = {name for name, value in names.items() if not value}
        print(f"\nWe detected missing modules: {missing}")
        print("Try create a env: ", end="")
        print("python3 -m venv venv")
        print("For pip: python3 -m pip install -r requirements.txt")
        print("For poetry: poetry install")
        return
    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    analyze_matrix_data()
    print("Generating visualization...")
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print()
    main()
