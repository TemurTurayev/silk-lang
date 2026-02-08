"""
Tests for dict .toPersonalizeConfig() method - format as Personalize config.
"""

from silk.interpreter import Interpreter


class TestDictToPersonalizeConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPersonalizeConfig_basic(self):
        output = self._run('print({"dataset": "users"}.toPersonalizeConfig())')
        assert output[-1] == "dataset = users"

    def test_toPersonalizeConfig_multi(self):
        output = self._run('print({"recipe": "trending", "events": 1000}.toPersonalizeConfig())')
        assert "recipe = trending" in output[-1]
