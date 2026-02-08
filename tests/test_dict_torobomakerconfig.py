"""
Tests for dict .toRoboMakerConfig() method - format as AWS RoboMaker config.
"""

from silk.interpreter import Interpreter


class TestDictToRoboMakerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRoboMakerConfig_basic(self):
        output = self._run('print({"robot": "main"}.toRoboMakerConfig())')
        assert output[-1] == "robot = main"

    def test_toRoboMakerConfig_multi(self):
        output = self._run('print({"robot": "main", "env": "staging"}.toRoboMakerConfig())')
        assert "robot = main" in output[-1]
