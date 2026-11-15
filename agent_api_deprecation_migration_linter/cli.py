"""CLI for API Migration Linter."""
import argparse
from .core import APIMigrationLinter, MigrationRule

def main():
    parser = argparse.ArgumentParser(description="API Migration Linter CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate API deprecation codemod")
    args = parser.parse_args()

    linter = APIMigrationLinter()
    linter.add_rule(MigrationRule(
        r"old_client\.fetch_data\(",
        "new_client.stream_data(mode='fast', ",
        "Migrated fetch_data to modern stream_data"
    ))

    code = "result = old_client.fetch_data('users')"
    new_code, msgs = linter.migrate(code)
    print(f"Original: {code}")
    print(f"Migrated: {new_code}")
    print(f"Applied Changes: {msgs}")

if __name__ == "__main__":
    main()
