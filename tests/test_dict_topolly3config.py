"""
Tests for dict .toPolly3Config() method - format as Polly v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToPolly3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPolly3Config_basic(self):
        output = self._run('print({"voice": "Joanna"}.toPolly3Config())')
        assert output[-1] == "voice = Joanna"

    def test_toPolly3Config_multi(self):
        output = self._run('print({"voice": "Joanna", "engine": "neural"}.toPolly3Config())')
        assert output[-1] == "voice = Joanna\nengine = neural"
