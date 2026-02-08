"""
Tests for dict .toAutoScalingConfig() method - format as AWS Auto Scaling config.
"""

from silk.interpreter import Interpreter


class TestDictToAutoScalingConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAutoScalingConfig_basic(self):
        output = self._run('print({"group": "web-asg"}.toAutoScalingConfig())')
        assert output[-1] == "group = web-asg"

    def test_toAutoScalingConfig_multi(self):
        output = self._run('print({"group": "web-asg", "min": 2}.toAutoScalingConfig())')
        assert "group = web-asg" in output[-1]
