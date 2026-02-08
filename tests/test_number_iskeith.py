"""
Tests for number .isKeith() method - Keith number check.
"""

from silk.interpreter import Interpreter


class TestNumberIsKeith:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isKeith_14(self):
        output = self._run('print(14.isKeith())')
        assert output[-1] == "true"

    def test_isKeith_197(self):
        output = self._run('print(197.isKeith())')
        assert output[-1] == "true"

    def test_isKeith_15(self):
        output = self._run('print(15.isKeith())')
        assert output[-1] == "false"
