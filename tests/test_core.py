"""Automated test suite for API Migration Linter."""
import unittest
from agent_api_deprecation_migration_linter.core import APIMigrationLinter, MigrationRule

class TestAPIMigrationLinter(unittest.TestCase):
    def test_rule_application(self):
        linter = APIMigrationLinter()
        linter.add_rule(MigrationRule(r"legacy_init\(", "modern_init(", "Upgrade init"))
        code = "obj = legacy_init()"
        migrated, msgs = linter.migrate(code)
        self.assertEqual(migrated, "obj = modern_init()")
        self.assertEqual(len(msgs), 1)
