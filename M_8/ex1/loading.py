import importlib
from importlib.metadata import version, PackageNotFoundError
from typing import Any


def check_imports(packeage: str, util: str) -> bool:
    try:
        importlib.import_module(f"{packeage}")
        print(f"[OK] {packeage} ({version(packeage)}) - {util}")
        return True
    except ModuleNotFoundError:
        print(f"[MISSING] {packeage}")
        return False
    except PackageNotFoundError:
        print(f"[MISSING] {packeage} ('unknown') - {util}")
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
    plt.title("Matrix Analize")
    plt.legend()
    plt.tight_layout()
    plt.xlabel("index")
    plt.ylabel("signal")
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    print("Checking dependencies:")
    find_np = check_imports("numpy", "Numerical computatio ready")
    find_pd = check_imports("pandas", "Data manipulation ready")
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
        print("For pip: python3 -m pip install -r requirements.txt")
        print("For poetry: poetry install")
        return
    print("\n")
    print("Analyzing Matrix data...")
    process_data()
    print("Processing 1000 data points...")
    analyze_matrix_data()
    print("Generating visualization...")
    print("\n")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print("\n")
    main()
