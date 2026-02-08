"""
Tests for dict .toLambdaConfig() method - format as Lambda config.
"""

from silk.interpreter import Interpreter


class TestDictToLambdaConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLambdaConfig_basic(self):
        output = self._run('print({"handler": "main"}.toLambdaConfig())')
        assert output[-1] == "handler = main"

    def test_toLambdaConfig_multi(self):
        output = self._run('print({"timeout": 30, "memory": 512}.toLambdaConfig())')
        assert "memory = 512" in output[-1]
