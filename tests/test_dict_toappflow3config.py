"""
Tests for dict .toAppFlow3Config() method - format as AppFlow v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAppFlow3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppFlow3Config_basic(self):
        output = self._run('print({"source": "salesforce"}.toAppFlow3Config())')
        assert output[-1] == "source = salesforce"

    def test_toAppFlow3Config_multi(self):
        output = self._run('print({"source": "salesforce", "dest": "s3"}.toAppFlow3Config())')
        assert output[-1] == "source = salesforce\ndest = s3"
