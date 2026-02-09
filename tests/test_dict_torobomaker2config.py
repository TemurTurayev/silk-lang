"""
Tests for dict .toRoboMaker2Config() method - format as RoboMaker v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToRoboMaker2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRoboMaker2Config_basic(self):
        output = self._run('print({"robot": "arm"}.toRoboMaker2Config())')
        assert output[-1] == "robot = arm"

    def test_toRoboMaker2Config_multi(self):
        output = self._run('print({"robot": "arm", "sim": "gazebo"}.toRoboMaker2Config())')
        assert output[-1] == "robot = arm\nsim = gazebo"
