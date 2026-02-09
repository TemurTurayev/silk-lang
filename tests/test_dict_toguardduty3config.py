"""
Tests for dict .toGuardDuty3Config() method - format dict as GuardDuty3 config.
"""

from silk.interpreter import Interpreter


class TestDictToGuardDuty3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGuardDuty3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toGuardDuty3Config())')
        assert output[-1] == "host = localhost"

    def test_toGuardDuty3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toGuardDuty3Config())')
        assert output[-1] == "host = localhost\nport = 443"
