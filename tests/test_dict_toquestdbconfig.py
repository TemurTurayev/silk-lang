"""
Tests for dict .toQuestDBConfig() method - QuestDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToQuestDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuestDBConfig_basic(self):
        output = self._run('print({"port": 9000}.toQuestDBConfig())')
        assert output[-1] == "port = 9000"

    def test_toQuestDBConfig_string(self):
        output = self._run('print({"host": "localhost"}.toQuestDBConfig())')
        assert output[-1] == "host = localhost"
