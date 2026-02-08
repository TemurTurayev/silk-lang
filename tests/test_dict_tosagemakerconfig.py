"""
Tests for dict .toSageMakerConfig() method - format as SageMaker config.
"""

from silk.interpreter import Interpreter


class TestDictToSageMakerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSageMakerConfig_basic(self):
        output = self._run('print({"model": "xgboost"}.toSageMakerConfig())')
        assert output[-1] == "model = xgboost"

    def test_toSageMakerConfig_multi(self):
        output = self._run('print({"instance": "ml.m5", "count": 2}.toSageMakerConfig())')
        assert "count = 2" in output[-1]
