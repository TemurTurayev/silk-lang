"""
Tests for dict .toAppStreamConfig() method - format as Amazon AppStream config.
"""

from silk.interpreter import Interpreter


class TestDictToAppStreamConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppStreamConfig_basic(self):
        output = self._run('print({"fleet": "default"}.toAppStreamConfig())')
        assert output[-1] == "fleet = default"

    def test_toAppStreamConfig_multi(self):
        output = self._run('print({"fleet": "default", "type": "ondemand"}.toAppStreamConfig())')
        assert "fleet = default" in output[-1]
