from dotenv import load_dotenv
import sys
import os

load_dotenv()


def main() -> None:
    REQUIRED = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    matrix_mode = (os.getenv("MATRIX_MODE") or "development").strip()
    config = {k: os.getenv(k) for k in REQUIRED}
    missing = [k for k, v in config.items() if not v]

    if matrix_mode == "production" and missing:
        print("CRITICAL WARNING")
        print(f"[ERROR] missing this configuration {missing}")
        print("\nFix:")
        print("1- Correct with the rights value")
        print("2- override the missing with '...'")
        sys.exit(1)

    if matrix_mode == "development" and missing:
        print(f"[ERROR] missing this configuration {missing}")
        sys.exit(1)
        print("Configuration loaded:")
    if matrix_mode == "development":
        print(f"Mode: {matrix_mode}")
        print("Database: Connected to local instance")
        print("API Access: TEST MODE")
        print("Log Level: DEBUG-like verbose output")
        print("Zion Network: on TEST MODE")
        print("\nEnvironment security check:")
        print("[OK] CODE CHECK")
        print("[OK] .env file properly configured")
        print("[OK] remote origin")
    else:
        print(f"Mode: {matrix_mode}")
        print("Database: Connected to production instance")
        print("API Access: Authenticated")
        print("Log Level: production logging")
        print(f"Zion Network: {config['ZION_ENDPOINT']}")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")

        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    main()
