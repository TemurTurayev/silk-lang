"""
Tests for dict .toNeptuneServerless3Config() method - format as Neptune Serverless v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToNeptuneServerless3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNeptuneServerless3Config_basic(self):
        output = self._run('print({"capacity": "auto"}.toNeptuneServerless3Config())')
        assert output[-1] == "capacity = auto"

    def test_toNeptuneServerless3Config_multi(self):
        output = self._run('print({"capacity": "auto", "maxNCU": 128}.toNeptuneServerless3Config())')
        assert output[-1] == "capacity = auto\nmaxNCU = 128"
