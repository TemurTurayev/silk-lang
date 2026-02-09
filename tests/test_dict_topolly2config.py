"""
Tests for dict .toPolly2Config() method - format as Polly v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToPolly2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPolly2Config_basic(self):
        output = self._run('print({"voice": "Joanna"}.toPolly2Config())')
        assert output[-1] == "voice = Joanna"

    def test_toPolly2Config_multi(self):
        output = self._run('print({"voice": "Joanna", "engine": "neural"}.toPolly2Config())')
        assert output[-1] == "voice = Joanna\nengine = neural"
