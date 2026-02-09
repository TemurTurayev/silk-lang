"""
Tests for dict .toSageMaker3Config() method - format as SageMaker v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToSageMaker3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSageMaker3Config_basic(self):
        output = self._run('print({"endpoint": "my-model"}.toSageMaker3Config())')
        assert output[-1] == "endpoint = my-model"

    def test_toSageMaker3Config_multi(self):
        output = self._run('print({"endpoint": "my-model", "instance": "ml.m5.large"}.toSageMaker3Config())')
        assert output[-1] == "endpoint = my-model\ninstance = ml.m5.large"
