"""
Tests for dict .toWorkSpacesConfig() method - format as Amazon WorkSpaces config.
"""

from silk.interpreter import Interpreter


class TestDictToWorkSpacesConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWorkSpacesConfig_basic(self):
        output = self._run('print({"bundle": "standard"}.toWorkSpacesConfig())')
        assert output[-1] == "bundle = standard"

    def test_toWorkSpacesConfig_multi(self):
        output = self._run('print({"bundle": "standard", "mode": "alwayson"}.toWorkSpacesConfig())')
        assert "bundle = standard" in output[-1]
