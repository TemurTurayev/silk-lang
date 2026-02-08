"""
Tests for dict .toShieldConfig() method - format as Shield config.
"""

from silk.interpreter import Interpreter


class TestDictToShieldConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toShieldConfig_basic(self):
        output = self._run('print({"protection": "advanced"}.toShieldConfig())')
        assert output[-1] == "protection = advanced"

    def test_toShieldConfig_multi(self):
        output = self._run('print({"autoRenew": true, "tier": "business"}.toShieldConfig())')
        assert "tier = business" in output[-1]
