"""Core API deprecation migration linter."""
import re
from typing import List, Tuple

class MigrationRule:
    def __init__(self, deprecated_pattern: str, modern_replacement: str, message: str):
        self.deprecated_pattern = re.compile(deprecated_pattern)
        self.replacement = modern_replacement
        self.message = message

class APIMigrationLinter:
    def __init__(self):
        self.rules: List[MigrationRule] = []

    def add_rule(self, rule: MigrationRule):
        self.rules.append(rule)

    def migrate(self, source_code: str) -> Tuple[str, List[str]]:
        migrated = source_code
        applied_messages = []

        for rule in self.rules:
            if rule.deprecated_pattern.search(migrated):
                migrated = rule.deprecated_pattern.sub(rule.replacement, migrated)
                applied_messages.append(rule.message)

        return migrated, applied_messages
