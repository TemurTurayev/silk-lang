"""
Tests for dict .toBudgets3Config() method - format dict as Budgets3 config.
"""

from silk.interpreter import Interpreter


class TestDictToBudgets3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBudgets3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toBudgets3Config())')
        assert output[-1] == "host = localhost"

    def test_toBudgets3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toBudgets3Config())')
        assert output[-1] == "host = localhost\nport = 443"
