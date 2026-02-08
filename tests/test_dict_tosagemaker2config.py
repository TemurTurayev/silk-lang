"""
Tests for dict .toSageMaker2Config() method - format as SageMaker config.
"""

from silk.interpreter import Interpreter


class TestDictToSageMaker2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSageMaker2Config_basic(self):
        output = self._run('print({"endpointName": "my-endpoint"}.toSageMaker2Config())')
        assert output[-1] == "endpointName = my-endpoint"

    def test_toSageMaker2Config_multi(self):
        output = self._run('print({"endpointName": "my-endpoint", "instanceType": "ml.m5.large"}.toSageMaker2Config())')
        assert "endpointName = my-endpoint" in output[-1]
