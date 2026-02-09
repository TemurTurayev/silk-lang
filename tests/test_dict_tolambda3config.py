"""
Tests for dict .toLambda3Config() method - format as Lambda v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToLambda3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLambda3Config_basic(self):
        output = self._run('print({"runtime": "python3.12"}.toLambda3Config())')
        assert output[-1] == "runtime = python3.12"

    def test_toLambda3Config_multi(self):
        output = self._run('print({"runtime": "python3.12", "memory": 256}.toLambda3Config())')
        assert output[-1] == "runtime = python3.12\nmemory = 256"
