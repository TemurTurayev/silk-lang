"""
Tests for dict .toComprehendConfig() method - format as Comprehend config.
"""

from silk.interpreter import Interpreter


class TestDictToComprehendConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toComprehendConfig_basic(self):
        output = self._run('print({"language": "en"}.toComprehendConfig())')
        assert output[-1] == "language = en"

    def test_toComprehendConfig_multi(self):
        output = self._run('print({"model": "custom", "endpoint": "prod"}.toComprehendConfig())')
        assert "model = custom" in output[-1]
