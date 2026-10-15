"""Contract tests for core methodology resources shipped to every integration."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / ".agents" / "skills" / "vedic-core" / "resources"
INTEGRATIONS = ("codex", "antigravity", "claude-code")


class CoreResourceSyncTests(unittest.TestCase):
    def test_house_framework_contains_required_diagnostic_contract(self):
        text = (CANONICAL / "house_framework.md").read_text(encoding="utf-8")
        required = (
            "## 诊断四维度",
            "## 宫位评级",
            "## 12宫速查",
            "## 多阶段事件推导",
            "## Dasha事件推导硬约束（必须严格执行）",
            "### Dasha事件优先级（多事件同期激活时的排序规则）",
            "## Badhaka（障碍星）审计",
            "## Maraka（杀手星）审计",
        )
        for heading in required:
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_house_framework_is_identical_in_every_distribution(self):
        canonical = (CANONICAL / "house_framework.md").read_bytes()
        for integration in INTEGRATIONS:
            distributed = (
                ROOT / integration / "skills" / "vedic-core" / "resources"
                / "house_framework.md"
            )
            with self.subTest(integration=integration):
                self.assertEqual(canonical, distributed.read_bytes())


if __name__ == "__main__":
    unittest.main()
