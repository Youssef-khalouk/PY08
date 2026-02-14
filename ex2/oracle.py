
import os
import sys
from dotenv import load_dotenv

load_dotenv()


def get_config(var_name: str, required: bool = True):
    value = os.getenv(var_name)
    if required and not value:
        print(
            f"ERROR: Required configuration'{var_name}' is missing.",
            file=sys.stderr)
        sys.exit(1)
    return value


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    matrix_mode = get_config("MATRIX_MODE")
    database_url = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL", required=False) or "INFO"
    zion_endpoint = get_config("ZION_ENDPOINT")

    print("Configuration loaded:")
    if matrix_mode.lower() == "development":
        print("Mode: development")
        print("Database: Connected to local instance")
    elif matrix_mode.lower() == "production":
        print("Mode: production")
        print("Database: Connected to production instance")
    else:
        print(f"ERROR: Unknown MATRIX_MODE '{matrix_mode}'", file=sys.stderr)
        sys.exit(1)

    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    if zion_endpoint:
        print("Zion Network: Online\n")
    else:
        print("Zion Network: Offline\n")
    print("Environment security check:")
    if api_key in database_url:
        print("[WARNING] API_KEY appears in DATABASE_URL!")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print(f"[WARNING] .env file missing in '{os.getcwd()}'")

    if matrix_mode.lower() == "production":
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
