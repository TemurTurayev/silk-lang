"""
Tests for number .isSmith() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsSmith:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSmith_true(self):
        output = self._run('print(22.isSmith())')
        assert output[-1] == "true"

    def test_isSmith_false(self):
        output = self._run('print(23.isSmith())')
        assert output[-1] == "false"

    def test_isSmith_4(self):
        output = self._run('print(4.isSmith())')
        assert output[-1] == "true"
