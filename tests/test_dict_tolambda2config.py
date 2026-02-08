"""
Tests for dict .toLambda2Config() method - format as Lambda config.
"""

from silk.interpreter import Interpreter


class TestDictToLambda2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLambda2Config_basic(self):
        output = self._run('print({"functionName": "my-handler"}.toLambda2Config())')
        assert output[-1] == "functionName = my-handler"

    def test_toLambda2Config_multi(self):
        output = self._run('print({"functionName": "my-handler", "runtime": "python3.12"}.toLambda2Config())')
        assert "functionName = my-handler" in output[-1]
