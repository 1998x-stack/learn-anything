"""Regression checks for accessible animation and keyboard focus styles."""
from pathlib import Path
import re
import unittest

HTML = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")


class AccessibilityStylesTest(unittest.TestCase):
    def test_reduced_motion_disables_card_animation_and_transform(self):
        match = re.search(
            r"@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{"
            r"(?P<rules>.*?)\n  \}",
            HTML, re.DOTALL,
        )
        self.assertIsNotNone(match)
        rules = match.group("rules")
        self.assertRegex(rules, r"\.method-card\s*\{[^}]*animation:\s*none\s*;")
        self.assertRegex(rules, r"\.method-card\s*\{[^}]*transition:\s*none\s*;")
        self.assertRegex(rules, r"\.method-card:hover\s*\{[^}]*transform:\s*none\s*;")

    def test_keyboard_focus_has_visible_outline(self):
        self.assertRegex(
            HTML,
            r"footer a:focus-visible\s*\{[^}]*outline:\s*2px solid var\(--accent\)",
        )

    def test_default_animation_remains_for_other_users(self):
        self.assertIn("animation: fadeIn 0.5s ease-out both;", HTML)


if __name__ == "__main__":
    unittest.main()
